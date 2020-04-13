from Interactions import *
from Map import Map
from Healthbar import PlayerHealthbar
from Score import Score
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector
from Collisions import Collisions
from Inputs import *
from StartScreen import StartScreen
from EndScreen import EndScreen
from Creatures import Wizard



class Game:
    def __init__(self):
        title = "Trip: Down The Rabbit Hole" #working title
        self.canvas_width = 500
        self.canvas_height = 500
        self.frame = simplegui.create_frame(title, self.canvas_width, self.canvas_height)
        self.frame.set_canvas_background( "rgb(28, 17, 23)" )
        self.state = "start"

        self.start_screen = StartScreen(self.canvas_width, self.canvas_height)
        self.end_screen = EndScreen(self.canvas_width, self.canvas_height)

        # Player
        self.player = Wizard( Vector(self.canvas_width/2, self.canvas_height/2))
        self.health = PlayerHealthbar(self.player, ( 20, 20 ), ( 170, 50 ))
        self.score = Score((self.canvas_width - 150, 40))
        self.floor = 0

        # Interactions
        self.keyboard = Keyboard()
        self.mouse = Mouse( (self.canvas_width/2, self.canvas_height/2) )
        self.player_input = PlayerInputInteraction(self.player, self.keyboard, self.mouse)
        self.player_game = None

        
        # Map Generation
        self.__min_room_size = 256
        self.__max_rooms = 12
        self.__random_rooms = 0.4
        self.map = None




    def start(self):
        self.change_state("start")
        self.frame.set_draw_handler(self.draw_handler)
        self.frame.start()

        
    def start_game(self):#called from the start screen 
        self.map = Map(self.__min_room_size, self.__min_room_size, self.canvas_width, self.canvas_height)
        self.map.generate(self.__max_rooms, self.__random_rooms, (self.canvas_width, self.canvas_height))
        self.current_room = [self.map.getRooms()[0]]
        self.player_game = PlayerGameInteraction( self.player, self.current_room[0] )

    def change_state(self, newState):
        states = ["start","game","end"]
        if newState in states:
            if newState == "start":
                self.frame.set_mouseclick_handler(self.start_screen.KeyClick)
            elif newState == "game":
                self.frame.set_keydown_handler(self.keyDown_handler)
                self.frame.set_keyup_handler(self.keyUp_handler)
                self.frame.set_mousedrag_handler(self.drag_handler)
                self.frame.set_mouseclick_handler(self.click_handler)
            elif newState == "end":
                self.frame.set_mouseclick_handler(self.end_screen.willPlayAgain)
            self.state = newState

    def draw_handler(self, canvas):#always draw handler
        if self.state == "start":
            self.start_screen.update(canvas)
            if(self.start_screen.canStartGame()):
                self.start_game()
                self.change_state("game")
        elif self.state == "game":
            self.update_all()
            self.draw_all(canvas)
        elif self.state == "end": 
            self.end_screen.update(canvas)
            if(self.end_screen.doPlayAgain()):
                self.player = Wizard( Vector(self.canvas_width/2, self.canvas_height/2))
                self.health = PlayerHealthbar(self.player, ( 20, 20 ), ( 170, 50 ))
                self.score = Score((self.canvas_width - 150, 40))
                self.floor = 0
                self.start_game()
                self.change_state("game")
        
    def update_all(self):
        collisions_handler = Collisions(self.player, self.current_room[0])
        collisions_handler.update()
        new_room = collisions_handler.getNewRoom()
        if(new_room != None):
            old_room = self.current_room[0]
            self.current_room[0] = new_room
            self.player.setPos( self.current_room[0].getNewRoomPos(old_room) )
            self.player_game = PlayerGameInteraction( self.player, self.current_room[0] )
        if(collisions_handler.doGenerateNewMap()):
            self.floor += 1
            self.map.generate(self.__max_rooms, self.__random_rooms, [self.canvas_width, self.canvas_height])
            self.current_room[0] = self.map.getRooms()[0]
            self.player_game = PlayerGameInteraction( self.player, self.current_room[0] )
            self.player.restoreHealth( self.player.getHealth()/2 )

        for e in self.current_room[0].getEnemies():
            if(e.isDead()):
                self.score.updateScore(e.getScore())
                self.current_room[0].removeEnemy(e)

        if(self.player.getHealth() <= 0):
            self.score.multiplyScore(self.floor)
            self.end_screen.updatePlayerState("dead")
            self.end_screen.updateScore(self.score.getScore())
            self.change_state("end")
                
        

        
    
    def draw_all(self,canvas):
        # Draws room and enemies in room
        self.current_room[0].draw(canvas)

        # Draw player character
        self.player.draw(canvas, self.keyboard, self.mouse)

        # Handle projectiles
        self.player_game.process(canvas)

        # Draw enemies
        enemies = self.current_room[0].getEnemies()
        for e in enemies:
            e.draw(canvas, self.player, self.current_room[0])
        
        # UI Components
        self.health.draw(canvas)
        self.score.draw(canvas)

    # Handlers
    def drag_handler(self, position):
        self.player_input.MCdrag(position)

    def click_handler(self, position):
        self.player_input.MCclick(position)

    def keyDown_handler(self, key):
        self.player_input.MCkeyD(key)

    def keyUp_handler(self, key):
        self.player_input.MCkeyU(key)

game = Game()
game.start()
