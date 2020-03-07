import Creatures
import animation
try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
try:
    from Vector import Vector
except ImportError:
    from user304_rsf8mD0BOQ_1 import Vector

class Bunny(Creatures.Wizard, animation.MC):
    def __init__(self, pos):
        super().__init__(pos)
        self.frame_index = [1,0]
        self.frame_duration = 10
        self.frameclock = 0
        self.img_rows = 4
        self.img_columns = 4
        self.sprite = simplegui.load_image("https://i.imgur.com/hpehVFb.png")
        self.width_height_source = [self.sprite.get_width()/4, self.sprite.get_width()/4]
        self.center_source = [self.width_height_source[0]/2, self.width_height_source[1]/2]
        
        
    def draw(self, canvas):
        self.nextFrame()
        super().draw(canvas)
        
        
    def nextFrame(self):
        self.frameclock += 1
        if (self.frameclock % self.frame_duration == 0):
            self.update_frameindex()
        
        self.center_source = (self.width_height_source[0] * self.frame_index[0] + self.width_height_source[0]/2, self.width_height_source[1] * self.frame_index[1] + self.width_height_source[1]/2)
