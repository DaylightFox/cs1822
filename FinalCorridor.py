try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


from Vector import*
from playerAnimation import*
from Keyboard import Keyboard
from Mouse import Mouse
from Room import Room
import random
from testMap2 import Collisions
#import character death??


def ranPos ():
    x = random.randint(10,WIDTH)
    y = random.randint(100, HEIGHT+ 100)
    return Vector(x,y)
'''
def randVel():
    x = random.randint(-5, 5)
    y = random.randint(-5, 5)
    return( Vector(x, y) )

def randCol ():
    r = random.randrange (0, 256)
    g = random.randrange (0, 256)
    b = random.randrange (0, 256)
    return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'
'''

class Bunny(MC):
    def __init__(self, pos):
        super().__init__(pos)
        self.inCorridor = True
        self.size = 5  #5 pixels to account for sprite width

    #Checks that the sprite is within the Corridor
    def isInCorridor(self, width):
        self.centre = width/2
        if not (self.pos.x >= centre + 100) or (self.pos.x <= centre - 100):
            self.isInCorridor = False
        return self.inCorridor
    '''
    def hitWalls(self, width):
        #self.
        if (self.pos.x <= self.size):
            self.pos.x = self.size
        if (self.pos.x >= WIDTH- self.size):
            self.pos.x = WIDTH - self.size
    '''

class Projectiles:
    def __init__(self, pos, vel, colour): # all projectiles are the same except for where on the CANVAS WIDTH they spawn
        self.pos = pos
        self.radius = 10
        self.vel = vel
        self.colour = colour
        self.border = 1
        self.__numProjectiles = 10
        self.__centre = 0

    def bounce(self, normal):
        self.vel.reflect(normal)

    def hitWalls(self, width):
        self.__centre = width/2
        if(self.pos.x <= self.__centre + 100):
            self.bounce(Vector(1, 0))
        elif(self.pos.x >=  self.__centre - 100):
            self.bounce(Vector(1, 0))
    
    def update(self):
        self.walls()
        self.pos.add(self.vel)

    def generateProjectiles(self):
        '''
        returns a list of projectiles with random velocities
        '''
        plist = [Projectiles(ranPos(), ranPos(), "red" ) for i in range(self.numProjectiles)]
        return plist

    def draw(self,canvas):
        canvas.draw_circle(self.pos.get_p(), 
                           self.radius,
                           self.border,
                           self.colour,
                           self.colour)

class Corridor:
    def __init__(self):

        #Corridor Info
        self.canvas_width = 500
        self.room_width = 200
        self.height = 500


        self.bunny = MC(Vector(self.canvas_width/2, self.height - 100))
        self.__kbd = Keyboard()
        self.__mouse = Mouse(self.bunny.getPos())
        self.spriteInter = Interaction(self.bunny, self.__kbd, self.__mouse)
        self.steps = 0
 
        '''
        Room1 has vertical projectiles 
        Room2 has projectiles(vertical and horizontal?) shooting from the top
        '''
        self.room1 = Room(Vector(self.canvas_width/2,self.height/2), self.room_width, self.height)
        self.room2 = Room(Vector(self.canvas_width/2, self.height/2), self.room_width, self.height)
        
        
        #self.projectVertical = [Projectiles(ranPos(), Vector(0,5), "red" ) for i in range(self.numProjectiles)]

    def stepCount(self):
        self.step +=1

    def stepReset(self):
        self.step = 0
    
    '''
    def disappearingProjectiles room

    def bouncing room

    def reset:
        if (self.bunny.isDead):
            resetstep counter
            call corridor here again

    '''       

    def main(self, canvas):

        self.room1.draw(canvas)
        self.spriteInter.MCdraw(canvas)

        #self.spriteInter.MC.walls(self.room_width)

        

        #collisions = Collisions(self.spriteInter.MC, self.room1)
        #collisions.update()

    '''
    #room.draw(canvas)
    def update(self, canvas):
        global i, j, inter
        #self.bunny.walls(WIDTH) #keeps sprite insidse hopefully
        
        if i < len(self.projectVertical):
            self.projectVertical[i].draw(canvas)
            self.projectVertical[i].update()
            #if (self.hit(self.sprite, self.projectVertical[i])):
                #collide handle method
            if (self.projectVertical[i].pos.y >= HEIGHT):
                i+= 1


        if j <len(self.projectDiagonal):
            self.projectDiagonal[j].draw(canvas)
            self.projectDiagonal[j].update()

            if (self.projectDiagonal[j].pos.y >= HEIGHT):
                j+= 1;
        self.room.draw(canvas)
        '''

