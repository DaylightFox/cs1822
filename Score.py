from Vector import Vector


class Score:
    def __init__(self, pos, score=0):
        """
        Creates a Score object

        Keyword arguments:
        pos - an object for the position of the top left corner of the score
        score - the initial score (default: 0)
        """
        self.__pos = pos
        self.__score = score
        
    def getScore(self):
        """
        Returns the score
        """
        return(self.__score)

    def updateScore(self, score):
        """
        Update the score by adding an integer to it

        Keyword arguments:
        score - an integer to add to the score
        """
        self.__score += score

    def multiplyScore(self, multiplier):
        """
        Multiplies the current score by the given multiplier

        Keyword arguments:
        multiplier - a whole integer to multiply the score by
        """
        self.__score *= 1 + ( multiplier / 10 )
        self.__score = int(self.__score)

    def draw(self, canvas):
        """
        Draws the score on the screen

        Keyword arguments:
        canvas - the SimpleGUI canvas object
        """
        canvas.draw_text("Score: " + str(self.__score), self.__pos, 25 , 'white', 'monospace')