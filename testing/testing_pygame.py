def flappy_bird():
    import pygame
    import sys
    import random
    pygame.init()

    class Bird(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            original = pygame.image.load("testing/bird.png").convert_alpha()
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
            self.angle = self.velocity * -5
            if self.angle < -90:
                self.angle = -90
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            run = True
            if bird.rect.bottom > screen_height - 10:
                run = False
                return run
        
        def jump(self):
            self.velocity = 0
            self.velocity -= 12
    
    class Pipe(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            original = pygame.image.load("testing/pipe.png").convert_alpha()
            self.original_image = pygame.transform.scale(original, (50, 1000))
            self.image = self.original_image
            self.rect = self.image.get_rect()
            self.rect.center = (screen_width - (screen_width // 4), screen_height // 2)
            self.point = [screen_width, screen_height-(50+(random.randint(1,750)))]
        
        def update(self):
            self.point[0] -= 5
            self.rect.centerx -= 5
    
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    score = 0
    screen_width, screen_height = pygame.display.get_surface().get_size()
    pygame.display.set_caption("Flappy Bird")

    bird = Bird()
    bird_group = pygame.sprite.Group()
    bird_group.add(bird)

    pipe = Pipe()
    pipe_group = pygame.sprite.Group()
    pipe_group.add(pipe)
    
    running = True
    start = False
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
            if pygame.sprite.collide_rect(bird_group, pipe_group) == True:
                running = False

        # SET UP
        screen.fill("light blue")
        bird_group.draw(screen)
        pipe_group.draw(screen)
        
        # UPDATE
        if start == True:
            # Move dot across x
            # Update pipe
            bird_group.update()
            pipe_group.update()
            if bird.rect.bottom >= screen_height - 10:
                running = False
            if bird.rect.top <= -30:
                running = False
            
            
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
    return score

flappy_bird()