#Pong

def pong():
    import pygame
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, vsync=1)
    clock = pygame.time.Clock()
    font = pygame.font.Font("sprites/font.TTF", size=48)
    screen_width, screen_height = screen.get_size()
    pygame.display.set_caption("Pong")
    #width - 2560
    #height - 1440

    score = 0

    class ball(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((20, 20))
            self.image.fill("white")
            self.rect = self.image.get_rect(center=(screen_width//2, screen_height//2))
            self.vx = 10
            self.vy = 10
        
        def update(self):
            self.rect.x += self.vx
            self.rect.y += self.vy
            if self.rect.top <= 0 or self.rect.bottom >= screen_height:
                self.vy *= -1
        
        def bounce(self):
            self.vx *= -1
    
    class player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((20, 120))
            self.image.fill("white")
            self.rect = self.image.get_rect(midleft=(30, screen_height//2))
        
        def up(self):
            self.rect.centery -= 10
        
        def down(self):
            self.rect.centery += 10

        def update(self):
            self.rect.y = max(0, min(screen_height - self.rect.height, self.rect.y))


    class bot(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((20, 120))
            self.image.fill("white")
            self.rect = self.image.get_rect(midright=(screen_width - 30, screen_height//2))

        def update(self):
            if self.rect.centery < ball.rect.centery:
                self.rect.y += 10
            elif self.rect.centery > ball.rect.centery:
                self.rect.y -= 10
            
            self.rect.y = max(0, min(screen_height - self.rect.height, self.rect.y))

    ball = ball()
    ball_group = pygame.sprite.Group(ball)

    player = player()
    player_group = pygame.sprite.Group(player)

    bot = bot()
    bot_group = pygame.sprite.Group(bot)

    running = True
    start = False
    while running:
        # INPUTS
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.up()
            start = True
        if keys[pygame.K_DOWN]:
            player.down()
            start = True

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                running = False
            if event.type == pygame.QUIT:
                running = False

        # SET UP
        screen.fill("black")
        ball_group.draw(screen)
        player_group.draw(screen)
        bot_group.draw(screen)
        
        # UPDATE
        if start == True:
            ball_group.update()
            player_group.update()
            bot_group.update()

            if pygame.Rect.colliderect(ball.rect, player.rect) == True or pygame.Rect.colliderect(ball.rect, bot.rect) == True:
                ball.bounce()
                score += 1
            if ball.rect.centerx < 0 or ball.rect.centerx > screen_width:
                running = False

        text_surface = font.render(f"{score}", True, (255,255,255))
        text_rect = text_surface.get_rect()
        text_rect.center = (screen_width // 2, 100)
        screen.blit(text_surface, text_rect) 

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    print(f"Score: {score}")
    return score

pong()