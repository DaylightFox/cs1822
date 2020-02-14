try:
    from Vector import Vector
except ImportError:
    from user304_rsf8mD0BOQ_1 import Vector

class Creature:
    def __init__(self, pos, radius, sprite):
        self.pos = pos #centre of sprite
        self.radius = radius
        self.sprite = sprite
        self.center_source = []
        self.width_height_source = [] 
        self.width_height_dest = []
        self.speed = 0
        self.level = 1
        self.maxHpBase = 1
        self.maxHpMultiplier = 1
        self.currentHp = 1
        self.DmgBase = 1
        
    def draw(self, canvas):
        canvas.draw_image(self.sprite, self.center_source, self.width_height_source, self.pos, self.width_height_dest)

    def take_damage(self, damage):
        self.currentHp -= damage
        
    
        

class Player(Creature):
    def __init__(self, pos):
        playerRadius = 20
        sprite = 1#replace with default sprite
        super().__init__(pos, playerRadius, sprite)
        self.speed = 1
        
        
        
        
class Wizard(Player):
    def __init__(self, pos):
        super().__init__(pos)
        
    def main_attack(self, mouse_pos):
        """
        Vector: mouse_pos 
        """
        direction = (mouse_pos - self.pos).normalise
        attack = ConeAttack(self.pos, direction)




class Enemy(Creature):
    def __init__(self, radius, sprite, speed):
        sprite = 1#replace with default sprite
        super().__init__(pos, radius, sprite)
        self.speed = speed

    def take_damage(self, damage):
        super().take_damage(damage)
        if self.currentHp >= 0:
            self.killed()

    def killed(self):
        a=1#placeholder
        #run death animation or delete
        
        
