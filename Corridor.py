from Vector import Vector

class Corridor:
    def __init__(self, room1, room2):
        self.__room1 = room1
        self.__room2 = room2
        self.__path = []
        self.__intersect = self.__tunnel()

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

    def draw(self, canvas):
        canvas.draw_line(self.__room1.getCenter().get_p(), self.__intersect.get_p(), 5, "Yellow")
        canvas.draw_line(self.__room2.getCenter().get_p(), self.__intersect.get_p(), 5, "Yellow")
