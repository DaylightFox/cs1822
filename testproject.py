from Vector import Vector
from Projectile import Projectile
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Mouse:

    def __init__(self, pos):
        self.pos = pos
        self.last_pos = pos

    def drag(self, position):
        self.pos = position
    
    def click(self, position):
        self.pos = position
    
    def save_lastpos(self):
        self.last_pos = self.pos
    
    def is_newpos(self):
        return(self.last_pos != self.pos)

class Interaction:

    def __init__(self, mouse):
        self.mouse = mouse
        self.ListProject = []
        self.ClearList = []
    
    def shooting(self):
        if self.mouse.is_newpos():
            mousepos = self.mouse.pos
            currpos = (WIDTH/2, HEIGHT/2)
            currposV = Vector(WIDTH/2, HEIGHT/2)
            direction = Vector((mousepos[0]-currpos[0]), (mousepos[1]-currpos[1]))
            direction.normalize()
            direction.multiply(2.5)
            if (mousepos[1]>currpos[1]):
                angle = -direction.angle(Vector(-1, 0))
            else:
                angle = (direction.angle(Vector(-1, 0)))
            fireball = Projectile(currposV, direction, angle)
            self.ListProject.append(fireball)
            self.mouse.save_lastpos()
    
    def MCdrag(self, position):
        self.mouse.drag(position)
    
    def MCclick(self, position):
        self.mouse.click(position)

WIDTH = 500
HEIGHT = 500

mouse = Mouse((WIDTH/2, HEIGHT/2))
inter = Interaction(mouse)

def draw_handler(canvas):
    inter.shooting()
    if len(inter.ListProject)>0:
        for i in inter.ListProject:
            if (i.pos.x<WIDTH) or (i.pos.x>0) or (i.pos.y<HEIGHT) or (i.pos.y>0):
                i.drawprojectile(canvas)
                i.update()
            else:
                del inter.ListProject[i]

def drag_handler(position):
    inter.MCdrag(position)

def click_handler(position):
    inter.MCclick(position)

frame = simplegui.create_frame("Rabbit on Acid", WIDTH, HEIGHT)
frame.set_draw_handler(draw_handler)
frame.set_mousedrag_handler(drag_handler)
frame.set_mouseclick_handler(click_handler)
frame.start()