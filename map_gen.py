import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector
import math, random



WIDTH = 500
HEIGHT = 500
ROOMS = 8

class GenerateMap:
    """
    Class handles random map generation
    """
    def __init__(self, width, height):
        """
        Constructor for GenerateMap class

        Keyword arguments:
        width - Width of the canvas
        height - Height of the canvas
        """
        self.canvas_width = width
        self.canvas_height = height
        self.grid_size = 1 # grid size in pixels
        self.min_room_size = 30
        self.max_room_size = 100
        self.rooms = []

    def generate(self, num_of_rooms):
        """
        Generates the number of rooms specified. Clears previous rooms when called.

        Keyword arguments:
        num_of_rooms - The number of rooms to generate
        """
        self.rooms = []
        for i in range(num_of_rooms):
            center = self.getRandomPoint(50)
            self.rooms.append(Room(self.min_room_size, self.max_room_size, center))
    
    def getRandomPoint(self, radius):
        """
        Generates random Vectors around a given radius

        Keyword arguments:
        radius - The radius to generate points within
        """
        R = radius
        u = random.uniform(0,1) + random.uniform(0,1)
        t = random.uniform(0,1) * math.pi * 2
        r = 2-u if u>1 else u
        x = R * r * math.cos(t)
        y = R * r * math.sin(t)
        return( Vector(x, y) )

    def getRooms(self):
        """
        Returns all the rooms as a list of Room objects
        """
        return(self.rooms)

    def separateRooms(self):
        """
        Uses separation steering to space the rooms out from each other
        """

    def doOverlap(self, room1, room2):
        """
        Returns boolean on whether the two given rooms overlap

        Keyword arguments:
        room1 - A room object
        room2 - A room object
        """
        room1_corners = room1.getCorners()
        room2_corners = room2.getCorners()
        # [0] = Top left
        # [1] = Top Right
        # [2] = Bot Right
        # [3] = Bot Left
        for corner in room1_corners:
            print((corner.x < room2_corners[1].x), corner.x, room2_corners[1].x)
            print((corner.x > room2_corners[0].x), corner.x, room2_corners[0].x)
            print((corner.y < room2_corners[1].y), corner.y, room2_corners[1].y)
            print((corner.y > room2_corners[2].y), corner.y, room2_corners[2].y)
            print(corner.x < room2_corners[1].x and corner.x > room2_corners[0].x)
            print(corner.y < room2_corners[1].y and corner.y > room2_corners[2].y)
            print("------------------------")
            if((corner.x < room2_corners[1].x and corner.x > room2_corners[0].x)
                and (corner.y < room2_corners[1].y and corner.y > room2_corners[2].y)):
                return True
        return False



    def squashVector(self, vector):
        """
        Returns a list of two vectors with either the x or y set to 0

        Keyword arguments:
        vector - A vector object to "squash"
        """
        v1 = Vector(vector.x, 0)
        v2 = Vector(0, vector.y)
        return([v1, v2])





class Room:
    def __init__(self, min_size, max_size, center):
        self.__width = random.randint(min_size, max_size)
        self.__height = random.randint(min_size, max_size)
        self.__center = center
        self.__center.x = (WIDTH/2) + self.__center.x
        self.__center.y = (HEIGHT/2) + self.__center.y
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

    def draw(self, canvas):
        corners = [corner.get_p() for corner in self.__corners]
        canvas.draw_polygon(corners, 5, "Red")

    def getCenter(self):
        return(self.__center)
    
    def getCorners(self):
        return(self.__corners)


mapGen = GenerateMap(WIDTH, HEIGHT)
mapGen.generate(2)
rooms = mapGen.getRooms()
print(mapGen.doOverlap(rooms[0], rooms[1]))
print("+++++++++++++++++++++++++++++")
print(mapGen.doOverlap(rooms[1], rooms[0]))
r1 = Room(50, 50, Vector(50,50))
r2 = Room(50, 50, Vector(250,250))
#print(mapGen.doOverlap(r1,r2))

def draw(canvas):
    global mapGen, points
    
    for room in mapGen.getRooms():
        room.draw(canvas)
    

    



frame = simplegui.create_frame("Map Gen", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

frame.start()