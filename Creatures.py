from Attacks import *
import math

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
        self.width_height_dest = [self.radius*2, self.radius*2]
        self.speed = 0
        self.direction = Vector(0,0)#unit vector or (0,0)
        self.attackList = []
        self.level = 1
        self.levelScaleMultplier = 1
        self.exp = 0
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
    
    def create_attack(self, target_pos, attackClass):
        target_pos = Vector(target_pos[0], target_pos[1])
        direction = (target_pos - self.pos).normalize()
        offset = 1
        source = self.pos + ((self.radius + offset) * direction)
        attack = attackClass(source, self.Dmg, direction)
        return attack

    def update(self):
        self.pos += self.direction * self.speed

class Player(Creature):
    def __init__(self, pos):
        playerRadius = 23
        sprite = 1#replace with default sprite
        super().__init__(pos, playerRadius, sprite)
        self.width_height_dest = [self.radius*2,self.radius*2]
        self.speed = 2
        self.levelScaleMultplier = 1.09
        self.exp = 0
        self.expTargetBase = 500
        self.expTarget = self.expTargetBase
        self.maxHpBase = 300
        self.maxHp = self.maxHpBase
        self.currentHp = self.maxHp
        self.DmgBase = 10
        self.Dmg = self.DmgBase
        self.altAttacking = False
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def die(self):
        print("Death!!!!!!!")
        
    def needLevelUp(self):
        return self.exp >= self.expTarget
    
    def setLevel(self, level):
        super().setLevel(level)
        self.exp = 0
        self.expTarget = int(self.expTargetBase * (self.levelScaleMultplier ** level))
    
    def increaseExp(self, x):
        self.exp += x
    
    def update(self):
        super().update()
        if self.needLevelUp():
            self.levelUp()
    
    def moveD(self, key):
        if key in [87,83,65,68]:
            if key == 87:#w
                self.up = True
            elif key == 83:#s
                self.down = True
            elif key == 65:#a
                self.left = True
            elif key == 68:#d
                self.right = True
            self.setDirection()
        elif key == 32:#space
            self.altAttacking = True
    
    def moveU(self, key):
        if key in [87,83,65,68]:
            if key == 87:#w
                self.up = False
            elif key == 83:#s
                self.down = False
            elif key == 65:#a
                self.left = False
            elif key == 68:#d
                self.right = False
        elif key == 32:#space
            self.altAttacking = False
        self.setDirection()
        
    def setDirection(self):
        self.direction = Vector(0,0)
        if self.up and (not self.down):
            self.direction.add(Vector(0,-1))
        if self.down and (not self.up):
            self.direction.add(Vector(0,1))
        if self.left and (not self.right):
            self.direction.add(Vector(-1,0))
        if self.right and (not self.left):
            self.direction.add(Vector(1,0))
        if self.direction.length() > 0:
            self.direction.normalize()
            
    def pauseMove(self, room):
        wall_left = (room.getCenter().x - room.getWidth()/2)
        wall_right = room.getCenter().x + room.getWidth()/2
        wall_up = room.getCenter().y - room.getHeight()/2
        wall_down = room.getCenter().y + room.getHeight()/2

        if (self.pos.x - self.radius <= wall_left):
            self.pos.x = wall_left
        elif (self.pos.x + self.radius >= wall_right):
            self.pos.x = wall_right
        
        if (self.pos.y - self.radius <= wall_up):
            self.pos.y = wall_up
        elif (self.pos.y + self.radius >= wall_down):
            self.pos.y = wall_down
        
class Wizard(Player):
    def __init__(self, pos):
        super().__init__(pos)
        self.sprite = simplegui._load_local_image('assets/mcsprite.png')
        self.center_source = [23,23]
        self.width_height_source = [46,46]
        self.frame_count = 0
        self.frame_delay_count = 0
        self.frame_delay = 4
        
    def draw(self, canvas):
        if self.direction.x < 0:#left
            self.center_source[0] = 23
        elif self.direction.x > 0:#right
            self.center_source[0] = 161
        elif self.direction.y > 0:#down
            self.center_source[0] = 69
        elif self.direction.y < 0:#up
            self.center_source[0] = 115
        else:
            self.center_source[0] = 69 #default looking down
        self.center_source[1] = 46*self.frame_count + 23
        super().draw(canvas)
        
    def update(self):
        if (self.up or self.down or self.left or self.right):
            self.frame_delay_count = (self.frame_delay_count+1) % self.frame_delay
            if not(self.frame_delay_count):
                self.frame_count = (self.frame_count+1) % 4
        super().update()

    def main_attack(self, mouse_pos):
        attack = self.create_attack(mouse_pos, FireBolt)
        #mouse_pos = Vector(mouse_pos[0], mouse_pos[1])
        #direction = (mouse_pos - self.pos).normalize
        #offset = 1
        #source = self.pos + ((self.radius + offset) * direction)
        #attack = FireBolt(source, self.Dmg, direction)
        self.attackList.append(attack)
    
    def alt_attack(self, mouse_pos):
        #if self.direction.length():
            #target_pos = (self.direction + self.pos).get_p()
        #else:
            #target_pos = (Vector(0,1) + self.pos).get_p()
        attack = self.create_attack(mouse_pos, BurningHands)
        #mouse_pos = Vector(mouse_pos[0], mouse_pos[1])
        #direction = (mouse_pos - self.pos).normalize
        #offset = 1
        #source = self.pos + ((self.radius + offset) * direction)
        #attack = BurningHands(source, self.Dmg, direction)
        self.attackList.append(attack)




class Enemy(Creature):
    def __init__(self, pos, radius, sprite, speed, base_exp, level, ideal_range):
        sprite = 1#replace with default sprite
        super().__init__(pos, radius, sprite)
        self.speed = speed
        self.base_exp = base_exp
        self.setLevel(level)
        self.ideal_range = ideal_range#replace with 3/4 main attack range

    def setLevel(self, level):
        super().setLevel(level)
        expModifier = 1.08
        self.exp = self.base_exp * (expModifier**self.level)

    def die(self):
        super().die()
        #run death animation
        #increase Player exp
        
    def setDirection(self, player):
        self.direction = (player.pos - self.pos).normalize()
        
    def update(self, player):
        self.setDirection(player)
        distance = (player.pos - self.pos).length()
        ideal_range = self.ideal_range
        if ideal_range[0] <= distance <= ideal_range[0]:
            self.main_attack(player.pos.get_p())
        elif ideal_range[0] > distance:
            self.direction.rotate_rad(math.pi)
        else:
            self.pos += self.direction * self.speed

class Goblin(Enemy):
    def __init__(self, pos, level):
        radius = 20#will be small
        sprite = 1#replace with sprite
        speed = 3#will be fast
        base_exp = 5
        ideal_range = 1
        super().__init__(pos, radius, sprite, speed, base_exp, level, ideal_range)

class DaggerGoblin(Goblin):
    def __init__(self, pos, level):
        super().__init__(pos, level)
        self.ideal_range = [0.5,4]#approx
        self.hit = False

    def main_attack(self_pos):
        attack = self.create_attack(player.pos, SwordSlash)
        self.attackList.append(attack)
    
    def update(self, player):
        if not self.hit:
            super().update(player)
            #ideal_range = self.ideal_range
            #if ideal_range[0] <= distance <= ideal_range[0]:
                #self.main_attack(player.pos.get_p())
                #self.hit = True
            #elif ideal_range[0] > distance:
                #self.direction.rotate(math.pi)
                #self.pos += self.direction * self.speed
            #else:
                #self.pos += self.direction * self.speed
        else:
            self.setDirection(player)
            distance = (player.pos - self.pos).length()
            safeDistance = 100
            if distance >= safeDistance:
                self.hit = False
            else:
                self.direction.rotate_rad(math.pi)
            self.pos += self.direction * self.speed
            
    def draw(self, canvas):
        if self.sprite==1:
            canvas.draw_circle(self.pos.get_p(), self.radius, 1, "Gray", "Green")
        else:
            super().draw(canvas)

class Dragon(Enemy):
    def __init__(self, pos, level):
        radius = 10#will be large
        sprite = 1#replace with sprite
        speed = 3#will be slow
        base_exp = 7
        ideal_range = [5,17]
        super().__init__(pos, radius, sprite, speed, base_exp, level, ideal_range)

    def main_attack(self, player_pos):
        attack = self.create_attack(player.pos, IceBreath)
        self.attackList.append(attack)
        
    def draw(self, canvas):
        if self.sprite==1:
            canvas.draw_circle(self.pos.get_p(), self.radius, 1, "CadetBlue", "CadetBlue")
        else:
            super().draw(canvas)
