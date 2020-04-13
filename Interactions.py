

class PlayerInputInteraction:

    def __init__(self, player, keyboard, mouse):
        self.player = player
        self.keyboard = keyboard
        self.mouse = mouse

    def MCdraw(self, canvas):
        self.player.draw(canvas, self.keyboard, self.mouse)

    def MCdrag(self, position):
        self.mouse.drag(position)
    
    def MCclick(self, position):
        self.mouse.click(position)
    
    def MCkeyD(self, key):
        self.keyboard.keyDown(key)
    
    def MCkeyU(self, key):
        self.keyboard.keyUp(key)

class PlayerGameInteraction:

    def __init__(self, player, room):
        self.player = player
        self.enemies = room.getEnemies()
        self.room = room
    
    def playerAttack(self, canvas):
        remove=[]
        for attack in self.player.getProjectiles():
            if(attack.isCollidingWall(self.room)):
                remove.append(attack)
            elif(len(self.enemies) > 0):
                for enemy in self.enemies:
                    if attack.isCollidingCreature(enemy):
                        remove.append(attack)
                        attack.deal_damage(enemy)
                    else:
                        attack.draw(canvas)
                        attack.update()
            else:
                attack.draw(canvas)
                attack.update()
        for attack in remove:
            self.player.removeProjectile(attack)
    
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

    def enemyAttack(self, canvas):
        for enemy in self.enemies:
            if(enemy.isRanged()):
                remove = []
                for attack in enemy.getProjectiles():
                    if attack.isCollidingCreature(self.player):
                        remove.append(attack)
                        attack.deal_damage(self.player)
                    elif attack.isCollidingWall(self.room):
                        remove.append(attack)
                    else:
                        attack.draw(canvas)
                        attack.update()
                for attack in remove:
                    enemy.removeProjectile(attack)
    
    def process(self, canvas):
        self.playerAttack(canvas)
        #self.ulting(canvas)
        self.enemyAttack(canvas)

