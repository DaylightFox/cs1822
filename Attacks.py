try:
    from Vector import Vector
except ImportError:
    from user304_rsf8mD0BOQ_1 import Vector

class Attack:
    def __init__(self, damage, pos):
        self.damage = damage
        self.pos = pos
        self.sprite = 1  #replace with place holder

    def deal_damage(self.creature):
        creature.take_damage(self.damage)