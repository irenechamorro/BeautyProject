import pygame
import pygame.locals import *

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((1000, 500))
    surface.fill((255,255,255))
    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pass
            elif eveny.type == QUIT:
                running = False
