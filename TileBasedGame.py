import pygame
from pygame.locals import *

playerAnimationStep = 1

pygame.display.set_caption("Tile Based Game")
screen = pygame.display.set_mode((640, 640))



class Tile(pygame.sprite.Sprite):
    def __init__(self, tileType):
        super(Tile, self).__init__()
        self.image = pygame.transform.scale(pygame.image.load("./textures/tiles/"+tileType+".png"), (64, 64))
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.transform.scale(pygame.image.load("./textures/sprites/player/resting/1.png"), (64, 128))
        self.drawrect = self.image.get_rect()
        self.hitrect = pygame.Rect(0,0,64,64)

        self.resting1 = pygame.transform.scale(pygame.image.load("./textures/sprites/player/resting/1.png"), (64, 128))
        self.resting2 = pygame.transform.scale(pygame.image.load("./textures/sprites/player/resting/2.png"), (64, 128))
        self.resting3 = pygame.transform.scale(pygame.image.load("./textures/sprites/player/resting/3.png"), (64, 128))
        self.frameCounter = 0

    def drawboxRealign(self):
        self.drawrect.bottom = self.hitrect.bottom
        self.drawrect.left = self.hitrect.left

    def move(self, pressedKeys):
        if pressedKeys[K_w]:
            self.hitrect.move_ip(0,-1)
        if pressedKeys[K_s]:
            self.hitrect.move_ip(0,1)
        if pressedKeys[K_a]:
            self.hitrect.move_ip(-1,0)
        if pressedKeys[K_d]:
            self.hitrect.move_ip(1,0)

    def animate(self, animationMode):
        global playerAnimationStep
        if animationMode == "resting":
            if self.frameCounter == 0:
                if playerAnimationStep == 1:
                    self.image = self.resting1
                    playerAnimationStep += 1
                elif playerAnimationStep == 2:
                    self.image = self.resting2
                    playerAnimationStep += 1
                elif playerAnimationStep == 3:
                    self.image = self.resting3
                    playerAnimationStep = 1
            self.frameCounter += 1
            if self.frameCounter == 120:
                self.frameCounter = 0



tileMap = [["d","dd","dd","dd","dd","dd","dd","dd","dd","d"],
           ["dr","g","g","g","g","g","g","g","g","dl"],
           ["dr","g","g","g","g","g","g","g","g","dl"],
           ["dr","g","g","g","g","g","g","g","g","dl"],
           ["dr","g","g","g","dul","dur","g","g","g","dl"],
           ["dr","g","g","g","ddl","ddr","g","g","g","dl"],
           ["dr","g","g","g","g","g","g","g","g","dl"],
           ["dr","g","g","g","g","g","g","g","g","dl"],
           ["dr","g","g","g","g","g","g","g","g","dl"],
           ["d","du","du","du","du","du","du","du","du","d"]]



tileMapDraw = []
rowCounter = 0
for row in tileMap:
    for tile in range(len(row)):
        if row[tile] == "g":
            tileType = "GrassCenter"
        elif row[tile] == "dudlr":
            tileType = "DirtUDLR"
        elif row[tile] == "d":
            tileType = "Dirt"
        elif row[tile] == "du":
            tileType = "DirtU"
        elif row[tile] == "dd":
            tileType = "DirtD"
        elif row[tile] == "dl":
            tileType = "DirtL"
        elif row[tile] == "dr":
            tileType = "DirtR"
        elif row[tile] == "dul":
            tileType = "DirtUL"
        elif row[tile] == "dur":
            tileType = "DirtUR"
        elif row[tile] == "ddl":
            tileType = "DirtDL"
        elif row[tile] == "ddr":
            tileType = "DirtDR"
        tileObj = Tile(tileType)
        tileObj.rect.center = ((64*(tile+1))-32,(64*(rowCounter+1))-32)
        tileMapDraw.append(tileObj)
    rowCounter += 1



player = Player()
player.hitrect.center = (32,32)



gameloop = True
while gameloop:
    screen.fill((0,0,0))

    for _ in range(0,10*10):
        screen.blit(tileMapDraw[_].image, tileMapDraw[_].rect)

    player.drawboxRealign()
    player.animate("resting")
    screen.blit(player.image, player.drawrect)

    pygame.display.flip()

    player.move(pygame.key.get_pressed())

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                gameloop = False
        elif event.type == QUIT:
            pygame.quit()
            gameloop = False