import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector
import math, random
from Room import Room
from Map import Map
from animation import MC
from animation import Keyboard
from animation import Interaction

mc_img = simplegui.load_image("https://i.imgur.com/hpehVFb.png")
mc_width = 128
mc_height = 128
mc_columns = 4
mc_rows = 4


WIDTH = 500
HEIGHT = 500
ROOMS = 2

#mapgen = Map(WIDTH, HEIGHT)
#mapgen.generate(30, 80, ROOMS)

class Keyboard(Keyboard):
    
    def disableKey(self, key):
        self.disabled_keys.append(key)
        print(self.disabled_keys)

    def enableKey(self, key):
        self.disabled_keys.pop(key)

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
bunny = MC(Vector(WIDTH/2, HEIGHT/2), mc_img, mc_width, mc_height, mc_columns, mc_rows)
kbd = Keyboard()
bunnyMove = Interaction(bunny, kbd)


# rooms
m = Map(200, 200, WIDTH, HEIGHT)
m.generate(10, 8, [WIDTH, HEIGHT])
rooms = m.getRooms()

current_room = rooms[0]

def draw(canvas):
    #global mapgen
    global bunny, bunnyMove, current_room, rooms
    collisions_handler = Collisions(bunny, current_room)
    current_room.draw(canvas)
    bunnyMove.update()
    collisions_handler.update()
    new_room = collisions_handler.getNewRoom()
    if(new_room != None):
        old_room = current_room
        current_room = new_room
        bunny.setPos( current_room.getNewRoomPos(old_room) )
    bunny.update()
    bunny.draw(canvas)
    

    

    



frame = simplegui.create_frame("Map Gen", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)

frame.start()