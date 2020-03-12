from Vector import*
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

#Canvas dimensions
WIDTH = 500
HEIGHT = 500

class MC:

    def __init__(self, pos):
       
        #Movement vectors
        self.pos = pos
        self.vel = Vector()

        #Spritesheet data
        self.spritesheet = simplegui.load_image("https://i.imgur.com/hpehVFb.png")
        self.img_width = 128
        self.img_height = 128
        self.img_columns = 4
        self.img_rows = 4

        #Frame data
        self.frame_width = self.img_width / self.img_columns
        self.frame_height = self.img_height / self.img_rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2
        self.frame_index = [1,0]
        self.frame_duration = 10
        self.frameclock = 0
    
    def update_frameindex(self):
        self.frame_index[1] = (self.frame_index[1] + 1) % self.img_rows
    
    def draw(self, canvas):
        self.frameclock += 1
        if (self.frameclock % self.frame_duration == 0):
            self.update_frameindex()
        
        frame_centre = (self.frame_width * self.frame_index[0] + self.frame_centre_x, self.frame_height * self.frame_index[1] + self.frame_centre_y)
        frame_size = (self.frame_width, self.frame_height)
        canvas.draw_image(self.spritesheet, frame_centre, frame_size, self.pos.get_p(), frame_size)
    
    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.85)

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

class Keyboard:

    def __init__(self):
        self.down = False
        self.up = False
        self.right = False
        self.left = False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['s']:
            self.down = True
        elif key == simplegui.KEY_MAP['w']:
            self.up = True
        elif key == simplegui.KEY_MAP['d']:
            self.right = True
        elif key == simplegui.KEY_MAP['a']:
            self.left = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['s']:
            self.down = False
        elif key == simplegui.KEY_MAP['w']:
            self.up = False
        elif key == simplegui.KEY_MAP['d']:
            self.right = False
        elif key == simplegui.KEY_MAP['a']:
            self.left = False

class Interaction:

    def __init__(self, MC, keyboard, mouse):
        self.MC = MC
        self.keyboard = keyboard
        self.mouse = mouse

    def update(self):
        if self.mouse.is_newpos():
            mousepos = self.mouse.pos
            currpos = self.MC.pos.get_p()
            direction = Vector(mousepos[0]-currpos[0], mousepos[1]-currpos[1])
            
            if (direction.angle(Vector(1,0))>0.785 and direction.angle(Vector(1,0))<2.356) and (mousepos[1]<=currpos[1]):
                self.MC.frame_index[0]=2
            if (direction.angle(Vector(1,0))>0.785  and direction.angle(Vector(1,0))<2.356) and (mousepos[1]>=currpos[1]):
                self.MC.frame_index[0]=1
            if (direction.angle(Vector(1,0))<=0.785):
                self.MC.frame_index[0]=3
            if (direction.angle(Vector(1,0))>=2.356):
                self.MC.frame_index[0]=0
            self.mouse.save_lastpos()
            
            if self.keyboard.up:
                self.MC.vel.add(Vector(0, -0.75))
            if self.keyboard.down:
                self.MC.vel.add(Vector(0, 0.75))
            if self.keyboard.right:
                self.MC.vel.add(Vector(0.75, 0))
            if self.keyboard.left:
                self.MC.vel.add(Vector(-0.75, 0))
        else:
            if self.keyboard.up:
                self.MC.vel.add(Vector(0, -0.75))
                self.MC.frame_index[0]=2
            if self.keyboard.down:
                self.MC.vel.add(Vector(0, 0.75))
                self.MC.frame_index[0]=1
            if self.keyboard.right:
                self.MC.vel.add(Vector(0.75, 0))
                self.MC.frame_index[0]=3
            if self.keyboard.left:
                self.MC.vel.add(Vector(-0.75, 0))
                self.MC.frame_index[0]=0

    def MCdraw(self, canvas):
        self.update()
        self.MC.update()
        self.MC.draw(canvas)
    
    def MCdrag(self, position):
        self.mouse.drag(position)
    
    def MCclick(self, position):
        self.mouse.click(position)
    
    def MCkeyD(self, key):
        self.keyboard.keyDown(key)
    
    def MCkeyU(self, key):
        self.keyboard.keyUp(key)

'''#Create objects from different classes
bunny = MC(Vector(WIDTH/2, HEIGHT/2))
kbd = Keyboard()
mouse = Mouse(bunny.pos.get_p())
inter = Interaction(bunny, kbd, mouse)

def draw(canvas):
    inter.MCdraw(canvas)

def drag_handler(position):
    inter.MCdrag(position)

def click_handler(position):
    inter.MCclick(position)

def keyDown_handler(key):
    inter.MCkeyD(key)

def keyUp_handler(key):
    inter.MCkeyU(key)



# Create a frame and call events
frame = simplegui.create_frame("Rabbit on Acid", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keyDown_handler)
frame.set_keyup_handler(keyUp_handler)
frame.set_mousedrag_handler(drag_handler)
frame.set_mouseclick_handler(click_handler)
frame.start()'''