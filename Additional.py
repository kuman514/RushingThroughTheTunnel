import pygame


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
            pass

    def blit(self, display):
        # will be implemented
        pass
