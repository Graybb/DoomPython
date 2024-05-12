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
        self.collided = False
        self.damage = game.player.damageScale*PLAYER_BASE_DAMAGE

    def draw(self):
        pg.draw.circle(self.game.screen, self.color, (self.x*100,self.y*100), self.radius)


    def update(self):
        self.move()
    def move(self):
        dx = self.xDirection*self.speed
        dy = self.yDirection*self.speed
        self.duration -= 1
        self.check_wall_collision(dx,dy)

    def check_wall(self,x,y):
        return (x,y) not in self.game.map.world_map
    
    def check_wall_collision(self,dx,dy):
        #Not completly implemented, it gives errors in tight areas
        self.x += dx
        self.y += dy
        