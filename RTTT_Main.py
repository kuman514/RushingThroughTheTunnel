import sys
import pygame
from pygame.locals import *

import Player
import Enemies
import GameOBJ
import Tunnel


TargetFPS = 60
pygame.init()
_display = pygame.display.set_mode((1280, 720), DOUBLEBUF)
pygame.display.set_caption('Rushing Through The Tunnel')
clock = pygame.time.Clock()


def main():
    title = pygame.image.load('title.png')
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
        elif _key[pygame.constants.K_q]:
            print 'exit to windows'
            pygame.quit()
            sys.exit()

        # Object State Update

        # Display Init
        _display.fill(0x000000)

        # Draw
        _display.blit(title, (0, 0))
        pygame.display.update()
        clock.tick(TargetFPS)


def game():
    bg = pygame.image.load('playbg.png')
    tunnel = Tunnel.Tunnel(pygame.image.load('tunnel.png'))
    player = Player.Player(100, 10, pygame.image.load('player.png'))
    dmgobj = pygame.image.load('damageobj.png')
    goldobj = pygame.image.load('goldobj.png')

    tempObj = GameOBJ.DamagePlatform(1, dmgobj)
    tempObj2 = GameOBJ.GoldPlatform(3, goldobj)

    while True:
        # Event Handle
        for Event in pygame.event.get():
            if Event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Display Init
        _display.fill(0x000000)

        # Key Input
        _key = pygame.key.get_pressed()
        if _key[pygame.constants.K_LEFT]:
            player.lane = (player.lane - 1) % 6
        if _key[pygame.constants.K_RIGHT]:
            player.lane = (player.lane + 1) % 6
        if _key[pygame.constants.K_ESCAPE]:
            print 'return to title'
            return

        # Object State Update
        # testing a gold platform and a damaging one
        if tempObj.pos >= 300 and tempObj2.pos >= 300:
            tempObj.pos = 0
            tempObj2.pos = 0
        tempObj.forward(5)
        tempObj2.forward(5)
        tempObj.judge(player)
        tempObj2.judge(player)

        # for o in (objects on each lane) :
        #   if o.pos >= 300:
        #       (remove o)
        #   o.forward(5)
        #   o.judge(player)

        # Draw
        _display.blit(bg, (0, 0))
        tunnel.blit(_display, player)

        tempObj.blit(_display, player)
        tempObj2.blit(_display, player)

        # for o in (objects on each lane) :
        #   o.blit(_display, player)

        player.blit(_display)
        pygame.display.update()
        clock.tick(TargetFPS)


if __name__ == '__main__':
    main()
