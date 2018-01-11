import pygame

class Enemy(object):
    def __init__(self, HP, DAMAGE, APPEARANCE):
        self.__hp = HP
        self.__maxHP = HP
        self.__damage = DAMAGE
        self.__appe = APPEARANCE

    def hit(self):
        print 'enemy hit'
        # reduce enemy's hp
        self.__hp -= self.__damage

    def defeat(self):
        if self.__hp <= 0:
            return True

    def blit(self, display):
        enemy_img_pos = self.__appe.get_rect()
        enemy_img_pos.center = (640, 360)
        display.blit(self.__appe, enemy_img_pos)
        pygame.draw.rect(display, (0, 0, 255), (1041, 640 - int(560 * self.__hp / self.__maxHP), 40, int(560 * self.__hp / self.__maxHP)))