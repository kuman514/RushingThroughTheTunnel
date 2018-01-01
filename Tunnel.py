import pygame

class Tunnel(object):
    def __init__(self, APPEARANCE):
        self.rotation = 0
        self.appe = APPEARANCE
        # self.lanes = [list(), list(), list(), list(), list(), list()]

    def generateObj(self):
        pass

    def blit(self, display, player):
        tunnel_rot = pygame.transform.rotate(self.appe, -60 * player.lane)
        tunnel_image_pos = tunnel_rot.get_rect()
        tunnel_image_pos.center = (640, 360)
        display.blit(tunnel_rot, tunnel_image_pos)
