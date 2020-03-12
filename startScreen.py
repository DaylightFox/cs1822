#START SCREEN
try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from animationV3 import MC
from Vector import Vector

'''
when going to a different stage
main function in each file
takes optional parameters
stats, player, etc
feed in the frame(the simple gui frame)
'''

WIDTH = 500
HEIGHT = 500

class Start():
    def __init__(self):
        self.wasd = simplegui._load_local_image("Images/WASDkeys.png")
        self.wasdPos = (60,150)
        self.left = simplegui._load_local_image("Images/leftClick.png")
        self.leftPos = (50, 250)
        self.right = simplegui._load_local_image("Images/rightClick.png")
        self.rightPos = (50, 350)
        self.mc = MC(Vector(100,300))
        self.size = (2048, 2048)
        self.resize = (150,150)
        self.centre = (2048/2, 2048/2)

    
    def tutorial(self, canvas):
        canvas.draw_text('Tutorial', (180, 50), 30, 'white', 'monospace')
        canvas.draw_text('Move Character', (150, 150), 20, 'white', 'monospace')
        canvas.draw_text('Left Click & Drag to Shoot', (150, 250), 20, 'white', 'monospace')
        canvas.draw_text('Right Click to ____', (150, 350), 20, 'white', 'monospace')
        
        canvas.draw_image(self.wasd, 
                         self.centre,
                         self.size,
                         self.wasdPos,
                         self.resize)
        canvas.draw_image(self.left, 
                         self.centre,
                         self.size,
                         self.leftPos,
                         self.resize)
        canvas.draw_image(self.right, 
                         self.centre,
                         self.size,
                         self.rightPos,
                         self.resize)

    
    #def keyDown(self):
        


#startScreen = Start()

#frame = simplegui.create_frame('Start Screen', WIDTH, HEIGHT)
#frame.set_draw_handler(startScreen.tutorial)
#frame.set_keydown_handler(startScreen.keyDown)
#frame.start()