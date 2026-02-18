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
    running = True
    while running == True:
        screen.fill(red)
        pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                running = False
    pygame.display.set_caption("Reaction Game")
    pygame.display.flip()
    pass
reaction_time_game()