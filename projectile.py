from settings import *
import pygame as pg
from main import *
class Projectile:
    def __init__(self,game,x,y,radius,color,xDirection,yDirection,speed):
        self.game = game
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.xDirection = xDirection
        self.yDirection = yDirection
        self.speed = speed
        self.duration = 100

    def draw(self):
        pg.draw.circle(self.game.screen, self.color, (self.x*100,self.y*100), self.radius)


    def update(self):
        self.move()
    def move(self):
        self.x += self.xDirection*self.speed
        self.y += self.yDirection*self.speed
        self.duration -= 1