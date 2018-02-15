import sys
import pygame
import pygame._view
from pygame.locals import *

import Player
import Enemies
import GameOBJ
import Tunnel
import Additional


TargetFPS = 60
pygame.init()
_display = pygame.display.set_mode((1280, 720), DOUBLEBUF)
pygame.display.set_caption('Rushing Through The Tunnel')
clock = pygame.time.Clock()


def main():
    title = pygame.image.load('title.png')
    keyInputTiming = 10
    while True:
        # Event Handle
        for Event in pygame.event.get():
            if Event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Key Input
        _key = pygame.key.get_pressed()
        if _key[pygame.constants.K_RETURN]:
            if keyInputTiming <= 0:
                print 'game start'
                result = game()
                if result == 1:
                    print 'game over'
                elif result == 2:
                    Additional.Story(5).blit(_display, clock, TargetFPS)
            keyInputTiming = 10
        elif _key[pygame.constants.K_ESCAPE]:
            if keyInputTiming <= 0:
                print 'exit to windows'
                pygame.quit()
                sys.exit()
        elif _key[pygame.constants.K_c]:
            if keyInputTiming <= 0:
                Additional.Story(5).blit(_display, clock, TargetFPS)
                keyInputTiming = 10

        if keyInputTiming > 0:
            keyInputTiming -= 1

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
    healthbar = pygame.image.load('healthbar.png')

    objTiming = 0
    atkTiming = 0
    movTiming = 0
    movDirection = 0
    attackGauge = 0

    # 3 tuples for each stage
    # (0: level, 1: enemy, 2: dmgGenTiming, 3: goldGenTiming, 4: objSpeed, 5: attackGauge, 6: redundancy)
    stages = ((1, Enemies.Enemy(100, 10, pygame.image.load('enemy1.png')), 25, 50, 8, 1.3, 20),
              (2, Enemies.Enemy(120,  8, pygame.image.load('enemy2.png')), 20, 45, 9, 1.5, 24),
              (3, Enemies.Enemy(150,  7, pygame.image.load('enemy3.png')), 15, 40, 10, 1.6, 28))
    level = 1

    Additional.Story(1).blit(_display, clock, TargetFPS)

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
            if movTiming <= 0:
                movDirection = -1
                player.turn(movDirection)
                movTiming = 5
        if _key[pygame.constants.K_RIGHT]:
            if movTiming <= 0:
                movDirection = 1
                player.turn(movDirection)
                movTiming = 5
        if _key[pygame.constants.K_SPACE]:
            if atkTiming <= 0:
                if player.shoot(tunnel.getLane(player.getLane()), stages[level-1][1]):
                    atkTiming = 8
                    attackGauge = max(attackGauge - 18, 0)
        if _key[pygame.constants.K_ESCAPE]:
            print 'return to title'
            return 0
        # ========================================================

        # Object State Update ====================================
        tunnel.propagate(player, movTiming)

        if objTiming % stages[level-1][2] == 0:
            # generate a new damage object
            tunnel.generateObj((1, dmgobj))
        if objTiming % stages[level-1][3] == 0:
            # generate a new gold object
            tunnel.generateObj((2, goldobj))
        objTiming += 1

        if player.checkGameOver():
            return 1

        if stages[level-1][1].defeat():
            level += 1
            Additional.Story(level).blit(_display, clock, TargetFPS)
            attackGauge = 0
            player.resetAmmo()
            if level >= 4:
                return 2
            tunnel.setSpeed(stages[level-1][4])
            tunnel.setRedundancy(stages[level-1][6])

        if atkTiming > 0:
            atkTiming -= 1
        if movTiming > 0:
            movTiming -= 1
        else:
            attackGauge += stages[level-1][5]
        if objTiming >= 120:
            objTiming = 0
        if attackGauge >= 100:
            player.damage()
            attackGauge = 0
        # ========================================================

        # Draw ===================================================
        _display.blit(bg, (0, 0))
        tunnel.blit(_display, player, movTiming * movDirection)

        _display.blit(healthbar, (0,0))
        player.blit(_display)
        stages[level - 1][1].blit(_display)
        pygame.draw.rect(_display, (255, 0, 0), (550, 300, int(180 * attackGauge / 100), 5))
        pygame.display.update()
        # ========================================================

        clock.tick(TargetFPS)


if __name__ == '__main__':
    main()
