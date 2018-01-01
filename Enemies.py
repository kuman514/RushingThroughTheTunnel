class Enemy(object):
    def __init__(self, HP, STAGE, APPEARANCE):
        self.hp = HP
        self.stage = STAGE
        self.appe = APPEARANCE

    def hit(self):
        pass

    def defeat(self):
        pass

    def blit(self, display):
        enemy_img_pos = self.appe.get_rect()
        enemy_img_pos.center = (640, 360)
        display.blit(self.appe, enemy_img_pos)