from Vector import Vector
from Projectile import Projectile
from Room import Room
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

#Canvas dimensions
WIDTH = 500
HEIGHT = 500

class MC:

    def __init__(self, pos):
       
        #Movement
        self.pos = pos
        self.speed = 0.75
        self.vel = Vector()

        #Attacks parameters
        self.firespeed = 0
        self.ListAttack = []

        #Spritesheet data
        self.spritesheet = simplegui._load_local_image('mcsprite.png')
        self.img_width = 128
        self.img_height = 128
        self.img_columns = 4
        self.img_rows = 4

        #Frame data
        self.frame_width = self.img_width / self.img_columns
        self.frame_height = self.img_height / self.img_rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2
        self.frame_index = [1,0]
        self.frame_duration = 10
        self.frameclock = 0

    def getPos(self):
        return self.pos
    
    def setPos(self, pos):
        self.pos = pos
    
    def pauseMove(self, room):
        '''
        Takes a room object room.
        Keeps Sprite within the room by:
            -Pausing the movement if the sprite touches the walls
        '''
        wall_left = room.getCenter().x - room.getWidth()/2
        wall_right = room.getCenter().x + room.getWidth()/2

        wall_up = room.getCenter().y - room.getHeight()/2
        wall_down = room.getCenter().y + room.getHeight()/2

        if (self.pos.x <= wall_left):
            self.pos.x = wall_left
            print(self.pos.x)
            
        if (self.pos.x >=  wall_right):
            self.pos.x = wall_right
            print(self.pos.x)

        if (self.pos.y <= wall_up):
            self.pos.y = wall_up
        if (self.pos.y >= wall_down):
            self.pos.y = wall_down
    
    
    def distFromMouse(self, mouse):
        mousepos = mouse.pos
        currpos = self.pos.get_p()
        direction = Vector(mousepos[0]-currpos[0], mousepos[1]-currpos[1])
        return direction
    
    def movement(self, keyboard, mouse):
        if mouse.is_newpos():
            direction = self.distFromMouse(mouse)
            angleAlpha = direction.angle(Vector(1,0))
            if (angleAlpha>0.785 and angleAlpha<2.356) and (mouse.pos[1]<=self.pos.y):
                self.frame_index[0]=2
            if (angleAlpha>0.785  and angleAlpha<2.356) and (mouse.pos[1]>=self.pos.y):
                self.frame_index[0]=1
            if (angleAlpha<=0.785):
                self.frame_index[0]=3
            if (angleAlpha>=2.356):
                self.frame_index[0]=0
            self.shooting(mouse)
            mouse.save_lastpos()

            if keyboard.up:
                self.vel.add(Vector(0, -0.75))
            if keyboard.down:
                self.vel.add(Vector(0, 0.75))
            if keyboard.right:
                self.vel.add(Vector(0.75, 0))
            if keyboard.left:
                self.vel.add(Vector(-0.75, 0))
        
         #Input based movement + Sprite looking toward the direction the object is going
        else:
            if keyboard.up:
                self.vel.add(Vector(0, -0.75))
                self.frame_index[0]=2
            if keyboard.down:
                self.vel.add(Vector(0, 0.75))
                self.frame_index[0]=1
            if keyboard.right:
                self.vel.add(Vector(0.75, 0))
                self.frame_index[0]=3
            if keyboard.left:
                self.vel.add(Vector(-0.75, 0))
                self.frame_index[0]=0
    
    def shooting(self, mouse):
        self.firespeed += 1
        if mouse.is_newpos():
            if (self.firespeed%8==0): #Firespeed
                direction = self.distFromMouse(mouse)
                direction.normalize()
                offset = direction.copy()
                direction.multiply(5)
                currpos = self.pos.copy().add(offset.multiply(15))

                if (mouse.pos[1]>currpos.y):
                    angle = -direction.angle(Vector(-1, 0))
                else:
                    angle = (direction.angle(Vector(-1, 0)))
                fireball = Projectile(currpos, direction, angle)
                self.ListAttack.append(fireball)
        mouse.save_lastpos()

    def drawshooting(self, canvas): #Need to add real conditions + add wall/ennemy as argument
        remove = []
        for i in self.ListAttack:
            if (i.pos.x<WIDTH) or (i.pos.x>0) or (i.pos.y<HEIGHT) or (i.pos.y>0):
                i.drawprojectile(canvas)
                i.update()
            else:
                remove.append(i)
        for i in remove:
            self.ListAttack.remove(i)

    def update_frameindex(self):
        self.frame_index[1] = (self.frame_index[1] + 1) % self.img_rows
    
    def draw(self, canvas):
        self.frameclock += 1
        if (self.frameclock % self.frame_duration == 0):
            self.update_frameindex()
        
        frame_centre = (self.frame_width * self.frame_index[0] + self.frame_centre_x, self.frame_height * self.frame_index[1] + self.frame_centre_y)
        frame_size = (self.frame_width, self.frame_height)
        canvas.draw_image(self.spritesheet, frame_centre, frame_size, self.pos.get_p(), frame_size)
    
    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(self.speed)
    
    def playerDraw(self, canvas, mouse, keyboard):
        self.movement(keyboard, mouse)
        self.update()
        self.draw(canvas)
        self.drawshooting(canvas)

class Interaction:

    def __init__(self, MC, keyboard, mouse):
        self.MC = MC
        self.keyboard = keyboard
        self.mouse = mouse

    def MCdraw(self, canvas):
        self.MC.playerDraw(canvas, self.mouse, self.keyboard)

    def MCdrag(self, position):
        self.mouse.drag(position)
    
    def MCclick(self, position):
        self.mouse.click(position)
    
    def MCkeyD(self, key):
        self.keyboard.keyDown(key)
    
    def MCkeyU(self, key):
        self.keyboard.keyUp(key)
