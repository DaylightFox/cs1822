try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Vector import Vector
from animationV4 import*
from Creatures import*
from Attacks import*
from Score import Score



WIDTH = 500
HEIGHT = 500

'''
Screen when character dies
'''

class End():
    def __init__(self, score):
        self.mc = MC(Vector(WIDTH/2, HEIGHT/2))
        self.middle = (WIDTH/2, HEIGHT/2)
        self.score = str(score)
        self.playAgain = False
        self.playAgainKey = [250, 80]


    def willPlayAgain(self, pos): #NEEDS CLICK HANDLER
        #defines click area for start key
        a = WIDTH/4
        b = HEIGHT - HEIGHT/4
        if (pos[0] >= a and pos[0] <= a + self.playAgainKey[0]) and (pos[1] >= b and pos[1] <= b + self.playAgainKey[1]):
            self.playAgain = True

    def playAgainDraw(self, canvas):
        a = WIDTH/4
        b = HEIGHT - HEIGHT/4

        #Rectangle Width and Height
        width = self.playAgainKey[0]
        height = self.playAgainKey[1]
        canvas.draw_polygon([(a, b), (a, b + height), (a + width, b + height), (a + width, b)],1, "grey", "Green")
        canvas.draw_text('Play Again?', (width/2 + a/2 + 10, height/2 + b + 10), 30, 'white', 'monospace')


    def deathScreen(self, score, canvas):
        canvas.draw_text("YOU DIED", self.middle, 40, 'white', 'monospace')
        canvas.draw_text("Your Score" + self.score, self.middle.y + 100, 30, 'white', 'monospace')
        self.playAgainDraw()

    def victoryScreen(self, score, canvas):
        canvas.draw_text("You Have Left the Rabbit Hole", self.middle, 40, 'white', 'monospace')
        canvas.draw_text("Your Score: " + self.score, self.middle.y + 100, 30, 'white', 'monospace')
        self.playAgainDraw()