from Vector import Vector

class Door:
    def __init__(self, heading, center):
        """
        Generate a Door object based on the heading and center pos.
        """
        self.__heading = heading
        self.__width = 40
        self.__center = center
        self.__col_box_size = 10
        self.__show_col_box = False
        if(self.__heading == "N" or self.__heading == "S"):
            self.__p1 = Vector( (self.__center.x - self.__width/2), self.__center.y )
            self.__p2 = Vector( (self.__center.x + self.__width/2), self.__center.y )
            self.bounds = [ Vector(self.__p1.x, self.__p1.y - self.__col_box_size),
                            Vector(self.__p2.x, self.__p2.y - self.__col_box_size),
                            Vector(self.__p2.x, self.__p2.y + self.__col_box_size),
                            Vector(self.__p1.x, self.__p2.y + self.__col_box_size) ]
        else:
            self.__p1 = Vector( self.__center.x, (self.__center.y - self.__width/2) )
            self.__p2 = Vector( self.__center.x, (self.__center.y + self.__width/2) )
            self.bounds = [ Vector(self.__p1.x - self.__col_box_size, self.__p1.y),
                            Vector(self.__p1.x + self.__col_box_size, self.__p1.y),
                            Vector(self.__p2.x + self.__col_box_size, self.__p2.y),
                            Vector(self.__p2.x - self.__col_box_size, self.__p2.y) ]
            

    def draw(self, canvas):
        """
        Draws the door on the canvas

        Keyword arguments:
        canvas - The SimpleGUI canvas
        """
        canvas.draw_line(self.__p1.get_p(), self.__p2.get_p(), 5, "Yellow")
        if(self.__show_col_box):
            b_list = []
            for bound in self.bounds:
                b_list.append(bound.get_p())
            canvas.draw_polygon(b_list, 3, "Green")

    def getBounds(self):
        """
        Returns the collision box for the door
        """
        return(self.bounds)

    def inBounds(self, obj):
        """
        Returns a bool if the given obj is within the collision box

        Keyword arguments:
        obj - and object that has a getPos() method that returns a Vector
        """
        obj_x = obj.getPos().x
        obj_y = obj.getPos().y
        return(     obj_x >= self.bounds[0].x 
                and obj_x <= self.bounds[1].x
                and obj_y >= self.bounds[0].y
                and obj_y <= self.bounds[2].y )

    def getSpawnPos(self):
        """
        Returns a Vector object with the spawn position for the character
        relative to the heading
        """
        if(self.__heading == "N"):
            return( Vector( self.__center.x, self.__center.y + self.__col_box_size + 1 ) )
        elif(self.__heading == "E"):
            return( Vector( self.__center.x - self.__col_box_size - 1, self.__center.y ) )
        elif(self.__heading == "S"):
            return( Vector( self.__center.x, self.__center.y - self.__col_box_size - 1 ) )
        else:
            return( Vector( self.__center.x + self.__col_box_size + 1, self.__center.y ) )
        
