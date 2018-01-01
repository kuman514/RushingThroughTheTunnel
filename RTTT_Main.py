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
            if game() == 1:
                print 'game over'
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

    objTiming = 0

    while True:
        # Event Handle ===========================================
        for Event in pygame.event.get():
            if Event.type == QUIT:
                pygame.quit()
                sys.exit()
        # ========================================================

        # Display Init ===========================================
        _display.fill(0x000000)
        # ========================================================

        # Key Input ==============================================
        _key = pygame.key.get_pressed()
        if _key[pygame.constants.K_LEFT]:
            player.lane = (player.lane - 1) % 6
        if _key[pygame.constants.K_RIGHT]:
            player.lane = (player.lane + 1) % 6
        if _key[pygame.constants.K_ESCAPE]:
            print 'return to title'
            return 0
        # ========================================================

        # Object State Update ====================================
        for l in tunnel.lanes:
            for o in l:
                o.forward(5)
                o.judge(player)
                if o.pos >= 300:
                    tunnel.removeObj(o.lane, o)

        if objTiming >= 60:
            # generate a new gold object
            tunnel.generateObj((2, goldobj))
            objTiming = 0

        if objTiming % 30 == 0:
            # generate a new damage object
            tunnel.generateObj((1, dmgobj))

        if player.hp <= 0:
            return 1

        objTiming += 1
        # ========================================================

        # Draw ===================================================
        _display.blit(bg, (0, 0))
        tunnel.blit(_display, player)

        for l in tunnel.lanes:
            for o in l:
                o.blit(_display, player)

        player.blit(_display)
        pygame.display.update()
        # ========================================================

        clock.tick(TargetFPS)


if __name__ == '__main__':
    main()
