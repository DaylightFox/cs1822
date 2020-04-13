try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Keyboard:

    def __init__(self):
        self.down = False
        self.up = False
        self.right = False
        self.left = False
        self.spacebar = False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['s']:
            self.down = True
        elif key == simplegui.KEY_MAP['w']:
            self.up = True
        elif key == simplegui.KEY_MAP['d']:
            self.right = True
        elif key == simplegui.KEY_MAP['a']:
            self.left = True
        elif key == simplegui.KEY_MAP['space']:
            self.spacebar = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['s']:
            self.down = False
        elif key == simplegui.KEY_MAP['w']:
            self.up = False
        elif key == simplegui.KEY_MAP['d']:
            self.right = False
        elif key == simplegui.KEY_MAP['a']:
            self.left = False
        elif key == simplegui.KEY_MAP['space']:
            self.spacebar = False

class Mouse:

    def __init__(self, pos):
        self.pos = pos
        self.last_pos = pos

    def getPos(self):
        return(self.pos)

    def drag(self, position):
        self.pos = position
    
    def click(self, position):
        self.pos = position
    
    def save_lastpos(self):
        self.last_pos = self.pos
    
    def is_newpos(self):
        return(self.last_pos != self.pos)