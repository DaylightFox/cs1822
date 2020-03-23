class Collisions:
    def __init__(self, sprite, room):
        self.__sprite = sprite
        self.__room = room
        self.__in_collision = False
        self.__new_room = None
        self.__new_map = False

    def update(self):
        door = self.__room.getCollidingDoor(self.__sprite)
        if(door != None):
            self.__new_room = self.__room.getRoomFromDoor(door)
        if(self.__room.isEnd()):
            if(self.__room.isCollidingLevelDoor(self.__sprite)):
                self.__new_map = True
        if(self.__room.isCollidingWall(self.__sprite)):
            if(not self.__in_collision):
                self.__sprite.pauseMove(self.__room)
                self.__in_collision = True
        else:
            self.__in_collision = False

    def getNewRoom(self):
        room = self.__new_room
        self.__new_room = None
        return(room)

    def doGenerateNewMap(self):
        new = self.__new_map
        self.__new_map = False
        return(new)