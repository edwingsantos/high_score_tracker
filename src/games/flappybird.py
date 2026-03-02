#Flappy Bird

def flappy_bird():
    import pygame
    import random
    pygame.init()
    class Bird(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            original = pygame.image.load("sprites/bird.png").convert_alpha()
            self.original_image = pygame.transform.scale(original, (80, 50))
            self.image = self.original_image
            self.rect = self.image.get_rect()
            self.rect.center = [screen_width // 4, screen_height // 2]
            self.velocity = 0
            self.gravity = .4
            self.angle = 0
        
        def update(self):
            self.velocity += self.gravity
            self.rect.y += self.velocity
            self.angle = self.velocity * -6
            if self.angle < -90:
                self.angle = -90
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
        
        def jump(self):
            self.velocity = 0
            self.velocity -= 12
    
    class PipeTop(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            original = pygame.image.load("sprites/pipe.png").convert_alpha()
            self.image = pygame.transform.scale(original, (100, 1200))
            self.rect = self.image.get_rect()

        def update(self):
            self.rect.centerx -= 5

    class PipeBottom(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            original = pygame.image.load("sprites/pipe.png").convert_alpha()
            self.image = pygame.transform.scale(original, (100, 1200))
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect()

        def update(self):
            self.rect.centerx -= 5
    
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, vsync=1)
    clock = pygame.time.Clock()
    font = pygame.font.Font("sprites/font.TTF", size= 48)
    score = 0
    screen_width, screen_height = pygame.display.get_surface().get_size()
    pygame.display.set_caption("Flappy Bird")
    #width - 2560
    #height - 1440

    bird = Bird()
    bird_group = pygame.sprite.Group()
    bird_group.add(bird)

    gap = 260
    margin = 120
    def spawn_pipes():
        gap_center = random.randint(margin, screen_height - margin)
        top_y = gap_center - gap // 2
        bottom_y = gap_center + gap // 2
        pipe1.rect.midbottom = (screen_width, top_y)
        pipe2.rect.midtop = (screen_width, bottom_y)

    pipe1 = PipeTop()
    pipe1_group = pygame.sprite.Group()
    pipe1_group.add(pipe1)
    pipe2 = PipeBottom()
    pipe2_group = pygame.sprite.Group()
    pipe2_group.add(pipe2)
    spawn_pipes()

    bg = pygame.image.load("sprites/bg.png").convert()
    # Scale the image to the screen size
    bg = pygame.transform.scale(bg, (screen_width, screen_height))


    running = True
    start = False
    passed_pipe = False
    while running:
        # INPUTS
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                running = False
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP or event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                start = True
                bird.jump()
            if pygame.Rect.colliderect(bird.rect, pipe1.rect) == True or pygame.Rect.colliderect(bird.rect, pipe2.rect) == True:
                print("dead to pipe")
                running = False

        # SET UP
        screen.blit(bg, (0, 0))
        bird_group.draw(screen)
        pipe1_group.draw(screen)
        pipe2_group.draw(screen)
        
        # UPDATE
        if start == True:
            bird_group.update()
            pipe1_group.update()
            pipe2_group.update()

            if bird.rect.bottom >= screen_height - 72:
                print("dead to bottom of screen")
                running = False
            if bird.rect.top <= -30:
                print("dead to top of screen")
                running = False
            if pipe1.rect.center[0] < 0:
                spawn_pipes()
                passed_pipe = False
            if pipe1.rect.centerx < bird.rect.centerx and not passed_pipe:
                score += 1
                passed_pipe = True
            if pipe1.rect.right < 0:
                passed_pipe = False

        text_surface = font.render(f"{score}", True, (255,255,255))
        text_rect = text_surface.get_rect()
        text_rect.center = (screen_width // 2, 100)
        screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(45)

    pygame.quit()
    print(f"Score: {score}")
    return score

flappy_bird()