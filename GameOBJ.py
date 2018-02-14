import math
import pygame


class GameOBJ(object):
    def __init__(self, LANE, APPEARANCE):
        self._lane = LANE
        self._pos = 0
        self._appe = APPEARANCE
        self._activateJudge = True

    def judge(self):
        if self._pos >= 280 and self._activateJudge:
            self._activateJudge = False
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

    def getPos(self):
        return self._pos

    def getLane(self):
        return self._lane

    def getJudgeable(self):
        return self._activateJudge


class DamagePlatform(GameOBJ):
    def __init__(self, LANE, APPEARANCE):
        super(DamagePlatform, self).__init__(LANE, APPEARANCE)

    def judge(self, player, mov):
        if super(DamagePlatform, self).judge() and self._lane == player.getLane() and mov > 0:
            player.damage()


class GoldPlatform(GameOBJ):
    def __init__(self, LANE, APPEARANCE):
        super(GoldPlatform, self).__init__(LANE, APPEARANCE)

    def judge(self, player, mov):
        if super(GoldPlatform, self).judge() and self._lane == player.getLane() and mov > 0:
            player.gold()