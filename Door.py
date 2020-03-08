from Vector import Vector

class Door:
    def __init__(self, heading, center, debug=False):
        """
        Generate a Door object based on the heading and center pos.

        Keyword arguments:
        heading - The position of the door in the room (e.g. door is at top so pass in "N" for heading)
        center - A Vector object containing the position of the center of the door
        """
        self.__heading = heading
        self.__width = 64
        self.__center = center
        self.__col_box_size = 10
        self.__show_col_box = debug
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
            

    def draw(self, canvas, tileset, sprite_pos, size):
        """
        Draws the door on the canvas. Rotates door sprite based on `self.__heading`.
        Adjusts sprite position on canvas by a margin of 1 to fit walls.

        Keyword arguments:
        canvas - The SimpleGUI canvas
        """
        if(self.__heading == "N"):
            rotation = 3.14159
            dest = ( self.__center.x, self.__center.y + 1 )
        elif(self.__heading == "E"):
            rotation = 4.71239
            dest = ( self.__center.x - 1, self.__center.y )
        elif(self.__heading == "S"):
            rotation = 0
            dest = ( self.__center.x, self.__center.y - 1 )
        elif(self.__heading == "W"):
            rotation = 1.5708
            dest = ( self.__center.x + 1, self.__center.y )
        canvas.draw_image(tileset, sprite_pos, size, dest, size, rotation)
        # For debug purposes:
        if(self.__show_col_box):
            canvas.draw_line(self.__p1.get_p(), self.__p2.get_p(), 5, "Yellow")
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
        
