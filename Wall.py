import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector

class Wall:
    def __init__(self, start, end, heading, debug=False):
        self.__start = start
        self.__end = end
        self.__heading = heading
        self.__show_debug_walls = debug

    def draw(self, canvas, tileset, tile_size, walls, corners):
        """
        Draws the wall

        Keyword arguments:
        canvas - the SimpleGUI canvas
        tileset - a SimpleGUI Image object with a tilset loaded
        tile_size - a tuple with the tile size (e.g. 32x32)
        walls - a dictionary with a key:value pair of heading:sprite_source_position
        corners - a dictionary with a key:value pair of heading:sprite_source_position
        """
        top_left_corner = corners["NW"]
        top_right_corner = corners["NE"]
        bot_right_corner = corners["SE"]
        bot_left_corner = corners["SW"]
        wall = walls[self.__heading]
        half_tile_size_x = tile_size[0]/2
        half_tile_size_y = tile_size[1]/2
        if(self.__heading == "N"):
            top_left_pos = ( ( self.__start.x - half_tile_size_x ), ( self.__start.y - half_tile_size_y ) )
            top_right_pos = ( ( self.__end.x + half_tile_size_x ), ( self.__end.y - half_tile_size_y ) )
            canvas.draw_image(tileset, top_left_corner, tile_size, top_left_pos, tile_size)
            
            dest_center = Vector( self.__start.x + half_tile_size_x, self.__start.y - 6 ) # the -6 is an offset to get the wall into correct pos
            end_point = self.__end.x - half_tile_size_x
            while( dest_center.x <= end_point ):
                canvas.draw_image(tileset, wall, tile_size, dest_center.get_p(), tile_size)
                dest_center.x += tile_size[0]

            canvas.draw_image(tileset, top_right_corner, tile_size, top_right_pos, tile_size)

        elif(self.__heading == "E"):

            dest_center = Vector( self.__start.x + 17, self.__start.y + half_tile_size_y )
            end_point = self.__end.y + half_tile_size_y
            while( dest_center.y < end_point ):
                canvas.draw_image(tileset, wall, tile_size, dest_center.get_p(), tile_size)
                dest_center.y += tile_size[1]
            
        elif(self.__heading == "S"):
            bot_right_pos = ( ( self.__start.x + half_tile_size_x ), ( self.__start.y + half_tile_size_y ) )
            bot_left_pos = ( ( self.__end.x - half_tile_size_x), ( self.__end.y + half_tile_size_y ) )
            canvas.draw_image(tileset, bot_right_corner, tile_size, bot_right_pos, tile_size)

            dest_center = Vector( self.__start.x - half_tile_size_x, self.__start.y + 17 ) # +17 is offset
            end_point = self.__end.x - half_tile_size_x
            while( dest_center.x > end_point ):
                canvas.draw_image(tileset, wall, tile_size, dest_center.get_p(), tile_size)
                dest_center.x -= tile_size[0]

            canvas.draw_image(tileset, bot_left_corner, tile_size, bot_left_pos, tile_size)

        elif(self.__heading == "W"):
            dest_center = Vector( self.__start.x - 17, self.__start.y - half_tile_size_y )
            end_point = self.__end.y
            while( dest_center.y > end_point ):
                canvas.draw_image(tileset, wall, tile_size, dest_center.get_p(), tile_size)
                dest_center.y -= tile_size[1]

        if(self.__show_debug_walls):
            canvas.draw_line(self.__start.get_p(), self.__end.get_p(), 1, "Red")