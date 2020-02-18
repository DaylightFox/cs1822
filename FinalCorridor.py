try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Vector import*
from animation import*

import random


WIDTH = 300
HEIGHT = 700

def randCol ():
    r = random.randrange (0, 256)
    g = random.randrange (0, 256)
    b = random.randrange (0, 256)
    return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'

class Projectiles:
    def __init__(self, pos, colour): #initialized all projectiles to be the same
        self.pos = pos
        self.radius = 10
        self.vel = Vector(0, 2)
        self.colour = colour
        self.border = 1
    
    def update(self):
        self.pos.add(self.vel)

    def draw(self,canvas):
        canvas.draw_circle(self.pos.get_p(), 
                           self.radius,
                           self.border,
                           self.colour,
                           self.colour)


ProjectilesList = []

def makeProjectiles():
    global ProjectilesList
    fire = Projectiles()

    for i in range(1,6):
        n = random.randint(10,290)
        colour = randCol()
        fire = Projectiles(n, colour)
        ProjectilesList.append(fire)


def draw(canvas):
    makeProjectiles()

    

    #inter.update()
    #bunny.update()
    #bunny.draw(canvas)

frame = simplegui.create_frame("Collisions Corridor", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()