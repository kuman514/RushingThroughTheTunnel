import sys
import pygame
from pygame.locals import *


class Story(object):
    def __init__(self, stage):
        if stage == 1:
            self.story = pygame.image.load('story1.png')
        elif stage == 2:
            self.story = pygame.image.load('story2.png')
        elif stage == 3:
            self.story = pygame.image.load('story3.png')
        elif stage == 4:
            self.story = pygame.image.load('story4.png')
        else:
            self.story = pygame.image.load('credits.png')

    def blit(self, display, clock, TargetFPS):
        while True:
            # Event Handle
            for Event in pygame.event.get():
                if Event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # Key Input
            _key = pygame.key.get_pressed()
            if _key[pygame.constants.K_RETURN] or _key[pygame.constants.K_ESCAPE]:
                return

            # Display Init
            display.fill(0x000000)

            # Draw
            display.blit(self.story, (0, 0))
            pygame.display.update()
            clock.tick(TargetFPS)
