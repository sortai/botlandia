#!/bin/python3
import pygame
from bots import bot


def init():
    pygame.init()
    global size, w, h, screen
    size = [512, 512]
    w=size[0]
    h=size[1]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Botlandia")

def finish():
    pygame.quit()
    quit()

def main_menu():
    global size, w, h, screen
    done = False
    clock = pygame.time.Clock()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or ( pygame.key.get_pressed()[pygame.K_q] != 0 ):
                finish()
            if ( pygame.key.get_pressed()[pygame.K_b] != 0 ):
                screen = pygame.display.set_mode(size)
            if ( pygame.key.get_pressed()[pygame.K_f] != 0 ):
                screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # background
        screen.fill((0,0,0))
        # draw
        
        pygame.display.flip()
        clock.tick(20)

if __name__ == '__main__':
    init()
    main_menu()
    finish()




