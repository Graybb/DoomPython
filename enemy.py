from settings import*
import pygame as pg
class Enemy:
    def __init__(self,game, x, y, radius = 15, health= 10):
        self.game = game
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = PLAYER_SPEED
        self.health = health

    def move(self, targetX,targetY):
        self.x += targetX*self.speed
        self.y += targetY*self.speed
    def checkMovement(self):
        if(self.playerIsWithinThreeTiles):
            self.moveToPlayer()
        else:
            self.randomMovement()
    def playerIsWithinThreeTiles(self):
        playerX,playerY = self.game.getPlayerPos()
        return False
    def moveToPlayer(self):
        targetX,targetY = self.game.getPlayerPos()
        self.move(targetX,targetY)
    def update(self):
        #self.checkMovement()
        self.draw()
    def draw(self):
        pg.draw.circle(self.game.screen,'red',(self.x*100,self.y*100),self.radius)
    
    def randomMovement(self):
        self.move(1,1)
