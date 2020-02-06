from Vector import Vector
import math

class Corridor:
    def __init__(self, room1, room2):
        self.__room1 = room1
        self.__room2 = room2
        self.__path = []
        self.__intersect = self.__tunnel()
        self.__straightline_distance = math.sqrt(
              (self.__room2.getCenter().y - self.__room1.getCenter().y)**2
            + (self.__room2.getCenter().x - self.__room1.getCenter().x)**2
        )
        self.__width = 5
        self.__walls = self.__generateWalls()

    def __tunnel(self):
        """
        "Tunnels" from room1 to room2 and adds the vectors to __path
        """
        r1_center = self.__room1.getCenter()
        r2_center = self.__room2.getCenter()
        intersect = Vector(r1_center.x, r1_center.y)
        if(r2_center.x > r1_center.x):
            while(intersect.x != r2_center.x):
                intersect.x += 1
        else:
            while(intersect.x != r2_center.x):
                intersect.x -= 1
        return(intersect)

    def __generateWalls(self):
        """
        Generates the wall vectors for the corridor
        """
        radius = self.__width/2
        intersect_outer_corner = self.__intersect.__add__( Vector(radius, radius) )
        intersect_inner_corner = self.__intersect.__sub__( Vector(radius, radius) )

        if(self.__intersect.y > self.__room1.getCenter().y):
            wall1_start = Vector( self.__room1.getCenter().x - radius,
                                  self.__room1.getCenter().y + (self.__room1.getHeight()/2) )
            wall2_start = Vector( self.__room1.getCenter().x + radius,
                                  self.__room1.getCenter().y + (self.__room1.getHeight()/2) )
        if(self.__intersect.y < self.__room1.getCenter().y):
            wall1_start = Vector( self.__room1.getCenter().x - radius,
                                  self.__room1.getCenter().y - (self.__room1.getHeight()/2) )
            wall2_start = Vector( self.__room1.getCenter().x + radius,
                                  self.__room1.getCenter().y - (self.__room1.getHeight()/2) )

    def isColliding(self, pos):
        """
        Potential method to check if anything collides with the wall, given a vector
        """
        pass

    def draw(self, canvas):
        canvas.draw_line(self.__room1.getCenter().get_p(), self.__intersect.get_p(), 5, "Yellow")
        canvas.draw_line(self.__room2.getCenter().get_p(), self.__intersect.get_p(), 5, "Yellow")

    def getRooms(self):
        return [self.__room1, self.__room2]

    def getStraightDistance(self):
        return(self.__straightline_distance)
