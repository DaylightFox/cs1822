try:
    from Vector import Vector
except ImportError:
    from user304_rsf8mD0BOQ_1 import Vector
import math

class Attack:
    def __init__(self, pos, damage, direction):
        self.pos = pos
        self.damage = damage
        self.direction = direction
        self.sprite = 1  #replace with
        self.colour = "white"#to be used if there is no sprite
        self.center_source = []
        self.width_height_source = [] 
        self.width_height_dest = []
        self.done = False

    def deal_damage(self, creature):
        creature.take_damage(self.damage)
        
    def draw(self, canvas, rotation=0):
        canvas.draw_image(self.sprite, self.center_source, self.width_height_source, self.pos.get_p(), self.width_height_dest, rotation)

class ConeAttack(Attack):
    def __init__(self, pos, damage, direction, distance, angle, duration):
        super().__init__(pos, damage, direction)
        self.distance = distance
        self.angle = angle
        self.done = False
        self.duration = duration
        self.frame_count = 0
        #self.launch()
    
    def hit_creature(self, creature):
        difference = creature.pos - self.pos
        if difference.length() <= self.distance:
            cosAngle = self.direction.dot(difference) / (self.direction.length() * difference.length())
            if abs(cosAngle)>1:
                cosAngle = 1
            angle = math.acos(cosAngle)
            #angle = self.direction.angle(difference.get_normalized())
            if angle <= self.angle:
                return True
            
            edge = self.direction.copy().rotate_rad(self.angle) * difference.length()
            if (edge - creature.pos).length() <= creature.radius:
                return True
            
            edge.rotate_rad(self.angle * -2)
            #return (edge - creature.pos).length() <= creature.radius
            if (edge - creature.pos).length() <= creature.radius:
                return True
            
        return False
    
    def draw(self,canvas):
        if self.sprite != 1:
            super().draw(canvas)
        else:
            p1 = self.pos.get_p()
            p2 = (self.pos + self.direction.copy().rotate_rad(self.angle) * self.distance).get_p()
            p3 = (self.pos + self.direction.copy().rotate_rad(self.angle * 0.5) * self.distance).get_p()
            p4 = (self.pos + self.direction.copy() * self.distance).get_p()
            p5 = (self.pos + self.direction.copy().rotate_rad(self.angle * -0.5) * self.distance).get_p()
            p6 = (self.pos + self.direction.copy().rotate_rad(self.angle * -1) * self.distance).get_p()
            
            canvas.draw_polygon([p1,p2,p3,p4,p5,p6], 1, self.colour, self.colour)
            
    def update(self):
        self.frame_count = (self.frame_count+1) % self.duration
        if self.frame_count == 0:
            self.done = True
        #self.done = not self.done

class ProjectileAttack(Attack):
    def __init__(self, pos, damage, direction, radius, speed):
        super().__init__(pos, damage, direction)
        self.radius = radius
        self.trail = 1#length of the trail(texture) behind the projectile
        self.speed = speed
        #self.launch()
    
    def hit_creature(self, creature):
        difference = creature.pos - self.pos
        return difference.length() <= (self.radius + creature.radius)
            #angle = self.direction.angle(difference.get_normalized())
            #if angle <= self.angle:
                #return True
        #return False
        
    def hit_room(self, room):
        #print("East:",(self.pos.x >= room.getCenter().x + room.getWidth()/2))
        #print("West:",(self.pos.x <= room.getCenter().x - room.getWidth()/2))
        #print("North:",(self.pos.y <= room.getCenter().y - room.getHeight()/2))
        #print("South:",(self.pos.y >= room.getCenter().y + room.getHeight()/2))
        #print((self.pos.x >= room.getCenter().x + room.getWidth()/2) or (self.pos.x <= room.getCenter().x - room.getWidth()/2) or (self.pos.y <= room.getCenter().y - room.getHeight()/2) or (self.pos.y >= room.getCenter().y + room.getHeight()/2))
        return (self.pos.x >= room.getCenter().x + room.getWidth()/2) or (self.pos.x <= room.getCenter().x - room.getWidth()/2) or (self.pos.y <= room.getCenter().y - room.getHeight()/2) or (self.pos.y >= room.getCenter().y + room.getHeight()/2)
            
    def draw(self,canvas):
        if self.sprite != 1:
            super().draw(canvas)
        else:
            canvas.draw_circle(self.pos.get_p(), self.radius, 1, self.colour, self.colour)
            
    def update(self):
        self.pos += self.direction * self.speed

class BurningHands(ConeAttack):
    def __init__(self, pos, damage, direction):
        angle = 0.5
        distance = 50#subject to change
        duration = 20
        super().__init__(pos, damage, direction, distance, angle, duration)
        self.colour = "red"
    
    def next_frame():
        a=1#add code for frame transition

class FireBolt(ProjectileAttack):
    def __init__(self, pos, damage, direction):
        radius = 5
        speed = 5
        super().__init__(pos, damage, direction, radius, speed)
        self.colour = "red"
        
class SwordSlash(ConeAttack):
    def __init__(self, pos, damage, direction):
        angle = 2/3 * math.pi
        distance = 5#subject to change
        duration = 30
        super().__init__(pos, damage, direction, distance, angle, duration)
        self.colour = "white"
    
class IceBreath(ConeAttack):
    def __init__(self, pos, damage, direction):
        angle = 0.6
        distance = 20#subject to change
        duration = 60
        super().__init__(pos, damage, direction, distance, angle, duration)
        self.colour = "aqua"
