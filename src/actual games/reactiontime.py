import sys
import pygame
import random
import time

def reaction_time_game():
    pygame.init()
    print("This is a reaction time game, click when the screen goes from red to green as fast as you can")
    time.sleep(2)
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, vsync=1)
    screen_width, screen_height = (600,600)
    red = (255,0,0)
    green = (0,255,0)
    running = True
    click_now = False
    early = False
    x=0
    screen.fill(red)
    random.randint(5,20)
    pygame.display.set_caption("Reaction Game")
    pygame.display.flip()
    while running == True:
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and click_now == False:
                running = False
                early = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and click_now == True:
                running = False
                early = False
                reaction_time = clock.get_rawtime()
            if x == 5 and click_now == False:
                click_now = True
                screen.fill(green)
                pygame.display.flip()
                clock.tick(50)
            if x < 5:
                x+=1
    if early == False:
        print(f'{reaction_time}ms')
    elif early == True:
        print("You clicked too early")
    pass
reaction_time_game()