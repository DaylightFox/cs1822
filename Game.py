from Attacks import *
from Creatures import *
from Interactions import *
from Map import Map
from Healthbar import PlayerHealthbar
from Score import Score
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector
from startScreen import Start



class Game:
    def __init__(self):
        title = "Trip: Down The Rabbit Hole" #working title
        self.canvas_width = 500
        self.canvas_height = 500
        self.frame = simplegui.create_frame(title, self.canvas_width, self.canvas_height)
        self.state = ""
        self.creatures = []
        self.attacks = []

        self.player = Wizard( Vector(self.canvas_width/2, self.canvas_height/2) )
        self.creatures.append(player)
        self.health = PlayerHealthbar(self.player, ( 20, 20 ), ( 120, 120 ))
        self.score = Score(self.canvas_width - 50, 5)
        self.floor = 0

        self.objects = [self.creatures, self.attacks]
        self.removeList = []
        self.interactions = [AttackCreatureInteraction(self.attacks, self.creatures)]
        
        self.__min_room_size = 256
        self.__max_rooms = 12
        self.__random_rooms = 0.4

        self.map = Map(self.__min_room_size, self.__min_room_size, self.canvas_width, self.canvas_height)




    def start(self):
        self.state = "start screen"
        #probably extras
        frame.start()
        
    def start_game(self):#called from the start screen 
        #does stuff to prepare for the game to begin
        self.map.generate(self.__max_rooms, self.__random_rooms, [self.canvas_width, self.canvas_height])
        self.rooms = self.map.getRooms()
        self.interactions.append(AttackRoomInteraction(self.attacks, self.rooms))


    def draw_handler(self, canvas):
        if self.state == "start screen":
            pass #play the start screen
            #set event handlers for screen
            #the start screen should return the name of a different state
        elif self.state == "game":
            #set event handlers for screen
            self.draw_all(canvas)
            pass #draw all and update all
        elif self.state == "pause": #pressing Esc while in game loop switches to pause
            #set click handlers
            self.draw_all(canvas)
            pass #draw all but dont update
        elif self.state == "corridor":
            pass #run corridor 
        
    def update_all(self):
        for interaction in self.interactions:
            interaction.manageInteractions()
        for array in self.objects:
            for item in array:
                item.update()
        remove_objects()
    
    def draw_all(self,canvas):
        for array in self.objects:
            for item in array:
                item.draw(canvas)
                
    def remove_objects(self):
        for item in self.removeList:
            for array in self.objects:
                if item in array:
                    array.remove(item)
                    break
        ##if self.removeList != []:
        ##    #raise Exception()#
        ##    pass
        self.removeList = []
