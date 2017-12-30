class GameOBJ:
    def __init__(self, LANE, APPEARANCE):
        self.lane = LANE
        self.pos = 0
        self.appe = APPEARANCE

    def judge(self):
        pass


class DamagePlatform(GameOBJ):
    def __init__(self, LANE):
        super(DamagePlatform, self).__init__(LANE)

    def hit(self):
        pass

    def judge(self):
        pass


class GoldPlatform(GameOBJ):
    def __init__(self, LANE):
        super(GoldPlatform, self).__init__(LANE)

    def judge(self):
        pass
