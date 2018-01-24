import pygame
import GameOBJ
import Enemies


class Player(object):
    def __init__(self, HP, AMMO, APPEARANCE):
        self.__hp = HP
        self.__ammo = AMMO
        self.__appe = APPEARANCE
        self.__lane = 0
        self.__combo = 0

    def turn(self, dir):
        self.__lane = (self.__lane + dir) % 6

    def shoot(self, lane, enemy):
        if self.__ammo > 0:
            self.__ammo -= 1
            print "shoot it down! ammo: " + str(self.__ammo)
        else:
            print "no ammo"
            return False

        if type(lane) is list and type(enemy) is Enemies.Enemy:
            if len(lane) != 0:
                for l in lane:
                    if type(l) is GameOBJ.DamagePlatform:
                        print 'dmgobj hit'
                        lane.remove(l)
                        return True
            enemy.hit()
            return True

    def damage(self):
        self.__combo = 0
        if self.__hp >= 30:
            self.__hp -= 30
        else:
            self.__hp = 0
        print 'player damaged, hp: %d, combo: %d' % (self.__hp, self.__combo)

    def gold(self):
        self.__combo += 1
        if self.__ammo < 10:
            self.__ammo += 1

        if self.__hp <= 90:
            self.__hp += 10
        else:
            self.__hp = 100
        print 'player getting gold, hp: %d, combo: %d, ammo: %d' % (self.__hp, self.__combo, self.__ammo)

    def checkGameOver(self):
        if self.__hp <= 0:
            return True
        else:
            return False

    def getLane(self):
        return self.__lane

    def blit(self, display):
        player_img_pos = self.__appe.get_rect()
        player_img_pos.center = (640, 640)
        display.blit(self.__appe, player_img_pos)
        pygame.draw.rect(display, (0, 255, 0), (550, 600, int(180 * self.__ammo/10), 5))
        pygame.draw.rect(display, (255, 0, 0), (200, 640 - int(560 * self.__hp/100), 40, int(560 * self.__hp/100)))