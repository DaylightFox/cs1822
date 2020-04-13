from Vector import Vector
from Creatures import Wizard




'''
Screen when character dies
'''

class EndScreen():
    '''
    Arguments - 
    Score: Final Score achieved by player
    playerState: "dead" or "alive"

    Draws corresponding Screen for Victory or Defeat and displays score
    Prompts player to play again(this will restart the game loop)

    topLeftD - top left position of Death screen text
    topLeftA - top left position of Victory screen text

    '''
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.bunny = Wizard(Vector(self.width/2, self.height/2))
        self.topLeftD = (130,100)
        self.topLeftA = (30, 100)
        self.score = 0

        self.playAgain = False
        self.state = None
        self.playAgainKey = [300, 80]

    def updatePlayerState(self, state):
        # Expecting either "dead" or "alive"
        self.state = state

    def updateScore(self, score):
        self.score = str(score)

    def willPlayAgain(self, pos):
        #defines click area for start key
        a = self.width/4 + 10
        b = self.height - self.height/4
        if (pos[0] >= a and pos[0] <= a + self.playAgainKey[0]) and (pos[1] >= b and pos[1] <= b + self.playAgainKey[1]):
            self.playAgain = True

    def playAgainDraw(self, canvas):
        a = self.width/4 - 10 #topLeft
        b = self.height - self.height/4

        #Rectangle Width and Height
        width = self.playAgainKey[0]
        height = self.playAgainKey[1]
        canvas.draw_polygon([(a, b), (a, b + height), (a + width, b + height), (a + width, b)],1, "grey", "green")
        canvas.draw_text('Play Again', (width/2 + (a/2 - 20), height/2 + (b + 10)), 30, 'white', 'monospace')


    def deathScreen(self, score, canvas):
        canvas.draw_text("GAME OVER", self.topLeftD, 50, 'red', 'monospace')
        canvas.draw_text("Your Score: " + self.score, (self.topLeftD[0] + 30, self.topLeftD[1] + 100), 20, 'white', 'monospace')
        self.playAgainDraw(canvas)

    def victoryScreen(self, score, canvas):
        canvas.draw_text("You Have Left the Rabbit Hole", self.topLeftA, 25, 'yellow', 'monospace')
        canvas.draw_text("Your Score: " + self.score, (self.topLeftA[0], self.topLeftA[1] + 100), 20, 'white', 'monospace')
        self.playAgainDraw(canvas)

    def update(self, canvas):
        #self.titleSequence(canvas)
        '''
            Handles Transition:
            Start Screen -> Tutorial -> Game
        '''
        states = ["dead", "alive"]
        if (self.state in states):
            if (self.state == "alive"):
                self.victoryScreen(self.score, canvas)
            elif (self.state == "dead"):
                self.deathScreen(self.score, canvas)
        
    def doPlayAgain(self):
        return(self.playAgain)