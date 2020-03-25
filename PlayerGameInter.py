from playerAnimation import*
from enemyAnimation import*

WIDTH=500
HEIGHT=500

class PlayerGameInter:

    def __init__(self, player, listEnemy): #+curr_room
        self.player = player
        self.listEnemy = listEnemy
        #self.curr_room = curr_room
    
    def playerShoot(self, canvas):
        remove=[]
        for i in self.player.ListAttack:
            for j in self.listEnemy:
                if i.hit_creature(j):
                    remove.append(i)
                    #i.deal_damage(j)
                #elif i.hit_room(self.curr_room):
                    #remove.append(i)
                elif (i.pos.x>WIDTH) or (i.pos.x<0) or (i.pos.y>HEIGHT) or (i.pos.y<0):
                    remove.append(i)
                else:
                    i.drawprojectile(canvas)
                    i.update()
        for i in remove:
            self.player.ListAttack.remove(i)
    
    def ulting(self, canvas):
        if (self.player.ultOn):
            self.player.Ultimate.drawfb(canvas)
            self.player.ultLength -= 1
            #for i in self.listEnemy:
                #if self.player.Ultimate.hit_creature(i):
                    #self.player.Ultimate.deal_damge(i)
        if (self.player.ultLength < 0):
            self.player.ultOn = False
            self.player.ultLength = 100

    def enemyShoot(self, canvas):
        for i in self.listEnemy:
            remove = []
            for j in i.ListAttack:
                if j.hit_creature(self.player):
                    remove.append(j)
                    #j.deal_damage(self.player)
                #elif j.hit_room(self.curr_room):
                    #remove.append(j)
                elif (j.pos.x>WIDTH) or (j.pos.x<0) or (j.pos.y>HEIGHT) or (j.pos.y<0):
                    remove.append(j)
                else:
                    j.drawprojectile(canvas)
                    j.update()
            for j in remove:
                i.ListAttack.remove(j)
    
    def drawfight(self, canvas):
        self.playerShoot(canvas)
        self.ulting(canvas)
        self.enemyShoot(canvas)




