from Vector import Vector
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Attack:
    def __init__(self, damage):
        self.damage = damage

    def deal_damage(self, creature):
        creature.take_damage(self.damage)
        

class Melee(Attack):
    def __init__(self, damage):
        super().__init__(damage)
        

class Projectile(Attack):
    def __init__(self, damage, pos, vel, angle):
        super().__init__(damage)
        self.pos = pos
        self.vel = vel
        self.angle = angle

        # Sprite date
        self.spritesheet = simplegui.load_image("https://i.imgur.com/T8BwM8E.png")
        self.img_width = 840
        self.img_height = 54
        self.img_columns = 10
        self.img_rows = 6

        # Fram data
        self.frame_width = self.img_width / self.img_columns
        self.frame_height = self.img_height / self.img_rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2
        self.frame_index = [1,0]
        self.frame_duration = 2
        self.frameclock = 0
        self.radius = self.frame_width/2

    def update_frameindex(self):
        self.frame_index[0] = (self.frame_index[0] + 1) % self.img_columns
        if self.frame_index[0] == 0:
            self.frame_index[1] = (self.frame_index[1] + 1) % self.img_rows

    def draw(self, canvas):
        self.frameclock += 1
        if (self.frameclock % self.frame_duration == 0):
            self.update_frameindex()
        
        frame_centre = (self.frame_width * self.frame_index[0] + self.frame_centre_x, self.frame_height * self.frame_index[1] + self.frame_centre_y)
        frame_size = (self.frame_width, self.frame_height)
        canvas.draw_image(self.spritesheet, frame_centre, frame_size, self.pos.get_p(), frame_size, self.angle)

    def getPos(self):
        return(self.pos)

    def isCollidingCreature(self, creature):
        difference = creature.pos - self.pos
        distance = difference.length()
        return distance <= (self.radius + creature.radius)

    def isCollidingWall(self, room):
        return(room.isCollidingWall(self))

    def update(self):
        self.pos.add(self.vel)
        #self.vel.multiply(0.85)

class EnemyProjectile(Projectile):
    def __init__(self, pos, vel, angle):
        self.damage = 7
        super().__init__(self.damage, pos, vel, angle)
        self.spritesheet = simplegui.load_image("https://i.imgur.com/DYGyWeB.png")

class ConeAttack(Attack):
    def __init__(self, pos, damage, direction, distance, angle):
        super().__init__(damage, pos, direction)
        self.distance = distance
        self.angle = angle
        self.done = True
        #self.launch()
    
    def hit_creature(self, creature):
        difference = creature.pos - self.pos
        if difference.length() <= self.distance:
            angle = self.direction.angle(difference.get_normalized())
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
            p2 = (self.direction.copy().rotate_rad(self.angle) * self.distance).get_p()
            p3 = (self.direction.copy().rotate_rad(self.angle * 0.5) * self.distance).get_p()
            p4 = (self.direction.copy() * self.distance).get_p()
            p5 = (self.direction.copy().rotate_rad(self.angle * -0.5) * self.distance).get_p()
            p6 = (self.direction.copy().rotate_rad(self.angle * -1) * self.distance).get_p()
            
            canvas.draw_polygon([p1,p2,p3,p4,p5,p6], 1, self.colour, self.colour)
            
    def update(self):
        self.done = not self.done

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
        distance = 15#subject to change
        super().__init__(pos, damage, direction, distance, angle)
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
        super().__init__(pos, damage, direction, distance, angle)
        self.colour = "white"
    
class IceBreath(ConeAttack):
    def __init__(self, pos, damage, direction):
        angle = 0.6
        distance = 20#subject to change
        super().__init__(pos, damage, direction, distance, angle)
        self.colour = "aqua"
