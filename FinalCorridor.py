try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


from Vector import*
from animation import MC
from animation import Keyboard
from animation import Interaction

import random


WIDTH = 200
HEIGHT = 500
numProjectiles = 5

mc_img = simplegui.load_image("https://i.imgur.com/hpehVFb.png")
mc_width = 128
mc_height = 128
mc_columns = 4
mc_rows = 4

def ranPos ():
    x = random.randint(10,WIDTH)
    y = -10
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

class Projectiles:
    def __init__(self, pos, vel, colour): # all projectiles are the same except for where on the CANVAS WIDTH they spawn
        self.pos = pos
        self.radius = 10
        self.vel = vel
        self.colour = colour
        self.border = 1

    def bounce(self, normal):
        self.vel.reflect(normal)

    def walls(self):
        if(self.pos.x <= 0):
            self.bounce( Vector(1, 0) )
        elif(self.pos.x >= WIDTH):
            self.bounce( Vector(1, 0))
    
    def update(self):
        self.walls()
        self.pos.add(self.vel)

    def draw(self,canvas):
        canvas.draw_circle(self.pos.get_p(), 
                           self.radius,
                           self.border,
                           self.colour,
                           self.colour)

class SpriteProjectileInteraction:
    def __init__(self, sprite, projectVertical, projectDiagonal):
        self.bunny = sprite
        self.projectVertical = projectVertical
        self.projectDiagonal = projectDiagonal
        self.numProjectiles = numProjectiles #constant


    def draw(self, canvas):
        global i, bunnyMove
        
        if i < len(self.projectVertical):
            self.projectVertical[i].draw(canvas)
            self.projectVertical[i].update()

            if self.projectVertical[i].pos.y >= HEIGHT + 30:
                print(self.projectVertical)
                i+= 1
                #self.projectiles.remove(self.projectiles[i])
                #print("Prev Ball: " + str(i - 1))
                #print("Current ball: " + str(i))
                #print("List Length: " + str (len(self.projectiles)))

        bunnyMove.update()
        self.bunny.update()
        self.bunny.draw(canvas)        
        
        #else:
            #when i is more than number of projectiles
            #maybe call end game sequence?

i= j = 0
VProjectilesList = [Projectiles(ranPos(), Vector(0,5), "red" ) for i in range(numProjectiles) ]
DProjectilesList = [Projectiles(ranPos(), Vector(3,5), "blue") for j in range(numProjectiles)]

bunny = MC(Vector(WIDTH/2, HEIGHT - 100), mc_img, mc_width, mc_height, mc_columns, mc_rows)
kbd = Keyboard()
bunnyMove = Interaction(bunny, kbd)

spriteCollide = SpriteProjectileInteraction(bunny,VProjectilesList, DProjectilesList) #sprite, vertical and diagonal projectiles interaction definition




frame = simplegui.create_frame("Collisions Corridor", WIDTH, HEIGHT)
frame.set_draw_handler(spriteCollide.draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)

frame.start()