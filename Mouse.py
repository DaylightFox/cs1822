class Mouse:

    def __init__(self, pos):
        self.pos = pos
        self.last_pos = pos

    def drag(self, position):
        self.pos = position
    
    def click(self, position):
        self.pos = position
    
    def save_lastpos(self):
        self.last_pos = self.pos
    
    def is_newpos(self):
        return(self.last_pos != self.pos)