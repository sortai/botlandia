#!/bin/python3
import pygame

defstats = {
    "inp": 30.,
    "nip": .1,
    "dir": 0.
    }

class bot:
    def __init__(self, name, stats = None, affinities = None):
        self.name = name
        if stats is None: stats = dict(defstats)
        if affinites is None: affinities = dict()
        self.timealive = 0;
    def interact(self, olist):
        return 0


if __name__ == '__main__':
    pygame.init()
    size = [512, 512]
    w=size[0]
    h=size[1]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Botlandia")
    done = False
    clock = pygame.time.Clock()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or ( pygame.key.get_pressed()[pygame.K_q] != 0 ):
                done = True
            if ( pygame.key.get_pressed()[pygame.K_w] != 0 ):
                capture=True
        # Set the screen background
        screen.fill((0,0,0))
     
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
     
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # Limit to 20 frames per second
        clock.tick(20)
     
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
    #quit()
