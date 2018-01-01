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
        self.combo = 0
        self.hp -= 40
        print 'player damaged, hp: %d' % (self.hp)

    def getgold(self):
        self.combo += 1
        if self.ammo < 10:
            self.ammo += 1
        self.hp += 10
        print 'player getting gold, hp: %d' % (self.hp)

    def blit(self, display):
        display.blit(self.appe, (550, 600))
