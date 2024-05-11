from settings import*
class Enemy:
    def __init__(self,game, x, y, width, height, health= 10):
        self.game = game
        self.x = x
        self.y = y
        self.width = width
        self.height = height
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

    def randomMovement(self):
        self.move(1,1)
