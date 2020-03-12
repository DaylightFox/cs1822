from Vector import*
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH = 500
HEIGHT = 500

class Projectile:

    def __init__(self, pos, vel, angle):

        #Movement vectors
        self.pos = pos
        self.vel = vel

        #Angle
        self.angle = angle

        #Spritesheet data
        self.spritesheet = simplegui.load_image("https://i.imgur.com/T8BwM8E.png")
        self.img_width = 840
        self.img_height = 54
        self.img_columns = 10
        self.img_rows = 6

        #Frame data
        self.frame_width = self.img_width / self.img_columns
        self.frame_height = self.img_height / self.img_rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2
        self.frame_index = [1,0]
        self.frame_duration = 2
        self.frameclock = 0
    
    def update_frameindex(self):
        self.frame_index[0] = (self.frame_index[0] + 1) % self.img_columns
        if self.frame_index[0] == 0:
            self.frame_index[1] = (self.frame_index[1] + 1) % self.img_rows
    
    def drawprojectile(self, canvas):
        self.frameclock += 1
        if (self.frameclock % self.frame_duration == 0):
            self.update_frameindex()
        
        frame_centre = (self.frame_width * self.frame_index[0] + self.frame_centre_x, self.frame_height * self.frame_index[1] + self.frame_centre_y)
        frame_size = (self.frame_width, self.frame_height)
        canvas.draw_image(self.spritesheet, frame_centre, frame_size, self.pos.get_p(), frame_size, self.angle)
    
    def update(self):
        self.pos.add(self.vel)
        #self.vel.multiply(0.85)