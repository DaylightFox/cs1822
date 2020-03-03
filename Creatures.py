try:
    from Vector import Vector
except ImportError:
    from user304_rsf8mD0BOQ_1 import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

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
        self.killed = False
        
    def draw(self, canvas):
        canvas.draw_image(self.sprite, self.center_source, self.width_height_source, self.pos.get_p(), self.width_height_dest)

    def take_damage(self, damage):
        self.currentHp -= damage
        if self.currentHp >= 0:
            self.killed = True

    def die(self):
        a=1#placeholder
        #run death animation
        #increase Player exp
    
        

class Player(Creature):
    def __init__(self, pos):
        playerRadius = 20
        sprite = 1#replace with default sprite
        super().__init__(pos, playerRadius, sprite)
        self.speed = 1
        self.exp = 0
        #replace with final values
        self.center_source = []
        self.width_height_source = [] 
        self.width_height_dest = []
        
        
        
class Wizard(Player):
    def __init__(self, pos):
        super().__init__(pos)
        sprite = 1#replace with wizard sprite
        
    def main_attack(self, mouse_pos):
        """
        Vector: mouse_pos 
        """
        mouse_pos = Vector(mouse_pos[0], mouse_pos[1])
        direction = (mouse_pos - self.pos).normalise
        distance = 1#replace with value (probably level scale)
        angle = 1
        attack = ConeAttack(self.pos, direction, distance, angle)




class Enemy(Creature):
    def __init__(self, radius, sprite, speed):
        sprite = 1#replace with default sprite
        super().__init__(pos, radius, sprite)
        self.speed = speed
        self.base_exp = 1
        

##    def take_damage(self, damage):
##        super().take_damage(damage)
##        if self.currentHp >= 0:
##            self.killed = True

    def die(self):
        super().die()
        #run death animation
        #increase Player exp
        
        
