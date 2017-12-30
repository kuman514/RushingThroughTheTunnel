import sys
import pygame
from pygame.locals import *

import Player
import Enemies
import GameOBJ


TargetFPS = 60
pygame.init()
_display = pygame.display.set_mode((1280, 720), DOUBLEBUF)
pygame.display.set_caption('Rushing Through The Tunnel')
clock = pygame.time.Clock()


def main():
    while True:
        # Event Handle
        for Event in pygame.event.get():
            if Event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Key Input
        _key = pygame.key.get_pressed()
        if _key[pygame.constants.K_RETURN]:
            print 'game start'
            game()
        elif _key[pygame.constants.K_ESCAPE]:
            print 'exit to windows'
            pygame.quit()
            sys.exit()

        # Object State Update

        # Display Init
        _display.fill(0x000000)

        # Draw
        pygame.display.update()
        clock.tick(TargetFPS)


def game():
    while True:
        # Event Handle
        for Event in pygame.event.get():
            if Event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Key Input
        _key = pygame.key.get_pressed()
        if _key[pygame.constants.K_ESCAPE]:
            print 'return to title'
            return

        # Object State Update

        # Display Init
        _display.fill(0x000000)

        # Draw
        pygame.display.update()
        clock.tick(TargetFPS)


if __name__ == '__main__':
    main()
