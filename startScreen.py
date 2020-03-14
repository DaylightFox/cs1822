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
        '''
        title - list of 2 strings showing title
        storyText - list of strings that show the story scenario
        '''
        #Start Screen Info
        #self.spaceKey = False
        self.title = ["Welcome to...", "Trip: Down The Rabbit Hole"]
        self.storyText = ["HUH... WHERE AM I?", "It's another one...", "... get him...", "!!! I NEED TO GET OUT OF HERE"]
        self.counter = 0
        self.startKey = [250, 80]
        self.startClick = False
       
        #TUTORIAL IMAGE INFO
        self.wasd = simplegui._load_local_image("Images/WASDkeys.png")
        self.wasdPos = (60,150)
        self.left = simplegui._load_local_image("Images/leftKey.png")
        self.leftPos = (50, 250)
        self.right = simplegui._load_local_image("Images/rightKey.png")
        self.rightPos = (50, 350)
        self.size = (2048, 2048)
        self.resize = (150,150)
        self.centre = (2048/2, 2048/2)

        #SPRITE SHOW
        self.mc = MC(Vector(60, HEIGHT - 60))

    #def goToNext(self):
    #    return (self.spaceKey == simplegui.KEY_MAP['space'])


    def click(self, pos):
        #size of start key
        a = WIDTH/4
        b = HEIGHT - HEIGHT/4
        if (pos[0] >= a and pos[0] <= a + self.startKey[0]) and (pos[1] >= b and pos[1] <= b + self.startKey[1]):
            self.startClick = True
        

    
    def startKeyEvent(self, canvas):
        #(a,b) is the top  left corner of rectangle fixed to WIDTH = 500, HEIGHT = 500
        a = WIDTH/4
        b = HEIGHT - HEIGHT/4

        #Rectangle Width and Height
        width = self.startKey[0]
        height = self.startKey[1]
        canvas.draw_polygon([(a, b), (a, b + height), (a + width, b + height), (a + width, b)],1, "grey", "Green")
        canvas.draw_text('START', (width/2 + a/2 + 10, height/2 + b + 10), 30, 'white', 'monospace')
        #return (width, height)

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

        self.mc.draw(canvas)

    
    def titleSequence(self,canvas):
        if (self.counter%30 == 0):
            canvas.draw_text(self.title[0], (180, 50), 30, 'white', 'monospace')

    
    def update(self, canvas):
        #self.titleSequence(canvas)
        '''
        self.counter +=1
        if (self.goToNext()):
            self.tutorial(canvas)
        '''
        if (self.startClick == False):
            self.startKeyEvent(canvas)
        if (self.startClick == True):
            self.tutorial(canvas)

    
    #def keyDown(self):
