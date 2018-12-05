class Tree:
    def __init__(self, sx, sy):
        self.height=0.1
        self.x=sx
        self.y=sy
        self.dead = False          # noch nicht tot
        self.age = 0
        self.decay=0
        self.flash = False          # default-Einstellung: kein Blitz eingeschlagen

    def info(self):
        return "%d, %d: age%d" % (self.x, self.y, self.age)

    def __repr__(self):
        return self.info()
