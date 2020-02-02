#Beginning of Character movement: using circle instead of character sprite
#borders?

try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH = 1000
HEIGHT = 800
position = [WIDTH/2, HEIGHT/2]
move = [0,0]
radius = 10
velocity = 3

"""class Char:
    def __init__:
        self.health = 200
        self.damage = 5 ->base damage

    def regenerate(self, amt):
        self.health +=amt
    
    def sprite(self):
        **
"""

def keydown(key):
    global velocity, move
    if key == simplegui.KEY_MAP['s']:
        move[1] += velocity        
    elif key == simplegui.KEY_MAP['w']:
        move[1] -= velocity
    elif key == simplegui.KEY_MAP['a']:
        move[0] -= velocity
    elif key == simplegui.KEY_MAP['d']:
        move[0] += velocity 

def keyup(key):  
    global move
    if key == simplegui.KEY_MAP['s']:
        move[1] = 0
    elif key == simplegui.KEY_MAP['w']:
        move[1] = 0
    elif key == simplegui.KEY_MAP['d']:
        move[0] = 0
    elif key == simplegui.KEY_MAP['a']:
        move[0] = 0 

def draw(canvas):
    global position, velocity

    canvas.draw_circle(position, radius, 1, "aqua", "aqua")
   # canvas.draw_circle()

    position[0] += move[0]
    position[1] += move[1]



frame = simplegui.create_frame("Character move", WIDTH, HEIGHT)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

frame.start()