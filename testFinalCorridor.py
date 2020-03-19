from FinalCorridor import*
from Vector import*
from animationV4 import*
#from testMap2 import Collisions
from Room import Room


#Canvas dimensions
WIDTH = 500
HEIGHT = 500

#projectile Info
#DProjectilesList = [Projectiles(ranPos().add(Vector(0, -50)), Vector(3,5), "blue") for j in range(numProjectiles)]


#Animations

bunny = MC(Vector(WIDTH/2, HEIGHT - HEIGHT/4))
kbd = Keyboard()
mouse = Mouse(bunny.pos.get_p())
spriteInter = Interaction(bunny, kbd, mouse)

#Corridor Instance
start = True
stage1 = Corridor(Vector(WIDTH/2,HEIGHT/2), 200, WIDTH, "N")
stage2 = Corridor(Vector(WIDTH/2,HEIGHT/2), 200, WIDTH, "S")

stage1.addNeighbour(stage2, "N")
stage2.addNeighbour(stage1, "S")



stage1.generateProjectiles("vertical")
if (stage1.projectiles != None):
    print(stage1.projectiles)
stage2.generateProjectiles("horizontal")

def drawCorridor(canvas):
    global start, stage1, stage2, spriteInter
    collisions = Collisions(stage1, spriteInter.MC, stage1.projectiles)
    collisions.update()
    if (start):
        stage1.draw(canvas)
        stage1.drawProjectiles(canvas)
    

    
    spriteInter.MCdraw(canvas)

frame = simplegui.create_frame("Final Corridor", WIDTH, HEIGHT)
frame.set_draw_handler(drawCorridor)
frame.set_keydown_handler(spriteInter.keyboard.keyDown)
frame.set_keyup_handler(spriteInter.keyboard.keyUp)

frame.start()