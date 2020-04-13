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
        hp_percent = self.player.getHealth() / self.player.getMaxHealth()
        split_x = self.topL[0] + hp_percent * self.length
        
        if hp_percent < 1:
            canvas.draw_line((self.botR[0], self.V_centre), (split_x, self.V_centre), self.width, "red")
        canvas.draw_line((self.topL[0], self.V_centre), (min(self.botR[0], split_x), self.V_centre), self.width, "green")
        if hp_percent > 1:
            canvas.draw_line((self.topL[0], self.V_centre), (split_x - self.length, self.V_centre), self.width, "blue")
        
        hp_str = str(self.player.getHealth())+"/"+str(self.player.getMaxHealth())
        canvas.draw_text(hp_str, (self.topL[0], self.botR[1]), 12, "white")
