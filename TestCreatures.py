try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
try:
    from Vector import Vector
except ImportError:
    from user304_rsf8mD0BOQ_1 import Vector


#from map_gen import Room
from Creatures import *

WIDTH, HEIGHT = 400, 400

def draw(canvas):
    canvas.draw_polygon([(0,0),(WIDTH,0),(WIDTH,HEIGHT),(0,HEIGHT)], 5, "red")
    #room.draw(canvas)


#room = Room(350, 350, (WIDTH/2, HEIGHT/2))



player = Wizard(Vector(50,50))



frame = simplegui.create_frame("Test Creatures", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

frame.start()