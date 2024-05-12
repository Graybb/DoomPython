from settings import*
import random
import pygame as pg
class Enemy:
    def __init__(self,game, x, y, radius = 15, health= 10):
        self.game = game
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = ENEMY_SPEED*2
        self.health = health
        self.xDirection = 0
        self.yDirection = 0
        self.moveUntilDirectionChange = 60
        self.colour = 'red'

    def move(self, targetX,targetY):
        dx = targetX*self.speed
        dy = targetY*self.speed
        self.check_wall_collision(dx,dy)

    def check_wall(self,x,y):
        return (x,y) not in self.game.map.world_map
    
    def check_wall_collision(self,dx,dy):
        scale = ENEMY_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x+dx*scale),int(self.y)):
            self.x += dx
        else: self.xDirection = self.xDirection*-1
        if self.check_wall(int(self.x),int(self.y+dy*scale)):
            self.y += dy
        else: self.yDirection = self.yDirection*-1

    def checkMovement(self):
        self.randomMovement()
    def playerIsWithinThreeTiles(self):
        playerX,playerY = self.game.getPlayerPos()
        return False
    def moveToPlayer(self):
        targetX,targetY = self.game.getPlayerPos()
        self.move(targetX,targetY)
    def update(self):
        self.checkMovement()
        #self.draw()
    def collidesWithProjectile(self, projList):
        scale = ENEMY_SIZE_SCALE
        for projectile in projList:
            if (abs(projectile.x - self.x)*100) <= self.radius*1.2 and (abs(projectile.y - self.y)*100) <= self.radius*1.2 :
                self.health -= 1
                if self.health == 5: self.colour ="yellow"
                if self.health == 0 :
                    return True
        return False
    
    def draw(self):
        pg.draw.circle(self.game.screen,self.colour,(self.x*100,self.y*100),self.radius)
    
    def randomMovement(self):
        if self.moveUntilDirectionChange == 0:
            self.moveUntilDirectionChange = 60
            self.xDirection=random.randrange(-1,2)
            self.yDirection=random.randrange(-1,2)
        else:
            self.moveUntilDirectionChange -= 1
        
        self.move(self.xDirection,self.yDirection)

        
