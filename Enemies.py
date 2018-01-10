class Enemy(object):
    def __init__(self, HP, STAGE, APPEARANCE):
        self._hp = HP
        self._stage = STAGE
        self._appe = APPEARANCE

    def hit(self):
        print 'enemy hit'
        # reduce enemy's hp
        # TODO: Damage should be a variable
        self._hp -= 10

    def defeat(self):
        if self._hp <= 0:
            return True

    def blit(self, display):
        enemy_img_pos = self._appe.get_rect()
        enemy_img_pos.center = (640, 360)
        display.blit(self._appe, enemy_img_pos)