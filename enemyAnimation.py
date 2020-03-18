import random
import math
from Vector import Vector
from Projectile import Projectile
from Projectile import EnemyProjectile
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

#Canvas dimensions
WIDTH = 500
HEIGHT = 500

class Enemy:

    def __init__(self, pos):
       
        #Movement vectors
        self.pos = pos
        self.baseBehav = [Vector(1,0), Vector(0,-1), Vector(-1, 0), Vector(0,1)]
        self.vel = Vector(0,0)

        #Counter for behaviour
        self.firespeed = 0
        self.baseCount = 0

        #List of attacks
        self.ListAttack = []

        #Spritesheet data
        self.spritesheet = simplegui._load_local_image('enemysprite.png')
        self.img_width = 128
        self.img_height = 128
        self.img_columns = 4
        self.img_rows = 4

        #Frame data
        self.frame_width = self.img_width / self.img_columns
        self.frame_height = self.img_height / self.img_rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2
        self.frame_index = [3,0]
        self.frame_duration = 10
        self.frameclock = 0

    def distFromPlayer(self, Player):
        playerPos = Player.pos.get_p()
        enPos = self.pos.get_p()
        direction = Vector(playerPos[0]-enPos[0], playerPos[1]-enPos[1])
        return direction

    def movement(self, Player):
        mvmt = self.distFromPlayer(Player)
        distance = mvmt.length()
        if (distance>=100):
            mvmt.normalize()
            mvmt.multiply(1.5)
            self.vel = mvmt
        if (distance<=90):
            mvmt = mvmt.normalize()
            mvmt = - mvmt.multiply(1.5)
            self.vel = mvmt
        if (distance<100 and distance>90):
            mvmt = mvmt.normalize()
            mvmt = mvmt.rotate_anti()
            mvmt = mvmt.multiply(1.5)
            self.vel = mvmt
        self.is_facing(Player)

    def is_facing(self, Player):
        direction = self.distFromPlayer(Player)
        distance = direction.length()
        angleTeta = direction.angle(Vector(1,0))
        if (distance>100):
            angleAlpha = self.vel.angle(Vector(1,0))
            if (angleAlpha>0.785 and angleAlpha<2.356) and (self.vel.y<=0):
                self.frame_index[0]=2
            if (angleAlpha>0.785  and angleAlpha<2.356) and (self.vel.y>=0):
                self.frame_index[0]=1
            if (angleAlpha<=0.785):
                self.frame_index[0]=3
            if (angleAlpha>=2.356):
                self.frame_index[0]=0
        else:
            angleTeta = direction.angle(Vector(1,0))
            if (angleTeta>0.785 and angleTeta<2.356) and (direction.y<=0):
                self.frame_index[0]=2
            if (angleTeta>0.785  and angleTeta<2.356) and (direction.y>=0):
                self.frame_index[0]=1
            if (angleTeta<=0.785):
                self.frame_index[0]=3
            if (angleTeta>=2.356):
                self.frame_index[0]=0

    def shooting(self, Player):
        self.firespeed += 1
        direction = self.distFromPlayer(Player)
        distance = direction.length()
        if (distance<170):
            if (self.firespeed%20==0):

                direction.normalize()
                offset = direction.copy()
                direction.multiply(4)
                aim = self.pos.copy().add(offset.multiply(15))

                if (Player.pos.y>self.pos.y):
                    angle = -direction.angle(Vector(-1, 0))
                else:
                    angle = (direction.angle(Vector(-1, 0)))
                fireball = EnemyProjectile(aim, direction, angle)
                self.ListAttack.append(fireball)
    
    def drawshooting(self, canvas):
        remove = []
        for i in self.ListAttack:
            if (i.pos.x<WIDTH) or (i.pos.x>0) or (i.pos.y<HEIGHT) or (i.pos.y>0): #CHANGE FOR REAL CONDITIONS!
                i.drawprojectile(canvas)
                i.update()
            else:
                remove.append(i)
        for i in remove:
            self.Attack.remove(i)

    def update_frameindex(self):
        self.frame_index[1] = (self.frame_index[1] + 1) % self.img_rows
    
    def draw(self, canvas):
        self.frameclock += 1
        if (self.frameclock % self.frame_duration == 0):
            self.update_frameindex()
        
        frame_centre = (self.frame_width * self.frame_index[0] + self.frame_centre_x, self.frame_height * self.frame_index[1] + self.frame_centre_y)
        frame_size = (self.frame_width, self.frame_height)
        canvas.draw_image(self.spritesheet, frame_centre, frame_size, self.pos.get_p(), frame_size)
    
    def update(self, Player):
        self.pos.add(self.vel)
        self.vel.multiply(0.75)
        self.shooting(Player)

    def enemyDraw(self, canvas, Player):
        self.movement(Player)
        self.update(Player)
        self.draw(canvas)
        self.drawshooting(canvas)

        