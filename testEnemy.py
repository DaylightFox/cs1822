from Vector import Vector
from Projectile import*
from playerAnimation import*
from enemyAnimation import Enemy
from Keyboard import Keyboard
from Mouse import Mouse
from PlayerGameInter import PlayerGameInter
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

#Canvas dimensions
WIDTH = 500
HEIGHT = 500

#Create objects from different classes
deadb = Enemy(Vector(WIDTH/2, HEIGHT/2))
LE = [deadb]
bunny = MC(Vector(50,50))
kbd = Keyboard()
mouse = Mouse(bunny.pos.get_p())
inter = Interaction(bunny, kbd, mouse)
PGI = PlayerGameInter(bunny, LE)

def drag_handler(position):
    inter.MCdrag(position)

def click_handler(position):
    inter.MCclick(position)

def keyDown_handler(key):
    inter.MCkeyD(key)

def keyUp_handler(key):
    inter.MCkeyU(key)

def draw(canvas):
    inter.MCdraw(canvas)
    for i in LE:
        i.enemyDraw(canvas, bunny)
    PGI.drawfight(canvas)


# Create a frame and call events
frame = simplegui.create_frame("Rabbit on Acid", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keyDown_handler)
frame.set_keyup_handler(keyUp_handler)
frame.set_mousedrag_handler(drag_handler)
frame.set_mouseclick_handler(click_handler)
frame.start()