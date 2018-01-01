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
        # combo = 0
        # HP -= dmg amount
        print 'player damaged'

    def getgold(self):
        # combo += 1
        # if ammo < 10:
        #   ammo += 1
        # HP += rst amount
        print 'player getting gold'

    def blit(self, display):
        display.blit(self.appe, (550, 600))
