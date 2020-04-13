from Attacks import *
import math
from random import randint

try:
    from Vector import Vector
except ImportError:
    from user304_rsf8mD0BOQ_1 import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Creature:
    def __init__(self, pos, radius, sprite, sprite_size, max_hp):
        # Positional Vectors
        self.pos = pos #centre of sprite
        self.vel = Vector(0,0)

        # Sprite parameters
        self.spritesheet = simplegui.load_image(sprite)
        self.img_width = sprite_size[0]
        self.img_height = sprite_size[1]
        self.img_columns = 4
        self.img_rows = 4

        # Frame data
        self.frame_width = self.img_width / self.img_columns
        self.frame_height = self.img_height / self.img_rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2
        self.radius = self.frame_width/2
        self.frame_index = [3,0]
        self.frame_duration = 10
        self.frameclock = 0

        self.max_hp = max_hp
        self.hp = max_hp
        self.dead = False
        
    def getPos(self):
        return(self.pos)

    def setPos(self, pos):
        self.pos = pos
        
    def draw(self, canvas):
        self.frameclock += 1
        if (self.frameclock % self.frame_duration == 0):
            self.update_frameindex()
        
        frame_centre = (self.frame_width * self.frame_index[0] + self.frame_centre_x, self.frame_height * self.frame_index[1] + self.frame_centre_y)
        frame_size = (self.frame_width, self.frame_height)
        canvas.draw_image(self.spritesheet, frame_centre, frame_size, self.pos.get_p(), frame_size)

    def update_frameindex(self):
        self.frame_index[1] = (self.frame_index[1] + 1) % self.img_rows

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.die()

    def die(self):
        self.dead = True

    def isDead(self):
        return(self.dead)

    def getHealth(self):
        return(self.hp)

    def getMaxHealth(self):
        return(self.max_hp)

    def resetHealth(self):
        self.hp = self.max_hp

    def restoreHealth(self, val):
        self.hp += int(val)
        if(self.hp > self.max_hp):
            self.hp = self.max_hp

    """
    def setLevel(self, level):
        self.level = level
        self.maxHp = int(self.maxHpBase * (
        self.levelScaleMultplier ** level))
        self.currentHp = self.maxHp
        self.Dmg = int(self.DmgBase * (self.levelScaleMultplier ** level))

    def levelUp(self):
        self.setLevel(self.level + 1)

    """
    
    def create_attack(self, target_pos, attackClass):
        target_pos = Vector(target_pos[0], target_pos[1])
        direction = (target_pos - self.pos).normalize()
        offset = 1
        source = self.pos + ((self.radius + offset) * direction)
        attack = attackClass(source, self.Dmg, direction)
        return attack

    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(self.speed)

class Player(Creature):
    def __init__(self, pos, sprite, speed):
        playerRadius = 8
        sprite = sprite
        sprite_size = (184, 184)
        max_hp = 300
        super().__init__(pos, playerRadius, sprite, sprite_size, max_hp)
        
    def needLevelUp(self):
        return self.exp >= self.expTarget
    
    """
    def setLevel(self, level):
        super().setLevel(level)
        self.exp = 0
        self.expTarget = int(self.expTargetBase * (self.levelScaleMultplier ** level))
    """

    def increaseExp(self, x):
        self.exp += x
    
    def draw(self, canvas):
        super().draw(canvas)

    def update(self):
        super().update()
        
    def movement(self, keyboard, mouse):
        if mouse.is_newpos():
            direction = self.distFromMouse(mouse)
            angleAlpha = direction.angle(Vector(1,0))
            if (angleAlpha>0.785 and angleAlpha<2.356) and (mouse.pos[1]<=self.pos.y):
                self.frame_index[0]=2
            if (angleAlpha>0.785  and angleAlpha<2.356) and (mouse.pos[1]>=self.pos.y):
                self.frame_index[0]=1
            if (angleAlpha<=0.785):
                self.frame_index[0]=3
            if (angleAlpha>=2.356):
                self.frame_index[0]=0
            

            if keyboard.up:
                self.vel.add(Vector(0, -0.75))
            if keyboard.down:
                self.vel.add(Vector(0, 0.75))
            if keyboard.right:
                self.vel.add(Vector(0.75, 0))
            if keyboard.left:
                self.vel.add(Vector(-0.75, 0))
            #if keyboard.spacebar:
            #    if self.ultcount==10:
            #        self.ulting=True
            #if self.ultOn:
            #    self.ultUpdate()
            self.attack(mouse)
            mouse.save_lastpos()
        
         #Input based movement + Sprite looking toward the direction the object is going
        else:
            if keyboard.up:
                self.vel.add(Vector(0, -0.75))
                self.frame_index[0]=2
            if keyboard.down:
                self.vel.add(Vector(0, 0.75))
                self.frame_index[0]=1
            if keyboard.right:
                self.vel.add(Vector(0.75, 0))
                self.frame_index[0]=3
            if keyboard.left:
                self.vel.add(Vector(-0.75, 0))
                self.frame_index[0]=0
            
    def pauseMove(self, room):
        wall_left = (room.getCenter().x - room.getWidth()/2)
        wall_right = room.getCenter().x + room.getWidth()/2
        wall_up = room.getCenter().y - room.getHeight()/2
        wall_down = room.getCenter().y + room.getHeight()/2

        if (self.pos.x - 5 < wall_left):
            self.pos.x = wall_left
        elif (self.pos.x + 5>= wall_right):
            self.pos.x = wall_right
        
        if (self.pos.y - 5<= wall_up):
            self.pos.y = wall_up
        elif (self.pos.y + 5>= wall_down):
            self.pos.y = wall_down
        
    def distFromMouse(self, mouse):
        mousepos = mouse.getPos()
        currpos = self.pos.get_p()
        direction = Vector(mousepos[0]-currpos[0], mousepos[1]-currpos[1])
        return direction

class Wizard(Player):
    def __init__(self, pos):
        self.sprite = "https://i.imgur.com/zOclqKw.png"
        self.speed = 0.75
        self.firespeed = 0
        self.active_projectiles = []
        self.damage = 5
        super().__init__(pos, self.sprite, self.speed)
        
    def draw(self, canvas, keyboard, mouse):
        super().movement(keyboard, mouse)
        self.update()
        super().draw(canvas)
        
    def update(self):
        super().update()

    def attack(self, mouse):
        self.firespeed += 1
        if mouse.is_newpos():
            if (self.firespeed%8==0): #Firespeed
                direction = self.distFromMouse(mouse)
                direction.normalize()
                offset = direction.copy()
                direction.multiply(5)
                currpos = self.pos.copy().add(offset.multiply(15))
                if (mouse.pos[1]>currpos.y):
                    angle = -direction.angle(Vector(-1, 0))
                else:
                    angle = (direction.angle(Vector(-1, 0)))
                fireball = Projectile(self.damage, currpos, direction, angle)
                self.active_projectiles.append(fireball)
        mouse.save_lastpos()

    def getProjectiles(self):
        return(self.active_projectiles)

    def removeProjectile(self, projectile):
        for p in self.active_projectiles:
            if(p == projectile):
                self.active_projectiles.remove(projectile)





class Enemy(Creature):
    def __init__(self, pos, radius, sprite, sprite_size, speed, base_exp, level, ideal_range, max_hp, attack_type, score):
        """
        Instantiates an Enemy class

        Keyword arguments:
        pos - a Vector object for the position of the enemy
        radius - an integer with the size of the hitbox
        sprite - a string containing a URL to a spritehseet
        speed - an ineteger with the speed of the Enemy
        base_exp - ?
        level - ?
        ideal_range - a tuple of two integers, the first being the minimum, the second being the maximum range
        """
        # Initialise Super
        super().__init__(pos, radius, sprite, sprite_size, max_hp)

        # Movement
        self.speed_multiplier = speed
        self.baseBehav = [Vector(1,0), Vector(0,-1), Vector(-1, 0), Vector(0,1)]
        self.rotation = "CW" # CW for clockwise, ACW for Anti Clockwise

        # Leveling
        self.score = randint( score[0], score[1] )
        self.base_exp = base_exp
        #self.setLevel(level)
        self.ideal_range = ideal_range

        # Counter for behaviour
        self.attack_speed = 0
        self.baseCount = 0

        # Attack type
        self.attack_type = attack_type
        self.bounce = False
        self.bounce_count = 0

    def getAttackType(self):
        return(self.attack_type)

    def isMelee(self):
        return(self.attack_type == "M")
    
    def isRanged(self):
        return(self.attack_type == "R")

    def getScore(self):
        return(self.score)

    def inRange(self, player):
        """
        Returns true if the Enemy object is in range of the player
        based on self.ideal_range, false otherwise

        Keyword arguments:
        player - the player object
        """
        direction = getDirectionTo(player)
        distance = direction.length()
        return(distance > self.ideal_range[0] and distance < self.ideal_range[1])

    def getDirectionTo(self, player):
        player_pos = player.getPos().get_p()
        this_pos = self.getPos().get_p()
        direction = Vector( player_pos[0] - this_pos[0],
                            player_pos[1] - this_pos[1] )
        return(direction)

    def facePlayer(self, player):
        direction = self.getDirectionTo(player)
        distance = direction.length()
        angleTeta = direction.angle(Vector(1,0))
        if (distance>100):
            angleAlpha = self.vel.angle(Vector(1,0))
            if (angleAlpha>0.785 and angleAlpha<2.356) and (self.vel.y<=0):
                self.frame_index[0]=2
            if (angleAlpha>0.785  and angleAlpha<2.356) and (self.vel.y>=0):
                self.frame_index[0]=1
            if (angleAlpha<=0.785):
                self.frame_index[0]=3
            if (angleAlpha>=2.356):
                self.frame_index[0]=0
        else:
            angleTeta = direction.angle(Vector(1,0))
            if (angleTeta>0.785 and angleTeta<2.356) and (direction.y<=0):
                self.frame_index[0]=2
            if (angleTeta>0.785  and angleTeta<2.356) and (direction.y>=0):
                self.frame_index[0]=1
            if (angleTeta<=0.785):
                self.frame_index[0]=3
            if (angleTeta>=2.356):
                self.frame_index[0]=0

    def movement(self, player, room):
        mvmt = self.getDirectionTo(player)
        distance = mvmt.length()
        if(self.bounce):
            mvmt.normalize()
            mvmt = -mvmt.multiply(self.speed_multiplier * 2)
            self.vel = mvmt
            self.bounce_count += 1
            if(self.bounce_count % 30 == 0):
                self.bounce = False
        if (distance > self.ideal_range[1]):
            mvmt.normalize()
            mvmt.multiply(self.speed_multiplier)
            self.vel = mvmt
        if (distance <= self.ideal_range[0]):
            mvmt = mvmt.normalize()
            mvmt = - mvmt.multiply(self.speed_multiplier)
            self.vel = mvmt
        if (distance < self.ideal_range[1] and distance > self.ideal_range[0]):
            mvmt = mvmt.normalize()
            if(room.isCollidingWall(self)):
                if(self.rotation == "CW"):
                    mvmt.rotate(90)
                    self.rotation = "ACW"
                elif(self.rotation == "ACW"):
                    mvmt.rotate_anti()
                    self.rotation = "CW"
            #mvmt = mvmt.rotate_anti()
            mvmt = mvmt.multiply(self.speed_multiplier)
            self.vel = mvmt
        self.facePlayer(player)

    def update_frameindex(self):
        self.frame_index[1] = (self.frame_index[1] + 1) % self.img_rows

    def draw(self, canvas, player, room):
        self.movement(player, room)
        self.update(player)

        self.frameclock += 1
        if (self.frameclock % self.frame_duration == 0):
            self.update_frameindex()
        
        frame_centre = (self.frame_width * self.frame_index[0] + self.frame_centre_x, self.frame_height * self.frame_index[1] + self.frame_centre_y)
        frame_size = (self.frame_width, self.frame_height)
        canvas.draw_image(self.spritesheet, frame_centre, frame_size, self.pos.get_p(), frame_size)

    """
    def setLevel(self, level):
        super().setLevel(level)
        expModifier = 1.08
        self.exp = self.base_exp * (expModifier**self.level)
    """
        
    def update(self, player):
        self.pos.add(self.vel)
        self.vel.multiply(0.75)
        self.attack(player)

class Goblin(Enemy):
    def __init__(self, pos, radius, sprite, speed, level, ideal_range, max_hp, attack_type, score):
        base_exp = 5
        sprite_size = (184, 184)
        super().__init__(pos, radius, sprite, sprite_size, speed, base_exp, level, ideal_range, max_hp, attack_type, score)

class DaggerGoblin(Goblin):
    def __init__(self, pos):
        radius = 8 # 8 pixel radius
        spritesheet = "https://i.imgur.com/zN5kluE.png"
        speed = 2
        ideal_range = (0, 5)
        max_hp = 15
        attack_type = "M"
        self.damage = 3
        score = (10, 20)
        super().__init__(pos, radius, spritesheet, speed, 1, ideal_range, max_hp, attack_type, score)

    def attack(self, player):
        self.attack_speed += 1
        direction = self.getDirectionTo(player)
        distance = direction.length()
        if (distance < 5):
            self.bounce = True
            player.take_damage(self.damage)

class MageGoblin(Goblin):
    def __init__(self, pos):
        radius = 8 # 8 pixel radius
        spritesheet = "https://i.imgur.com/nAA2riI.png"
        speed = 1.5
        ideal_range = (90, 100)
        max_hp = 15
        attack_type = "R"
        self.active_projectiles = []
        score = (5, 10)
        super().__init__(pos, radius, spritesheet, speed, 1, ideal_range, max_hp, attack_type, score)

    def attack(self, player):
        self.attack_speed += 1
        direction = self.getDirectionTo(player)
        distance = direction.length()
        if (distance<170):
            if (self.attack_speed % 20 == 0):

                direction.normalize()
                offset = direction.copy()
                direction.multiply(4)
                aim = self.pos.copy().add(offset.multiply(15))

                if (player.getPos().y > self.getPos().y):
                    angle = -direction.angle(Vector(-1, 0))
                else:
                    angle = (direction.angle(Vector(-1, 0)))
                fireball = EnemyProjectile(aim, direction, angle)
                self.active_projectiles.append(fireball)
    
    def getProjectiles(self):
        return(self.active_projectiles)

    def removeProjectile(self, projectile):
        for p in self.active_projectiles:
            if(p == projectile):
                self.active_projectiles.remove(projectile)

class Zombie(Enemy):
    def __init__(self, pos):
        radius = 8 # 8 pixel radius
        spritesheet = "https://i.imgur.com/8We82gB.png"
        sprite_size = (128, 128)
        speed = 1
        ideal_range = (0, 5)
        max_hp = 30
        attack_type = "M"
        self.damage = 10
        score = (10, 20)
        super().__init__(pos, radius, spritesheet, sprite_size, speed, 1, 1, ideal_range, max_hp, attack_type, score)

    def attack(self, player):
        self.attack_speed += 1
        direction = self.getDirectionTo(player)
        distance = direction.length()
        if (distance < 5):
            self.bounce = True
            player.take_damage(self.damage)

class Dragon(Enemy):
    def __init__(self, pos):
        radius = 10
        spritesheet = "https://i.imgur.com/bbjre9N.png"
        sprite_size = (192, 192)
        speed = 0.75
        ideal_range = (120, 200)
        max_hp = 50
        attack_type = "R"
        self.active_projectiles = []
        score = (100, 100)
        super().__init__(pos, radius, spritesheet, sprite_size, speed, 1, 1, ideal_range, max_hp, attack_type, score)

    def attack(self, player):
        self.attack_speed += 1
        direction = self.getDirectionTo(player)
        distance = direction.length()
        if (distance < 220):
            if (self.attack_speed % 10 == 0):

                direction.normalize()
                offset = direction.copy()
                direction.multiply(4)
                aim = self.pos.copy().add(offset.multiply(15))

                if (player.getPos().y > self.getPos().y):
                    angle = -direction.angle(Vector(-1, 0))
                else:
                    angle = (direction.angle(Vector(-1, 0)))
                fireball = EnemyProjectile(aim, direction, angle)
                self.active_projectiles.append(fireball)
    
    def getProjectiles(self):
        return(self.active_projectiles)

    def removeProjectile(self, projectile):
        for p in self.active_projectiles:
            if(p == projectile):
                self.active_projectiles.remove(projectile)