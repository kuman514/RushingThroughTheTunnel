import pygame
import random
import time
import GameOBJ


class Tunnel(object):
    def __init__(self, APPEARANCE):
        self.__appe = APPEARANCE
        self.__lanes = [list(), list(), list(), list(), list(), list()]
        random.seed(time.time())

    def generateObj(self, type):
        num = random.randint(0, 5)
        if len(self.__lanes[num]) != 0:
            while self.__lanes[num][-1].getPos() <= 20:
                num = random.randint(0, 5)
                if len(self.__lanes[num]) == 0:
                    break

        if type[0] == 1:
            newobj = GameOBJ.DamagePlatform(num, type[1])
        elif type[0] == 2:
            newobj = GameOBJ.GoldPlatform(num, type[1])
        self.__lanes[num].append(newobj)

    def removeObj(self, lane, obj):
        self.__lanes[lane].remove(obj)

    def propagate(self, player):
        for l in self.__lanes:
            for o in l:
                o.forward(5)
                o.judge(player)
                if o.getPos() >= 300:
                    self.removeObj(o.getLane(), o)

    def getLane(self, curRotation):
        return self.__lanes[curRotation]

    def blit(self, display, player):
        tunnel_rot = pygame.transform.rotate(self.__appe, -60 * player.getLane())
        tunnel_image_pos = tunnel_rot.get_rect()
        tunnel_image_pos.center = (640, 360)
        display.blit(tunnel_rot, tunnel_image_pos)

        for l in self.__lanes:
            for o in l:
                o.blit(display, player)
