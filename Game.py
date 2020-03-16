from Attacks import *
from Creatures import *
from Interactions import *
from Map import Map
from Healthbar import PlayerHealthbar
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector
from Score import Score





class Game:
    def __init__(self):
        title = "Trip: Down The Rabbit Hole" #working title
        self.canvas_width = 500
        self.canvas_height = 500
        self.frame = simplegui.create_frame(title, self.canvas_width, self.canvas_height)
        self.state = ""
        self.creatures = []
        self.attacks = []

        self.player = Player( Vector(self.canvas_width/2, self.canvas_height/2) )
        self.player.maxHp = 300
        self.player.currentHp = 300
        self.health = PlayerHealthbar(self.player, ( 20, 20 ), ( 120, 120 ))
        self.score = 0
        self.floor = 0

        self.objects = [self.creatures, self.attacks]
        self.removeList = []
        
        self.__min_room_size = 256
        self.__max_rooms = 12
        self.__random_rooms = 0.4

        self.map = Map(self.__min_room_size, self.__min_room_size, self.canvas_width, self.canvas_height)




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
            self.map.generate(self.__max_rooms, self.__random_rooms, [self.canvas_width, self.canvas_height])
            rooms = self.map.getRooms()
            #set event handlers for screen
            pass #draw all and update all
        elif self.state == "pause": #pressing Esc while in game loop switches to pause
            #set click handlers
            pass #draw all but dont update
        elif self.state == "corridor":
            pass #run corridor 
