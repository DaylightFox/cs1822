#START SCREEN
try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Vector import Vector
from Creatures import Wizard
from Inputs import *
from Interactions import PlayerInputInteraction

'''
Mouse and Keyboard are necessary for the player to be drawn.
Handlers for them are not included.
'''

class StartScreen():
    def __init__(self, width, height):
        '''
        The Sequence for the beginning of the game
        startClick and beginGame are states both initialized to False
        Game begins after both sequences have been set to True

        '''
       
        self.title = ["Welcome to...", "Trip: Down The Rabbit Hole"]
        #self.storyText = ["HUH... WHERE AM I?", "It's another one...", "... get him...", "!!! I NEED TO GET OUT OF HERE"]
        self.Key = [200, 50]
        self.startClick = False
        self.beginGame = False
        self.counter = 0
        self.width = width
        self.height = height


        self.titleImage= simplegui.load_image("https://i.imgur.com/a1CyvTu.png")
        self.tutorialImage = simplegui.load_image("https://i.imgur.com/9y4AX1b.png")

        self.size = (2048, 2048)
        #self.resize = (150,150)
        self.centre = (2048/2, 2048/2)

        #SHOW Main CHARACTER
        self.bunny = Wizard( Vector(self.width/2, 130) )
        self.kbd = Keyboard()
        self.mouse = Mouse(self.bunny.getPos().get_p())
        self.mc = PlayerInputInteraction(self.bunny, self.kbd, self.mouse)

        self.start_game = False

    def KeyClick(self, pos):
        '''
        Defines click area for key
        '''
        a = self.width//4 + 50
        b = self.height - self.height/4
        if (pos[0] >= a and pos[0] <= a + self.Key[0]) and (pos[1] >= b and pos[1] <= b + self.Key[1]):
            self.startClick = True
            self.counter+=1
            if (self.counter == 2):
                self.beginGame = True
      
    def KeyDraw(self, canvas, keyText):
        '''
        Draws key on screen
        '''
        #(a,b) is the top  left corner of rectangle fixed to self.width = 500, self.height = 500
        a = self.width/4
        b = self.height - self.height/4

        #Rectangle Width and Height
        width = self.Key[0]
        height = self.Key[1]
        canvas.draw_polygon([(a, b), (a, b + height), (a + width, b + height), (a + width, b)],1, "grey", "Green")
        
        canvas.draw_text(keyText , (width/2 + a/2 + 10, height/2 + b + 10), 30, 'white', 'monospace')


    def tutorial(self, canvas):
        '''
        Tutorial Page demonstrating player controls
        '''
        canvas.draw_image(self.tutorialImage,
                          self.centre,
                          self.size,
                         (self.width/2, self.height/2),
                         (self.width, self.height))
        self.mc.MCdraw(canvas)
        
    def titleSequence(self, canvas, text):
        '''
        Draws Game Title
        '''
        canvas.draw_image(self.titleImage, 
                         self.centre,
                         self.size,
                         (self.width/2, self.height/2),
                         (self.width, self.height))   
    
    def update(self, canvas):
        #self.titleSequence(canvas)
        '''
            Handles Transition:
            Start Screen -> Tutorial -> Game
        '''
        if (self.startClick == False):
            self.titleSequence(canvas, self.title)
            
        if (self.startClick == True):
            self.tutorial(canvas)
            self.KeyDraw(canvas, "BEGIN")
        
        if ((self.beginGame == True) and (self.startClick == True)):
            self.start_game = True

    def canStartGame(self):
        return(self.start_game)
