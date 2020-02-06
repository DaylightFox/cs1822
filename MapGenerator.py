import random
from Vector import Vector
from Room import Room
from Corridor import Corridor
import math


class MapGenerator:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__rooms = []
        self.__corridors = []

    def getRooms(self):
        return(self.__rooms)
    
    def getCorridors(self):
        return(self.__corridors)

    def generate(self, min_room_size, max_room_size, max_rooms, min_rooms=0):
        """
        Generates rooms and corridors
        """
        for i in range(min_rooms, max_rooms):
            overlap = True
            while(overlap):
                center = self.__randomPoint()
                width = random.randint(min_room_size, max_room_size+1)
                height = random.randint(min_room_size, max_room_size+1)
                room = Room(center, width, height)
                passes = 0
                for r in self.__rooms:
                    if(not self.__doOverlap(room, r)):
                        passes += 1
                if passes == len(self.__rooms):
                    overlap = False
            self.__rooms.append( room )

        # Temporary
        for r1 in self.__rooms:
            for r2 in self.__rooms:
                if(r1 != r2):
                    self.__corridors.append(Corridor(r1, r2))

        self.__reduceCorridors()

    def __reduceCorridors(self):
        """
        Creates a minimum spanning tree of corridors and then
        adds extra_corridors_percent% extra corridors to make loops.
        """
        extra_corridors_percent = 0.1
        corridors_to_keep = []
        for room in self.__rooms:
            shortest_distance = 999
            for corridor in self.__corridors:
                if room in corridor.getRooms():
                    if corridor.getStraightDistance() < shortest_distance:
                        shortest = corridor
                        shortest_distance = corridor.getStraightDistance()
            corridors_to_keep.append(shortest)
        total_corridors = len(self.__corridors)
        extra_corridors_to_keep = math.floor(total_corridors * extra_corridors_percent)
        for corridor_to_keep in corridors_to_keep:
            for corridor in self.__corridors:
                if corridor_to_keep == corridor:
                    self.__corridors.remove(corridor)
        extra_corridors = []
        while(len(extra_corridors) < extra_corridors_to_keep):
            i = random.randint(0, len(self.__corridors)-1)
            extra_corridors.append(self.__corridors[i])
            self.__corridors.pop(i)
        self.__corridors = corridors_to_keep + extra_corridors


    def __doOverlap(self, room1, room2):
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
            if(corner.x in range(room2_corners[0].x, room2_corners[1].x)):
                return True
            elif(corner.y in range(room2_corners[0].y, room2_corners[3].y)):
                return True
        return False

    def __randomPoint(self):
        """
        Generates a random Vector inside the width & height
        """
        x = random.randint(0, self.__width)
        y = random.randint(0, self.__height)
        return Vector(x, y)
