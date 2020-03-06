import Creatures
import animation

class Bunny(Wizard, MC):
    def __init__(self, pos):
        super().__init__(pos)
        self.frame_index = [1,0]
        self.frame_duration = 10
        self.frameclock = 0
        self.sprite = simplegui.load_image("https://i.imgur.com/hpehVFb.png")
        self.width_height_source = [sprite.get_width/4, sprite.get_width/4]
        self.width_height_source_frame = self.width_height_source.copy()
        self.center_source = [self.width_height_source[0]/2, self.width_height_source[1]/2]
        
        
    def draw(self, canvas):
        self.nextFrame()
        super().draw(canvas)
        
        
    def nextFrame(self):
        #pass
        self.frameclock += 1
        if (self.frameclock % self.frame_duration == 0):
            self.update_frameindex()
        
        self.width_height_dest = (self.width_height_source_frame[0] * self.frame_index[0], self.width_height_source_frame[1] * self.frame_index[1])
