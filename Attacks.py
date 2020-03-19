try:
    from Vector import Vector
except ImportError:
    from user304_rsf8mD0BOQ_1 import Vector

class Attack:
    def __init__(self, pos, damage, direction):
        self.damage = damage
        self.pos = pos
        self.direction = direction
        self.sprite = 1  #replace with
        self.colour = "white"#to be used if there is no sprite
        self.center_source = []
        self.width_height_source = [] 
        self.width_height_dest = []

    def deal_damage(self, creature):
        creature.take_damage(self.damage)
        
    def draw(self, canvas, rotation=0):
        canvas.draw_image(self.sprite, self.center_source, self.width_height_source, self.pos.get_p(), self.width_height_dest, rotation)

class ConeAttack(Attack):
    def __init__(self, damage, pos, direction, distance, angle):
        super().__init__(damage, pos, direction)
        self.distance = distance
        self.angle = angle
        #self.launch()
    
    def hit_creature(self, creature):
        difference = creature.pos - self.pos
        if difference.length() <= self.distance:
            angle = self.direction.angle(difference.get_normalized())
            if angle <= self.angle:
                return True
            
            edge = self.direction.copy().rotate(self.angle) * difference.length()
            if (edge - creature.pos).length() <= creature.radius:
                return True
            
            edge.rotate(self.angle * -2)
            #return (edge - creature.pos).length() <= creature.radius
            if (edge - creature.pos).length() <= creature.radius:
                return True
            
        return False
    
    def draw(self,canvas):
        if self.colour != 1:
            super().draw(canvas)
        else:
            p1 = self.pos.get_p()
            p2 = (self.direction.copy().rotate(self.angle) * difference.length()).get_p()
            p3 = (self.direction.copy() * difference.length()
            canvas.draw()).get_p()
            p4 = (self.direction.copy().rotate(self.angle * -2) * difference.length()).get_p()
            
            canvas.draw_polygon([p1,p2,p3,p4], 1, self.colour, self.colour)

class ProjectileAttack(Attack):
    def __init__(self, pos, direction, radius, speed):
        super().__init__(damage, pos, direction)
        self.radius = radius
        self.trail = 1#length of the trail(texture) behind the projectile
        self.speed = speed
        #self.launch()
    
    def hit_creature(self, creature):
        difference = creature.pos - self.pos
        return difference.length <= (self.radius + creature.radius)
            #angle = self.direction.angle(difference.get_normalized())
            #if angle <= self.angle:
                #return True
        #return False
        
    def hit_room(self, room):
        return(self.pos.x >= room.top_right.x) or (self.pos.x <= room.top_left.x) or (self.pos.y <= room.top_right.y) or (self.pos.y >= room.bot_right.y )
            
    def draw(self,canvas):
        if self.colour != 1:
            super().draw(canvas)
        else:
            canvas.draw_circle(self.pos.get_p(), self.radius, 1, self.colour)

class FlameBreath(ConeAttack):
    def __init__(self, damage, pos, direction, distance):
        angle = 45
        super().__init__(damage, pos, direction, distance, angle)
        self.sprite = 1#replace with sprite
    
    def next_frame():
        a=1#add code for frame transition
