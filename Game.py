from Attacks import *
from Creatures import *
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector





class Game:
    def __init__(self):
        title = "Trip: Down The Rabbit Hole" #working title
        self.canvas_width = 500
        self.canvas_height = 500
        self.frame = simplegui.create_frame(title, self.canvas_width, self.canvas_height)
        self.state = ""
        self.creatures = []
        self.attacks = []

        self.objects = [self.creatures, self.attacks]
        
        room_minimum_size = 256
        self.map = Map(room_minimum_size, room_minimum_size, self.canvas_width, self.canvas_height)




    def start(self):
        self.state = "start screen"
        #probably extras
        frame.start()


    def draw_handler(self, canvas):
        if self.state == "start screen":
            pass #play the start screen
            #set event handlers for screen
            #the start screen should return the name of a different state
        elif self.state == "game":
            #set event handlers for screen
            pass #draw all and update all
        elif self.state == "pause": #pressing Esc while in game loop switches to pause
            #set click handlers
            pass #draw all but dont update
        elif self.state == "corridor":
            pass #run corridor 
