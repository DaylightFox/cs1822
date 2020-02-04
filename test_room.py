import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector
import math, random
from Room import Room
from MapGenerator import MapGenerator



WIDTH = 500
HEIGHT = 500
ROOMS = 8

class Ball:
    def __init__(self):
        self.pos = Vector(WIDTH/2, HEIGHT/2)
        self.radius = 10
        self.colour = "Yellow"
        self.velocity = Vector(1,1)
    
    def draw(self, canvas):
        canvas.draw_circle(self.pos.get_p(), self.radius, 1, self.colour, self.colour)

    def update(self):
        self.pos += self.velocity

class Interaction:
    def __init__(self):
        self.ball = Ball()
        self.room = Room(Vector(WIDTH/2, HEIGHT/2), 150, 150)

    def draw(self, canvas):
        self.ball.draw(canvas)
        self.room.draw(canvas)
        self.ball.update()
        self.checkCollision()

    def checkCollision(self):
        ball_pos = self.ball.pos
        radius = self.ball.radius
        corners = self.room.getCorners()
        if(ball_pos.x+radius >= corners[1].x):
            self.ball.velocity = Vector()
        elif(ball_pos.x-radius <= corners[0].x):
            self.ball.velocity = Vector()
        elif(ball_pos.y+radius <= corners[0].y):
            self.ball.velocity = Vector()
        elif(ball_pos.y-radius >= corners[2].y):
            self.ball.velocity = Vector()


            


interaction = Interaction()

def draw(canvas):
    global interaction
    interaction.draw(canvas)
    

    



frame = simplegui.create_frame("Map Gen", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

frame.start()