import pygame
import GameOBJ
import Enemies


class Player(object):
    def __init__(self, HP, AMMO, APPEARANCE):
        self.hp = HP
        self.hpbar = pygame.image.load('playerhealth.png')
        self.ammo = AMMO
        self.appe = APPEARANCE
        self.lane = 0
        self.combo = 0

    def shoot(self, lane, enemy):
        if type(lane) is list and type(enemy) is Enemies.Enemy:
            if len(lane) == 0:
                enemy.hit()
            else:
                for l in lane:
                    if type(l) is GameOBJ.DamagePlatform:
                        # now, a damage platform can be destroyed
                        # without having a gold platform that blocks a player's attack
                        print 'dmgobj hit'
                        lane.remove(l)
                        return
                enemy.hit()

    def damage(self):
        self.combo = 0
        self.hp -= 40
        print 'player damaged, hp: %d' % (self.hp)

    def getgold(self):
        self.combo += 1
        if self.ammo < 10:
            self.ammo += 1
        self.hp += 10
        print 'player getting gold, hp: %d' % (self.hp)

    def blit(self, display):
        display.blit(self.appe, (550, 600))
        display.blit(self.hpbar, (200, 80))