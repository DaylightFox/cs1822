#START SCREEN
try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Vector import Vector
from playerAnimation import*
from Mouse import Mouse
from Keyboard import Keyboard

'''
Mouse and Keyboard are necessary for the player to be drawn.
Handlers for them are not included.
'''

WIDTH = 500
HEIGHT = 500

class Start():
    def __init__(self):
        '''
        The Sequence for the beginning of the game
        Details:
        title - list of 2 strings showing title
        storyText - list of strings that show the story scenario
        

        '''
        #Start Screen Info
        #self.spaceKey = False
        self.title = ["Welcome to...", "Trip: Down The Rabbit Hole"]
        self.storyText = ["HUH... WHERE AM I?", "It's another one...", "... get him...", "!!! I NEED TO GET OUT OF HERE"]
        self.startKey = [250, 80]
        self.startClick = False
        self.beginGame = False
        self.counter = 0
       
        #TUTORIAL IMAGE INFO
        self.wasd = simplegui._load_local_image("Images/WASDkeys.png")
        self.wasdPos = (60,150)
        self.left = simplegui._load_local_image("Images/leftKey.png")
        self.leftPos = (50, 250)

        #self.right = simplegui._load_local_image("Images/rightKey.png")
        #self.rightPos = (50, 350)
        #self.space = simplegui._load_local_image("Images/spaceKey.png")
        #self.spacePos = (80, 350)

        self.size = (2048, 2048)
        self.resize = (150,150)
        self.centre = (2048/2, 2048/2)

        #SHOW Main CHARACTER
        self.bunny = MC(Vector(WIDTH/2, HEIGHT/2))
        self.kbd = Keyboard()
        self.mouse = Mouse(self.bunny.pos.get_p())
        self.mc = Interaction(self.bunny, self.kbd, self.mouse)

    def KeyClick(self, pos):
        '''
        Defines click area for start key
        '''
        a = WIDTH/4
        b = HEIGHT - HEIGHT/4
        return (pos[0] >= a and pos[0] <= a + self.startKey[0]) and (pos[1] >= b and pos[1] <= b + self.startKey[1])
      
    def KeyDraw(self, canvas, keyText):
        '''
        Draws start key on screen
        '''
        #(a,b) is the top  left corner of rectangle fixed to WIDTH = 500, HEIGHT = 500
        a = WIDTH/4
        b = HEIGHT - HEIGHT/4

        #Rectangle Width and Height
        width = self.startKey[0]
        height = self.startKey[1]
        canvas.draw_polygon([(a, b), (a, b + height), (a + width, b + height), (a + width, b)],1, "grey", "Green")
        canvas.draw_text(keyText , (width/2 + a/2 + 10, height/2 + b + 10), 30, 'white', 'monospace')


    def tutorial(self, canvas):
        '''
        Tutorial Page demonstrating player controls
        '''
        canvas.draw_text('Tutorial', (180, 50), 30, 'white', 'monospace')
        canvas.draw_text('Move Character', (150, 150), 20, 'white', 'monospace')
        canvas.draw_text('Left Click & Drag to Shoot', (150, 250), 20, 'white', 'monospace')
        #canvas.draw_text('Space for Alternate Fire', (180, 350), 20, 'white', 'monospace')

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
        '''
        canvas.draw_image(self.space, 
                         self.centre,
                         self.size,
                         self.spacePos,
                         (self.resize[0] + 50, self.resize[1] + 50))
        '''
    def titleSequence(self, canvas, text):
        '''
        Draws Game Title
        '''
        canvas.draw_text(text[0], (150, 100), 30, 'white', 'monospace')
        canvas.draw_text(text[1], (20, 150), 30, 'white', 'monospace')
        #self.counterInc()
        #print(self.counter)

    
    def update(self, canvas):
        #self.titleSequence(canvas)
        '''
            Handles Transition:
            Start Screen -> Tutorial -> Game
        '''
        
        if (self.startClick == False):
            self.KeyDraw(canvas, "START")
            self.titleSequence(canvas, self.title)
            self.mc.MCdraw(canvas)
            
        if (self.startClick == True):
            self.tutorial(canvas)
            self.KeyDraw(canvas, "BEGIN")
        
        if (self.beginGame == True):
            return ("game")

        '''
        if (self.goToNext == True):
            self.mc(Vector(WIDTH/2,HEIGHT/2))
            self.mc.draw(canvas)
        '''
