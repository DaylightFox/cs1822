import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector
import math, random
from Room import Room
from Map import Map
from playerAnimation import*
from Keyboard import Keyboard
from Mouse import Mouse

WIDTH = 500
HEIGHT = 500
ROOMS = 10
RANDOM_ROOMS = 0.4

#mapgen = Map(WIDTH, HEIGHT)
#mapgen.generate(30, 80, ROOMS)
'''
class Keyboard(Keyboard): #Who did this??
    
    def disableKey(self, key):
        self.disabled_keys.append(key)
        print(self.disabled_keys)

    def enableKey(self, key):
        self.disabled_keys.pop(key)
'''
class Collisions:
    def __init__(self, sprite, room):
        self.__sprite = sprite
        self.__room = room
        self.__in_collision = False
        self.__new_room = None
        self.__new_map = False

    def update(self):
        door = self.__room.getCollidingDoor(self.__sprite)
        if(door != None):
            self.__new_room = self.__room.getRoomFromDoor(door)
        if(self.__room.isEnd()):
            if(self.__room.isCollidingLevelDoor(self.__sprite)):
                self.__new_map = True
        if(self.__room.isCollidingWall(self.__sprite)):
            if(not self.__in_collision):
                self.__sprite.vel = self.__sprite.vel.rotate(180)
                self.__in_collision = True
        else:
            self.__in_collision = False

    def getNewRoom(self):
        room = self.__new_room
        self.__new_room = None
        return(room)

    def doGenerateNewMap(self):
        new = self.__new_map
        self.__new_map = False
        return(new)


#Sprite
bunny = MC(Vector(WIDTH/2, HEIGHT/2))
kbd = Keyboard()
mouse = Mouse(bunny.pos.get_p())
spriteInter = Interaction(bunny, kbd, mouse)

# rooms
m = Map(256, 256, WIDTH, HEIGHT)
m.generate(ROOMS, RANDOM_ROOMS, [WIDTH, HEIGHT])
rooms = m.getRooms()

current_room = rooms[0]

def draw(canvas):
    #global mapgen
    global bunny, spriteInter, current_room, rooms, mouse
    collisions_handler = Collisions(bunny, current_room)
    current_room.draw(canvas)
    spriteInter.MCdraw(canvas)
    collisions_handler.update()
    new_room = collisions_handler.getNewRoom()

    if(new_room != None):
        old_room = current_room
        current_room = new_room
        bunny.setPos( current_room.getNewRoomPos(old_room) )
    if(collisions_handler.doGenerateNewMap()):
        m.generate(ROOMS, RANDOM_ROOMS, [WIDTH, HEIGHT])
        current_room = m.getRooms()[0]
   
    #bunny.update()
    
    

    

    



frame = simplegui.create_frame("TestMap2", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(spriteInter.keyboard.keyDown)
frame.set_canvas_background( "rgb(28, 17, 23)" )
frame.set_keyup_handler(spriteInter.keyboard.keyUp)

frame.set_mousedrag_handler(spriteInter.MCdrag)
frame.set_mouseclick_handler(spriteInter.MCclick)

frame.start()