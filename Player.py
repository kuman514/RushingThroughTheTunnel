class Player(object):
    def __init__(self, HP, AMMO, APPEARANCE):
        self.hp = HP
        self.ammo = AMMO
        self.appe = APPEARANCE
        self.lane = 0
        self.combo = 0

    def shoot(self):
        pass

    def damage(self):
        print 'player damaged'

    def getgold(self):
        print 'player getting gold'

    def blit(self, display):
        display.blit(self.appe, (550, 600))
