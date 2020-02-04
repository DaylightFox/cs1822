import math
from Vector import Vector

class Room:
    def __init__(self, center, width, height):
        self.__width = width
        self.__height = height
        self.__center = center
        #self.__center.x = (WIDTH/2) + self.__center.x
        #self.__center.y = (HEIGHT/2) + self.__center.y
        self.__updatePosVectors()

    def draw(self, canvas):
        corners = [corner.get_p() for corner in self.__corners]
        canvas.draw_polygon(corners, 5, "Red")

    def addToPos(self, vector):
        self.__center += vector
        self.__updatePosVectors()

    def __updatePosVectors(self):
        self.__top_left = Vector(math.floor(self.__center.x - (self.__width/2)),
                                 math.floor(self.__center.y - (self.__height/2)))
        self.__top_right = Vector(math.floor(self.__center.x + (self.__width/2)),
                                   math.floor(self.__center.y - (self.__height/2)))
        self.__bot_right = Vector(math.floor(self.__center.x + (self.__width/2)),
                                  math.floor(self.__center.y + (self.__height/2)))
        self.__bot_left = Vector(math.floor(self.__center.x - (self.__width/2)),
                                 math.floor(self.__center.y + (self.__height/2)))
        self.__corners = [self.__top_left,
                          self.__top_right,
                          self.__bot_right,
                          self.__bot_left]

    def getCenter(self):
        return(self.__center)
    
    def getCorners(self):
        return(self.__corners)

    def getWidth(self):
        return(self.__width)

    def getHeight(self):
        return(self.__height)