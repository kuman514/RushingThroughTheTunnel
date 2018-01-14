import math
import pygame

class GameOBJ(object):
    def __init__(self, LANE, APPEARANCE):
        self._lane = LANE
        self._pos = 0
        self._appe = APPEARANCE

    def judge(self):
        if self._pos >= 280:
            return True
        else:
            return False

    def forward(self, speedPerFrame):
        self._pos += speedPerFrame

    def blit(self, display, player, mov):
        reladir = math.radians(60 * ((self._lane - player.getLane()) % 6) + (12 * mov))

        scale = int(120*(self._pos/280.0))
        scaled = pygame.transform.scale(self._appe, (scale,  scale))
        scaledpos = scaled.get_rect()
        scaledpos.center = (640, 360)
        display.blit(scaled, (scaledpos[0] + int(math.sin(reladir) * self._pos), scaledpos[1] + int(math.cos(reladir) * self._pos)))

        #scaledpos = self._appe.get_rect()
        #scaledpos.center = (640, 360)
        #display.blit(self._appe, (scaledpos[0] + int(math.sin(reladir) * self._pos), scaledpos[1] + int(math.cos(reladir) * self._pos)))

    def getPos(self):
        return self._pos

    def getLane(self):
        return self._lane


class DamagePlatform(GameOBJ):
    def __init__(self, LANE, APPEARANCE):
        super(DamagePlatform, self).__init__(LANE, APPEARANCE)

    def judge(self, player):
        if super(DamagePlatform, self).judge() and self._lane == player.getLane():
            player.damage()


class GoldPlatform(GameOBJ):
    def __init__(self, LANE, APPEARANCE):
        super(GoldPlatform, self).__init__(LANE, APPEARANCE)

    def judge(self, player):
        if super(GoldPlatform, self).judge() and self._lane == player.getLane():
            player.gold()