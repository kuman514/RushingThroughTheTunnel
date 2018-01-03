import pygame
import random
import time
import GameOBJ


class Tunnel(object):
    def __init__(self, APPEARANCE):
        self.rotation = 0
        self.appe = APPEARANCE
        self.lanes = [list(), list(), list(), list(), list(), list()]
        random.seed(time.time())

    def generateObj(self, type):
        num = random.randint(0, 5)
        if len(self.lanes[num]) != 0:
            while self.lanes[num][-1].pos >= 20:
                num = random.randint(0, 5)
                if len(self.lanes[num]) == 0:
                    break

        if type[0] == 1:
            newobj = GameOBJ.DamagePlatform(num, type[1])
        elif type[0] == 2:
            newobj = GameOBJ.GoldPlatform(num, type[1])
        self.lanes[num].append(newobj)

    def removeObj(self, lane, obj):
        self.lanes[lane].remove(obj)

    def blit(self, display, player):
        tunnel_rot = pygame.transform.rotate(self.appe, -60 * player.lane)
        tunnel_image_pos = tunnel_rot.get_rect()
        tunnel_image_pos.center = (640, 360)
        display.blit(tunnel_rot, tunnel_image_pos)
