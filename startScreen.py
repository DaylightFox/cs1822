#START SCREEN
try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Vector import Vector
from animationV4 import*

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
        self.spaceKey = False
        self.title = ["Welcome to...", "Trip: Down The Rabbit Hole"]
        self.storyText = ["HUH... WHERE AM I?", "It's another one...", "... get him...", "!!! I NEED TO GET OUT OF HERE"]
        self.wasd = simplegui._load_local_image("Images/WASDkeys.png")
        self.wasdPos = (60,150)
        self.left = simplegui._load_local_image("Images/leftKey.png")
        self.leftPos = (50, 250)
        self.right = simplegui._load_local_image("Images/rightKey.png")
        self.rightPos = (50, 350)
        self.mc = MC(Vector(WIDTH/2,HEIGHT/2))
        self.size = (2048, 2048)
        self.resize = (150,150)
        self.centre = (2048/2, 2048/2)

    def goToNext(self):
        return (self.key == simplegui.KEY_MAP['space'])

    
    def tutorial(self, canvas):
        i=0
        canvas.draw_text('Tutorial', (180, 50), 30, 'white', 'monospace')
        canvas.draw_text('Move Character', (150, 150), 20, 'white', 'monospace')
        canvas.draw_text('Left Click & Drag to Shoot', (150, 250), 20, 'white', 'monospace')
        canvas.draw_text('Right Click to ____', (150, 350), 20, 'white', 'monospace')

        #timerText(self.title, self.title.length())
        
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
#timer = simplegui.create_timer(800, timer_handler)
#timer.start()
#frame.start()
