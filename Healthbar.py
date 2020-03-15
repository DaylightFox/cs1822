"""import Creatures
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
"""
class PlayerHealthbar:
    def __init__(self, player, topL, botR):
        """
        player is the player
        topL = tuple coordinates of the top left corner
        botR = tuple coordinates of the bottom right corner
        """
        self.player = player
        self.topL = topL
        self.botR = botR
        self.V_centre = (botR[1] + topL[1])/2
        self.length = botR[0] - topL[0]#length of full bar
        self.width = botR[1] - topL[1]
        
    def draw(self, canvas):
        hp_percent = self.player.currentHp / self.player.maxHp
        split_x = hp_percent * self.length
        
        if hp_percent < 1:
            canvas.draw_line((self.botR[0], self.V_centre), (split_x, self.V_centre), self.width, "red")
        canvas.draw_line((self.topL[0], self.V_centre), (split_x, self.V_centre), self.width, "green")
        
        hp_str = str(self.player.currentHp)+"/"+str(self.player.maxHp)
        canvas.draw_text(hp_str, (self.topL[0], self.botR[1]), 12, "white")

"""def inputHandler(key):
    if key == simplegui.KEY_MAP["space"]:
        p1.currentHp -= 1
    else:
        p1.currentHp += 1


p1 = Creatures.Player((0,0))
p1.maxHp = 300
p1.currentHp = 300
hpBar = PlayerHealthbar(p1, (0,25), (300,75))

frame = simplegui.create_frame("Testing", 350,100)
frame.set_draw_handler(hpBar.draw)
frame.set_keydown_handler(inputHandler)
frame.set_keyup_handler(inputHandler)

frame.start()
"""
