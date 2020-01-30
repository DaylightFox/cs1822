class Creature:
    def __init__(self, pos, radius):
        self.pos = pos #centre of sprite
        self.radius = radius
        self.speed = 0




class Player(Creature):
    def __init__(self, pos):
        playerRadius = 20
        super().__init__(pos, playerRadius)
        
