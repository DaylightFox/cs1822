try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


from Vector import*
from animation import*

import random


WIDTH = 300
HEIGHT = 500

numProjectiles = 4

def randCol ():
    r = random.randrange (0, 256)
    g = random.randrange (0, 256)
    b = random.randrange (0, 256)
    return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'

def ranPos ():
    x = random.randint(10,WIDTH)
    y = -10
    return Vector(x,y)

class Projectiles:
    def __init__(self, pos): # all projectiles are the same except for where on the CANVAS WIDTH they spawn
        self.pos = pos
        self.radius = 10
        self.vel = Vector(0, 2)
        self.colour = 'red'
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

class Interaction:
    def __init__(self, sprite, projectiles):
        self.sprite = sprite
        self.projectiles = projectiles
        self.numProjectiles = numProjectiles #constant


    def draw(self, canvas):
        global i
        
        if i < len(self.projectiles):
            self.projectiles[i].draw(canvas)
            self.projectiles[i].update()

            if self.projectiles[i].pos.y >= HEIGHT + 30:
                print(self.projectiles)
                i+= 1
                #self.projectiles.remove(self.projectiles[i])
                #print("Prev Ball: " + str(i - 1))
                #print("Current ball: " + str(i))
                #print("List Length: " + str (len(self.projectiles)))
                
        
        #else:
            #when i is more than number of projectiles
            #maybe call end game sequence?

i=0
ProjectilesList = [Projectiles(ranPos()) for i in range(numProjectiles) ]
spriteCollide = Interaction(bunny,ProjectilesList) #sprite and projectile interaction definition




frame = simplegui.create_frame("Collisions Corridor", WIDTH, HEIGHT)
frame.set_draw_handler(spriteCollide.draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()