try:
    from Vector import Vector
except ImportError:
    from user304_rsf8mD0BOQ_1 import Vector

class Attack:
    def __init__(self, pos, damage):
        self.damage = damage
        self.pos = pos
        self.sprite = 1  #replace with place holder
        self.duration = 60 #frames on screen

    def deal_damage(self.creature):
        creature.take_damage(self.damage)

class ConeAttack(Attack):
    def __init__(self, pos, direction, distance, angle):
        super().__init__(damage, pos)
        self.direction = direction
        self.distance = distance
        self.angle = angle
        #self.launch()
    
    def hit_creature(self, creature):
        difference = creature.pos - self.pos
        if difference.length <= self.distance:
            angle = self.direction.angle(difference.get_normalized())
            if angle <= self.angle:
                return True
        return False

class ProjectileAttack(Attack):
    def __init__(self, pos, direction, radius):
        super().__init__(damage, pos)
        self.direction = direction
        self.radius = radius
        #self.launch()
    
    def hit_creature(self, creature):
        difference = creature.pos - self.pos
        return difference.length <= (self.radius + creature.radius):
            #angle = self.direction.angle(difference.get_normalized())
            #if angle <= self.angle:
                #return True
        #return False
