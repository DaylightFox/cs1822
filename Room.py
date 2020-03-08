from Vector import Vector
from Wall import Wall
from Door import Door
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Room:
    def __init__(self, center, width, height, type="none"):
        self.__center = center
        self.__width = width
        self.__height = height
        self.__top_left = Vector( self.__center.x - self.__width/2, self.__center.y - self.__height/2 )
        self.__top_right = Vector( self.__center.x + self.__width/2, self.__center.y - self.__height/2 )
        self.__bot_left = Vector( self.__center.x - self.__width/2, self.__center.y + self.__height/2 )
        self.__bot_right = Vector( self.__center.x + self.__width/2, self.__center.y + self.__height/2 )
        self.__walls = [ Wall(self.__top_left, self.__top_right, "N"),
                         Wall(self.__top_right, self.__bot_right, "E"),
                         Wall(self.__bot_right, self.__bot_left, "S"),
                         Wall(self.__bot_left, self.__top_left, "W") ]
        self.__type = type
        self.__characters = []
        self.__neighbours = {"N":None, "E":None, "S":None, "W":None}
        self.__doors = {}

        self.__tileset = simplegui._load_local_image("game-map-tileset.png")
        self.__wall_sprite_size = ( 32, 32 )
        self.__wall_sprite_pos_dict = {"N": (  16 , ( 64 + self.__wall_sprite_size[1]/2 ) ),
                                       "E": ( ( 32 + self.__wall_sprite_size[0]/2 ), ( 64 + self.__wall_sprite_size[1]/2 ) ),
                                       "S": ( ( 96 + self.__wall_sprite_size[0]/2 ), ( 64 + self.__wall_sprite_size[1]/2 ) ),
                                       "W": ( ( 64 + self.__wall_sprite_size[0]/2 ), ( 64 + self.__wall_sprite_size[1]/2 ) )}
        self.__corner_sprite_pos_dict = {"NW": ( ( 128 + 16 ), ( 64 + 16 ) ),
                                         "NE": (  16 , ( 96 + 16 ) ),
                                         "SE": ( ( 32 + 16 ), ( 96 + 16 ) ),
                                         "SW": ( ( 64 + 16 ), ( 96 + 16 ) )}
        self.__door_sprite_size = ( 64, 32 )
        self.__door_sprite_pos = ( ( 128 ), ( 128 + self.__door_sprite_pos[1]/2 ) )

    def isStart(self):
        return( self.__type == "start" )

    def isEnd(self):
        return( self.__type == "end" )

    def isBoss(self):
        return( self.__type == "boss" )

    def getNeighbours(self):
        return(self.__neighbours)

    def isCollidingWall(self, obj):
        """
        Returns a boolean if the given obj is colliding with a wall

        Keyword arguments:
        obj - an object that has a getPos() method that returns a Vector
        """
        obj_x = obj.getPos().x
        obj_y = obj.getPos().y
        return(    obj_x >= self.__top_right.x
                or obj_x <= self.__top_left.x
                or obj_y <= self.__top_right.y
                or obj_y >= self.__bot_right.y )

    def getCollidingDoor(self, obj):
        """
        Returns a Door object if the given obj is colliding with the door

        Keyword arguments:
        obj - an object that has a getPos() method that returns a Vector
        """
        for door in self.__doors:
            if(door.inBounds(obj)):
                return door

    def getRoomFromDoor(self, door):
        """
        Returns the room that is connected by the given door

        Keyword arguments:
        door - a Door object belonging to the Room
        """
        return( self.__neighbours[self.__doors[door]] )

    def getNewRoomPos(self, room):
        """
        Returns the spawn position when the character moves into the room,
        relative to the given room (the rooms must be connected)

        Keyword arguments:
        room - a Room object that is relative to this Room object
        """
        for door in self.__doors:
            if(self.__neighbours[self.__doors[door]] == room):
                return(door.getSpawnPos())


    def draw(self, canvas):
        """
        Draws the walls, doors & floor of the room

        Keyword arguments:
        canvas - the SimpleGUI canvas
        """
        for wall in self.__walls:
            wall.draw(canvas, self.__tileset, self.__wall_sprite_size, self.__wall_sprite_pos_dict, self.__corner_sprite_pos_dict)
        canvas.draw_polygon([self.__top_left.get_p(),
                             self.__top_right.get_p(),
                             self.__bot_right.get_p(),
                             self.__bot_left.get_p()], 0, 'rgb(66, 40, 53)', 'rgb(66, 40, 53)')
        for door in self.__doors:
            door.draw(canvas, self.__tileset, self.__door_sprite_pos, self.__door_sprite_size)


    def addNeighbour(self, room, direction):
        """
        Adds a neighbour in the given heading.

        Keyword arguments:
        room - a Room object to add as a neighbour
        direction - the heading of the new room relative to this Room ("N", "E", "S" or "W")
        """
        self.__neighbours[direction] = room
        if(direction == "N"):
            center = Vector( (self.__top_right.x + self.__top_left.x)/2, self.__top_right.y )
            d = Door("N", center)
        elif(direction == "E"):
            center = Vector( self.__bot_right.x, (self.__bot_right.y + self.__top_right.y)/2 )
            d = Door("E", center)
        elif(direction == "S"):
            center = Vector( (self.__bot_right.x + self.__bot_left.x)/2, self.__bot_left.y )
            d = Door("S", center)
        else:
            center = Vector( self.__bot_left.x, (self.__bot_left.y + self.__top_left.y)/2 )
            d = Door("W", center)
        self.__doors[d] = direction

    def getWidth(self):
        return(self.__width)

    def getHeight(self):
        return(self.__height)

    def __updateWalls(self):
        pass