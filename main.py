# Build a screen and a moving block

import pygame
from pygame.locals import * # import certain global variables


def draw_block():
    surface.fill((110, 110, 5))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()  # update the changes


if __name__ == '__main__':
    pygame.init() # initialize the whole module

    surface = pygame.display.set_mode((500, 500)) # initializing your game window
    surface.fill((110, 110, 5)) # change the background of the game window

    block = pygame.image.load("resources/block.jpg").convert() # Loading the image

    block_x, block_y = 100, 100

    surface.blit(block, (block_x, block_y))

    pygame.display.flip()

    # Event loop
    # Even loop is fundamental to any UI programming
    # Event loop is waiting for user input when you are working on any screen
    # Waiting mouse input or keyboard input

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()
                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()

            elif event.type == QUIT:
                running = False
