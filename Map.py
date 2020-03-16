import random
from Room import Room
from Vector import Vector
from Creatures import *

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

    def generate(self, max_rooms, random_percentage, screen_size):
        """
        Generates a list of rooms with a size of `max_rooms`

        Keyword arguments:
        max_rooms - an integer with the maximum number of rooms wanted
        random_percentage - the percent of rooms to keep for adding randomly to the map
        screen_size - a tuple of ints that represent the screen size
        """
        self.__rooms = []
        linear_rooms = int((max_rooms + 1) * (1 - random_percentage))
        random_rooms = max_rooms - linear_rooms
        center = Vector(screen_size[0]/2, screen_size[1]/2)
        for i in range(linear_rooms):
            if(i == 0):
                r = Room(center,
                        random.randrange(self.__min_width, self.__max_width, self.__tile_size),
                        random.randrange(self.__min_height, self.__max_height, self.__tile_size),
                        "start" )
            elif(i == linear_rooms-1):
                r = Room(center,
                        random.randrange(self.__min_width, self.__max_width, self.__tile_size),
                        random.randrange(self.__min_height, self.__max_height, self.__tile_size),
                        "end" )
            else:
                r = Room(center,
                        random.randrange(self.__min_width, self.__max_width, self.__tile_size),
                        random.randrange(self.__min_height, self.__max_height, self.__tile_size)
                        )

            heading = self.__getRandomHeading()
            self.__rooms.append(r)
            if(i > 0):
                while(self.__rooms[i-1].headingExists(heading)):
                    heading = self.__getRandomHeading()
                self.__rooms[i-1].addNeighbour(r, heading)
                r.addNeighbour(self.__rooms[i-1], self.__invertHeading(heading))

        for i in range(random_rooms):
            chosen_room = self.__rooms[random.randint(0, len(self.__rooms)-1)]
            while(len(chosen_room.getEmptyNeighbours()) == 0 or chosen_room.isStart() or chosen_room.isEnd()):
                chosen_room = self.__rooms[random.randint(0, len(self.__rooms)-1)]
            heading = self.__getRandomHeading()
            while(chosen_room.headingExists(heading)):
                heading = self.__getRandomHeading()
            r = Room(center,
                     random.randrange(self.__min_width, self.__max_width, self.__tile_size),
                     random.randrange(self.__min_height, self.__max_height, self.__tile_size)
                     )
            chosen_room.addNeighbour(r, heading)
            r.addNeighbour(chosen_room, self.__invertHeading(heading))
            self.__rooms.append(r)

        #self.__addEnemies()
                    

    def __addEnemies(self):
        """
        Adds enemies to the rooms on map generated
        """
        num_of_enemy_types = 3
        for room in self.getRooms():
            enemies = []
            num_to_spawn = random.randint(1,2)
            for e in range(num_to_spawn):
                for i in range(num_of_enemy_types-1):
                    if(i == 0):
                        enemies.append( Goblin(room.getRandomPos()) )
                    elif(i == 1):
                        enemies.append( DaggerGoblin(room.getRandomPos()) )
            room.addEnemies(enemies)



    def __getRandomHeading(self):
        """
        Generates a random heading
        """
        choice = random.randint(0, 3)
        if(choice == 0):
            return "N"
        elif(choice == 1):
            return "E"
        elif(choice == 2):
            return "S"  
        else:
            return "W"  

    def __invertHeading(self, heading):
        """
        Inverts a given heading
        """
        if(heading == "N"):
            return("S")
        elif(heading == "E"):
            return("W")
        elif(heading == "S"):
            return("N")
        else:
            return("E")

    def getRooms(self):
        """
        Returns a sorted list of rooms where the first item will be a `start` room and the last item will be the `end` room
        """
        rooms = self.__rooms
        for room in rooms:
            if(room.isStart()):
                rooms.remove(room)
                rooms.insert(0, room)
            elif(room.isEnd()):
                rooms.remove(room)
                rooms.insert(len(rooms), room)
        return(rooms)


    