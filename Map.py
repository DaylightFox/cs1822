import random
from Room import Room
from Vector import Vector

class Map:
    def __init__(self, min_width, min_height, max_width, max_height, debug=False):
        """

        Notes:
            mid_width & min_height need to be binary, as in 32/64/128 etc.
        """
        self.__min_width = min_width
        self.__min_height = min_height
        self.__max_width = max_width
        self.__max_height = max_height
        self.__rooms = []
        self.__max_neighbours = 3
        self.__show_map = debug # for debug purposes
        self.__tile_size = 32

    def generate(self, map_size, max_rooms, screen_size):
        """
        Generates a map of rooms

        Keyword arguments:
        map_size - an integer that defines how large of a grid to generate the map on
        max_rooms - an integer that states the maximum number of rooms to make. Min: 2
        screen_size - a tuple of the screen size
        """
        self.__map_grid = [ [ 0 for i in range(map_size) ] for i in range(map_size) ]

        # Set starting room coords
        current = [ int(map_size/2), int(map_size/2) ]
        for num_of_rooms in range(max_rooms + 1):
            center = Vector(screen_size[0]/2, screen_size[1]/2)
            if(num_of_rooms == 0):
                room = Room(center,
                            random.randrange(self.__min_width, self.__max_width, self.__tile_size),
                            random.randrange(self.__min_height, self.__max_height, self.__tile_size),
                            "start" )
            elif(num_of_rooms == max_rooms):
                room = Room(center,
                            random.randrange(self.__min_width, self.__max_width, self.__tile_size),
                            random.randrange(self.__min_height, self.__max_height, self.__tile_size),
                            "end" )
            else: 
                room = Room(center,
                            random.randrange(self.__min_width, self.__max_width, self.__tile_size),
                            random.randrange(self.__min_height, self.__max_height, self.__tile_size)
                            )

            self.__map_grid[current[0]][current[1]] = room
            valid_pos = False
            if(num_of_rooms > 0):
                #print(current[0], current[1], self.__map_grid[current[0]][current[1]])
                #print(self.__prev[0], self.__prev[1], self.__map_grid[self.__prev[0]][self.__prev[1]])
                room.addNeighbour( self.__prev, self.__invertHeading(self.__prev_heading) )
                self.__prev.addNeighbour( room, self.__prev_heading )
            while(not valid_pos):
                direction = random.randint(0,3) # choose which direction to go
                if(direction == 0):
                    # North
                    current[1] += 1
                    heading = "N"
                elif(direction == 1):
                    # East
                    current[0] += 1
                    heading = "E"
                elif(direction == 2):
                    # South
                    current[1] -= 1
                    heading = "S"
                else:
                    # West
                    current[0] -= 1
                    heading = "W"
                if(not( current[0] > map_size-1
                     or current[0] < 0
                     or current[1] > map_size-1
                     or current[1] < 0 )
                     and self.__map_grid[current[0]][current[1]] == 0):
                    valid_pos = True
                    self.__prev_heading = heading
                    self.__prev = room
        if(self.__show_map):
            print("Map generated:")
            for row in self.__map_grid:
                for col in range(len(row)-1):
                    if(row[col] != 0):
                        print(" 1 ", end="")
                    else:
                        print(" 0 ", end="")
                print("\n")

    def __invertHeading(self, heading):
        if(heading == "N"):
            return("S")
        elif(heading == "E"):
            return("W")
        elif(heading == "S"):
            return("N")
        else:
            return("E")

    def getRooms(self):
        rooms = []
        size = len(self.__map_grid)-1
        for row in range(size):
            for col in range(size):
                if(self.__map_grid[row][col] != 0):
                    rooms.append(self.__map_grid[row][col])
        for room in rooms:
            if(room.isStart()):
                rooms.remove(room)
                rooms.insert(0, room)
            elif(room.isEnd()):
                rooms.remove(room)
                rooms.insert(len(rooms), room)
        return(rooms)


    