import math
import pygame


class GameOBJ(object):
    def __init__(self, LANE, APPEARANCE):
        self.lane = LANE
        self.pos = 0
        self.appe = APPEARANCE

    def judge(self):
        if self.pos >= 300:
            return True
        else:
            return False

    def forward(self, speedPerFrame):
        self.pos += speedPerFrame

    def blit(self, display, player):
        # scaled = pygame.transform.rotozoom(self.appe, 0, self.pos/300)
        # getting position using center
        scaledpos = self.appe.get_rect()
        scaledpos.center = (640, 360)
        # calculates relative direction
        # math.sin() and math.cos() use radian angle values
        reladir = math.radians(60 * ((self.lane - player.lane) % 6))
        display.blit(self.appe, (scaledpos[0] + int(math.sin(reladir) * self.pos), scaledpos[1] + int(math.cos(reladir) * self.pos)))


class DamagePlatform(GameOBJ):
    def __init__(self, LANE, APPEARANCE):
        super(DamagePlatform, self).__init__(LANE, APPEARANCE)

    def judge(self):
        pass

    def hit(self):
        pass


class GoldPlatform(GameOBJ):
    def __init__(self, LANE, APPEARANCE):
        super(GoldPlatform, self).__init__(LANE, APPEARANCE)

    def judge(self):
        pass
