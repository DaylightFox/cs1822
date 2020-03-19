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

WIDTH = 500
HEIGHT = 500

def ranPos(xLimit, yLimit):
    x = random.randint(xLimit[0],xLimit[1])
    y = random.randint(yLimit[0],yLimit[1])
    return Vector(x,y)

def randVel():
    x = random.randint(-3, 3)
    y = random.randint(-3, 3)
    return( Vector(x, y) )


def randCol ():
    r = random.randrange (0, 256)
    g = random.randrange (0, 256)
    b = random.randrange (0, 256)
    return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'

class Projectiles:
    def __init__(self, pos, vel, colour): # all projectiles are the same except for where on the CANVAS WIDTH they spawn
        self.pos = pos
        self.radius = 10
        self.vel = vel
        self.colour = colour
        self.border = 1
        self.numProjectiles = 10
        self.in_collision = False

    def bounce(self, normal):
        self.vel.reflect(normal)

    def walls(self, room):
        wall_left = room.getCenter().x - room.getWidth()/2
        wall_right = room.getCenter().x + room.getWidth()/2

        if (self.pos.x - self.radius <= wall_left) or (self.pos.x + self.radius >= wall_right):
            self.bounce(Vector(1,0))
            self.in_collision = True
        else:
            self.in_collision = False

    def isHittingWalls(self):
        return (self.in_collision)

    def update(self):
        self.pos.add(self.vel)

    def draw(self,canvas):
        canvas.draw_circle(self.pos.get_p(), 
                           self.radius,
                           self.border,
                           self.colour,
                           self.colour)
      
    def getNext(self, pList):
        for projectile in pList:
            if (projectile.isHittingWalls()):
                projectile.walls(self.__room)

class Collisions:
    def __init__(self, corridor, sprite, projectiles):
        self.__corridor = corridor
        self.__sprite = sprite
        self.__projectiles = projectiles
        self.__nextCorridor = None
        self.__in_collision = False

    def update(self):
        door = self.__corridor.getCollidingDoor(self.__sprite)
        #self.__projectiles.walls(self.__corridor)
             
        if(door != None):
            self.__nextRoom = self.__corridor.getRoomFromDoor(door)
             
        if (self.__sprite.pos == self.__projectlies):
            print("I have no clue")

        if(self.__corridor.isCollidingWall(self.__sprite)):
            if(not self.__in_collision):
                self.__sprite.pauseMove(self.__corridor)
                self.__in_collision = True
        else:
            self.__in_collision = False

    def getNextCorridor(self):
        corridor = self.__nextCorridor
        self.__nextCorridor = None
        return(corridor)

class Corridor(Room):
    def __init__(self, center, width, height, type='none', projectileTypes = 'none'):
        super().__init__(center, width, height, type=type)
        self.projectiles = []
        self.numProjectiles =10
        self.counter = 0

    def resetProjectileCounter(self):
        self.counter = 0
    
    def incCounter(self):
        self.counter +=1
  
    def generateProjectiles(self, kind):
        '''
        returns a list of projectiles given a type: random, vertical, horizontal, diagonal
        Uses ranPos() to generate varied projectiles
        Random = random colours
        horizontal = RED
        vertical = BLUE
        diagonal = GREEN
        '''
        corridor_left = (WIDTH/2) - 101
        corridor_right = (WIDTH/2) + 101

        corridor_top = 0
        corridor_bottom = HEIGHT

        plist = []
        if (kind == "random"):
            plist = [Projectiles(ranPos([corridor_left,corridor_right], 
                                        [corridor_top, corridor_bottom]), 
                                        randVel(), 
                                        randCol()) for i in range(self.numProjectiles)]
            
        if (kind == "vertical"):
            plist = [Projectiles(ranPos([corridor_left, corridor_right], 
                                        [-100, -10]), 
                                        randVel(), 
                                        "blue")  for i in range(self.numProjectiles)]
            
        if (kind == "horizontal"):
            vel = randVel()
            x = random.randint(corridor_left, corridor_right)
            y = random.randint(corridor_top, corridor_bottom)
            plist = [Projectiles(Vector(x,y), 
                    vel, 
                    "red" ) for i in range(int(self.numProjectiles/2))]
            
        if (kind == "diagonal"):
            plist = [Projectiles(ranPos(), randVel(), "red" ) for i in range(self.numProjectiles)]

        else:
            self.projectiles = []

        self.projectiles = plist


    def drawProjectiles(self, canvas):
    
        if (self.counter < len(self.projectiles)):
            self.projectiles[self.counter].draw(canvas)
            self.projectiles[self.counter].update()
            if (self.projectiles[self.counter].pos.y >= HEIGHT):
                self.incCounter()

            if (len(self.projectiles) == self.counter):
                self.resetProjectileCounter()

        '''

        #Corridor Info
        self.canvas_width = 500
        self.room_width = 200
        self.height = 500


        self.bunny = MC(Vector(self.canvas_width/2, self.height - 100))
        self.__kbd = Keyboard()
        self.__mouse = Mouse(self.bunny.getPos())
        self.spriteInter = Interaction(self.bunny, self.__kbd, self.__mouse)
        self.steps = 0

        self.counter = 0
 
        
        Room1 has vertical projectiles 
        Room2 has projectiles(vertical and horizontal?) shooting from the top
        
        self.room1 = Room(Vector(self.canvas_width/2,self.height/2), self.room_width, self.height)
        self.room2 = Room(Vector(self.canvas_width/2, self.height/2), self.room_width, self.height)
        self.current_room = self.room1
        
        self.current_projectiles = Projectile(Vector(), Vector(), "white")

        
    def linkRooms(self):
        self.room1.addNeighbour(self.room2, "N")
        self.room2.addNeighbour(self.room1, "S")

    
    
    

    
    def disappearingProjectiles room
    def bouncing room
    def reset:
        if (self.bunny.isDead):
            resetstep counter
            call corridor here again
    '''
        

        

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