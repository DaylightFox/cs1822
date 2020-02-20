

class Wall:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    def draw(self, canvas):
        """
        Draws the wall

        Keyword arguments:
        canvas - the SimpleGUI canvas
        """
        canvas.draw_line(self.__start.get_p(), self.__end.get_p(), 5, "Red")