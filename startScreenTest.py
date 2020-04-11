from startScreen import*
WIDTH = 500
HEIGHT = 500

startScreen = Start()

frame = simplegui.create_frame('Start Screen', WIDTH, HEIGHT)
frame.set_draw_handler(startScreen.update)
frame.set_mouseclick_handler(startScreen.KeyClick)

frame.start()