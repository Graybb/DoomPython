import pygame as pg
import sys
from settings import *
from map import *
from player import *



class Game:
    def __init__(self):
        pg.init
        
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        pg.mouse.set_visible(False)
        self.new_game()
        

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.projList = []

    def update(self):
        self.player.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')
        self.updateProjectiles()

    def updateProjectiles(self):
        for projectile in self.projList:
            projectile.update()
            if projectile.duration == 0:
                self.projList.pop(self.projList.index(projectile))

    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()
        for x in self.projList:
            x.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()
        