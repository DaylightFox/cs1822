from Attacks import *

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
        self.levelScaleMultplier = 1
        self.maxHpBase = 1
        self.maxHp = 1
        self.currentHp = 1
        self.Dmg = 1
        self.DmgBase = 1
        self.killed = False
        
    def getPos(self):
        return(self.pos)

    def setPos(self, pos):
        self.pos = pos
        
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

    def setLevel(self, level):
        self.level = level
        self.maxHp = int(self.maxHpBase * (
        self.levelScaleMultplier ** level))
        self.currentHp = self.maxHp
        self.Dmg = int(self.DmgBase * (self.levelScaleMultplier ** level))
        
    def levelUp(self):
        self.setLevel(self.level + 1)
    
        

class Player(Creature):
    def __init__(self, pos):
        playerRadius = 16
        sprite = 1#replace with default sprite
        super().__init__(pos, playerRadius, sprite)
        self.width_height_dest = [self.radius*2,self.radius*2]
        self.speed = 1
        self.levelScaleMultplier = 1.09
        self.exp = 0
        self.expTargetBase = 500
        self.expTarget = self.expTargetBase
        self.maxHpBase = 300
        self.maxHp = self.maxHpBase
        self.currentHp = self.maxHp
        self.DmgBase = 10
        self.Dmg = self.DmgBase

    def die(self):
        print("Death!!!!!!!")
        
    def needLevelUp(self):
        return self.exp >= self.expTarget
    
    def setLevel(self, level):
        super().setLevel(level)
        self.exp = 0
        self.expTarget = int(self.expTargetBase * (self.levelScaleMultplier ** level))
        
class Wizard(Player):
    def __init__(self, pos):
        super().__init__(pos)
        self.sprite = 1#replace with wizard sprite
        
    def main_attack(self, mouse_pos):
        mouse_pos = Vector(mouse_pos[0], mouse_pos[1])
        direction = (mouse_pos - self.pos).normalise
        distance = 1#replace with value (probably level scale)
        angle = 1
        offset = 1
        source = self.pos + ((self.radius + offset) * direction)
        attack = ConeAttack(self.pos, direction, distance, angle)
        return attack




class Enemy(Creature):
    def __init__(self, pos, radius, sprite, speed, ideal_range):
        sprite = 1#replace with default sprite
        super().__init__(pos, radius, sprite)
        self.speed = speed
        self.base_exp = 1
        self.ideal_range = ideal_range#replace with 3/4 main attack range
        

##    def take_damage(self, damage):
##        super().take_damage(damage)
##        if self.currentHp >= 0:
##            self.killed = True

    def die(self):
        super().die()
        #run death animation
        #increase Player exp

class Goblin(Enemy):
    def __init__(self, pos):
        radius = 1#will be small
        sprite = 1#replace with sprite
        speed = 3#will be fast
        ideal_range = 1
        super().__init__(pos, radius, sprite, speed, ideal_range)

class DaggerGoblin(Goblin):
    def __init__(self, pos):
        super().__init__(pos)
        self.ideal_range = 7#approx

    def main_attack(self, player_pos):
        direction = (player_pos - self.pos).normalise
        distance = 1#short #replace with value (probably level scale)
        angle = 135#wide
        offset = 1
        source = self.pos + ((self.radius + offset) * direction)
        attack = ConeAttack(self.pos, direction, distance, angle)
        return attack

class Dragon(Enemy):
    def __init__(self, pos):
        radius = 10#will be large
        sprite = 1#replace with sprite
        speed = 3#will be slow
        ideal_range = 1
        super().__init__(pos, radius, sprite, speed, ideal_range)

    def main_attack(self, player_pos):
        direction = (player_pos - self.pos).normalise
        distance = 20#short #replace with value (probably level scale)
        angle = 15#wide
        offset = 1
        source = self.pos + ((self.radius + offset) * direction)
        attack = ConeAttack(self.pos, direction, distance, angle)
        return attack
        
