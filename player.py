from settings import *
import pygame as pg
from projectile import *
import math
class Player:
    def __init__(self,game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.projectileSpeedModifier = 1
        self.cooldownCount = 0
    
    def action(self):
        speed = self.projectileSpeedModifier
        speed_y = speed*0
        speed_x = speed*1
        keys=  pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.cooldown()
            self.game.projList.append(Projectile(self.game,self.x, self.y, 10, 'blue', speed_y,-speed_x, PROJECTILE_SPEED*self.projectileSpeedModifier))
        elif keys[pg.K_DOWN]:
            self.cooldown()
            self.game.projList.append(Projectile(self.game,self.x, self.y, 10, 'blue', -speed_y,speed_x, PROJECTILE_SPEED*self.projectileSpeedModifier))
        elif keys[pg.K_LEFT]:
            self.cooldown()
            self.game.projList.append(Projectile(self.game,self.x, self.y, 10, 'blue', -speed_x,-speed_y, PROJECTILE_SPEED*self.projectileSpeedModifier))
        elif keys[pg.K_RIGHT]:
           self.cooldown()
           self.game.projList.append(Projectile(self.game,self.x,self.y, 10, 'blue', speed_x,speed_y, PROJECTILE_SPEED*self.projectileSpeedModifier))
        elif keys[pg.K_SPACE]:
           self.cooldown()
           None

    def movement(self):
        dx,dy = 0,0
        speed = PLAYER_SPEED*self.game.delta_time
        speed_y = speed*0
        speed_x = speed*1
        keys=  pg.key.get_pressed()
        if keys[pg.K_d]:
            dx += speed_x
            dy += speed_y
        if keys[pg.K_a]:
            dx += -speed_x
            dy += -speed_y
        if keys[pg.K_w]:
            dx += speed_y
            dy += -speed_x
        if keys[pg.K_s]:
            dx += -speed_y
            dy += speed_x
        

        self.check_wall_collision(dx,dy)
        #if keys[pg.K_LEFT]:
        #    self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        #if keys[pg.K_RIGHT]:
        #    self.angle += PLAYER_ROT_SPEED * self.game.delta_time

    def check_wall(self,x,y):
        return (x,y) not in self.game.map.world_map
    
    def check_wall_collision(self,dx,dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x+dx*scale),int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x),int(self.y+dy*scale)):
            self.y += dy

    def draw(self):
        #pg.draw.line(self.game.screen, 'yellow', (self.x*100,self.y*100),
        #            (self.x*100+WIDTH*math.cos(self.angle),
        #             self.y*100+WIDTH*math.sin(self.angle)),2)
        pg.draw.circle(self.game.screen,'green',(self.x*100,self.y*100),15)
        



    def cooldown(self):
        self.cooldownCount += 15
    def reduceCooldown(self,amount):
        self.cooldownCount -=amount

    def update(self):
        self.movement()
        if(self.cooldownCount == 0):
            self.action()
        else:
            self.reduceCooldown(1)

    @property
    def pos(self):
        return self.x,self.y
    

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
    
