from Attacks import *
from Creatures import *
from Interactions import *
from Map import Map
from Healthbar import PlayerHealthbar
from Score import Score
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector
from Score import Score
from Collisions import Collisions


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

        self.player = Wizard( Vector(self.canvas_width/2, self.canvas_height/2))
        self.creatures.append(self.player)
        self.health = PlayerHealthbar(self.player, ( 20, 20 ), ( 120, 120 ))
        self.score = Score(self.canvas_width - 50, 5)
        self.floor = 0

        self.objects = [self.creatures, self.attacks, [self.health]]
        self.removeList = []
        self.interactions = [AttackCreatureInteraction(self.attacks, self.creatures)]
        
        self.__min_room_size = 256
        self.__max_rooms = 12
        self.__random_rooms = 0.4

        self.map = Map(self.__min_room_size, self.__min_room_size, self.canvas_width, self.canvas_height)




    def start(self):
        self.change_state("game")#self.change_state("start screen")
        #probably extras
        self.frame.set_draw_handler(self.draw_handler)
        self.frame.start()
        
    def start_game(self):#called from the start screen 
        #does stuff to prepare for the game to begin
        self.map.generate(self.__max_rooms, self.__random_rooms, [self.canvas_width, self.canvas_height])
        self.rooms = self.map.getRooms()
        self.interactions.append(AttackRoomInteraction(self.attacks, self.rooms))

    def change_state(self, newState):
        states = ["start screen","game","pause","corridor"]
        if newState in states:
            if newState == "start screen":
                pass#set handlers
            elif newState == "game":
                #set handlers
                self.frame.set_mouseclick_handler(self.player.main_attack)
                self.frame.set_keydown_handler(self.player.moveD)
                self.frame.set_keyup_handler(self.player.moveU)
            elif newState == "pause":
                pass#set handlers
            elif newState == "corridor":
                pass#set handlers
            self.state = newState

    def draw_handler(self, canvas):#always draw handler
        if self.state == "start screen":
            pass #play the start screen
        elif self.state == "game":
            self.map.generate(self.__max_rooms, self.__random_rooms, [self.canvas_width, self.canvas_height])
            self.current_room = self.map.getRooms()[0]
            self.draw_all(canvas)
            pass #draw all and update all
        elif self.state == "pause": #pressing Esc while in game loop switches to pause
            self.draw_all(canvas)
        elif self.state == "corridor":
            pass #run corridor 
        
    def update_all(self):
        for interaction in self.interactions:
            interaction.manageInteractions()
        for array in self.objects:
            for item in array:
                if isinstance(item, Enemy):
                    item.update(self.player)
                else:
                    item.update()
                if isinstance(item, Creature):
                    self.attacks.extend(item.attackList)
                    item.attackList = []
        for attack in self.attacks:
            if attack.done:
                removeList.append(attack)
        remove_objects()
    
    def draw_all(self,canvas):
        collisions_handler = Collisions(self.player, self.current_room)
        self.current_room.draw(canvas)

        collisions_handler.update()
        new_room = collisions_handler.getNewRoom()

        if(new_room != None):
            old_room = self.current_room
            current_room = new_room
            self.player.setPos( current_room.getNewRoomPos(old_room) )
        if(collisions_handler.doGenerateNewMap()):
            self.map.generate(self.__max_rooms, self.__random_rooms, [self.canvas_width, self.canvas_height])
            self.current_room = self.map.getRooms()[0]

        for array in self.objects:
            for item in array:
                item.draw(canvas)
                
    def remove_objects(self):
        for item in self.removeList:
            for array in self.objects:
                if item in array:
                    if isinstance(item, Enemy):
                        if item.killed:
                            self.player.increaseExp(item.exp)
                    array.remove(item)
                    break

game = Game()
game.start()
