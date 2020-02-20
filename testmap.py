import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector
import math, random
from Room import Room
from Map import Map



WIDTH = 500
HEIGHT = 500
ROOMS = 2

#mapgen = Map(WIDTH, HEIGHT)
#mapgen.generate(30, 80, ROOMS)

class Ball:
    def __init__(self):
        self.pos = Vector( WIDTH/2, HEIGHT/2 )
        self.vel = Vector()
        self.radius = 15
        self.line_width = 1
        self.colour = "Blue"
    
    def draw(self, canvas):
        canvas.draw_circle(self.pos.get_p(), self.radius, self.line_width, self.colour, self.colour)

    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.85)

    def getPos(self):
        return(self.pos)

    def setPos(self, pos):
        self.pos = pos

    def getOffset(self):
        return(self.radius)

class Keyboard:

    def __init__(self):
        self.down = False
        self.up = False
        self.right = False
        self.left = False
        self.disabled_keys = []

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['down']:
            self.down = True
        elif key == simplegui.KEY_MAP['up']:
            self.up = True
        elif key == simplegui.KEY_MAP['right']:
            self.right = True
        elif key == simplegui.KEY_MAP['left']:
            self.left = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['down']:
            self.down = False
        elif key == simplegui.KEY_MAP['up']:
            self.up = False
        elif key == simplegui.KEY_MAP['right']:
            self.right = False
        elif key == simplegui.KEY_MAP['left']:
            self.left = False
    
    def disableKey(self, key):
        self.disabled_keys.append(key)

    def enableKey(self, key):
        self.disabled_keys.pop(key)

class Movement:

    def __init__(self, ball, keyboard):
        self.ball = ball
        self.keyboard = keyboard

    def update(self):
        if self.keyboard.up:
            self.ball.vel.add(Vector(0, -0.75))
        if self.keyboard.down:
            self.ball.vel.add(Vector(0, 0.75))
        if self.keyboard.right:
            self.ball.vel.add(Vector(0.75, 0))
        if self.keyboard.left:
            self.ball.vel.add(Vector(-0.75, 0))

class Collisions:
    def __init__(self, ball, room):
        self.__ball = ball
        self.__room = room
        self.__in_collision = False
        self.__new_room = None
    
    def update(self):
        door = self.__room.getCollidingDoor(self.__ball)
        if(door != None):
            self.__new_room = self.__room.getRoomFromDoor(door)
        if(self.__room.isCollidingWall(self.__ball)):
            if(not self.__in_collision):
                self.__ball.vel = self.__ball.vel.rotate(180)
                self.__in_collision = True
        else:
            self.__in_collision = False

    def getNewRoom(self):
        room = self.__new_room
        self.__new_room = None
        return(room)


# ball & int
ball = Ball()
kbd = Keyboard()
mvmt = Movement(ball, kbd)


# rooms
m = Map(200, 200, WIDTH, HEIGHT)
m.generate(10, 8, [WIDTH, HEIGHT])
rooms = m.getRooms()
r1 = Room(Vector(WIDTH/2, HEIGHT/2), 200, 200)
r2 = Room(Vector(WIDTH/2, HEIGHT/2), 300, 400)
r3 = Room(Vector(WIDTH/2, HEIGHT/2), 400, 300)
r1.addNeighbour(r2, "N")
r2.addNeighbour(r1, "S")
r1.addNeighbour(r3, "E")
r3.addNeighbour(r1, "W")

current_room = rooms[0]
print(current_room.getNeighbours())

def draw(canvas):
    #global mapgen
    global ball, mvmt, current_room, rooms
    collisions_handler = Collisions(ball, current_room)
    current_room.draw(canvas)
    mvmt.update()
    collisions_handler.update()
    new_room = collisions_handler.getNewRoom()
    if(new_room != None):
        old_room = current_room
        current_room = new_room
        ball.setPos( current_room.getNewRoomPos(old_room) )
    ball.update()
    ball.draw(canvas)
    

    

    



frame = simplegui.create_frame("Map Gen", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)

frame.start()