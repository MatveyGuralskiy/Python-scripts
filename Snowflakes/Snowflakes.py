            #Snowflakes
import pygame
import sys
import time
import random
#--------------Snow Variables------------
MAX_X=1920
MAX_Y=1080
MAX_SNOW=200
SNOW_SIZE=50

#--------------Class with methods---------
class Snow():
    """Snowflakes class"""


    def __init__(self,X,Y):
        """Configurations of snow images"""
        self.X=X
        self.Y=Y
        self.SPEED=random.randint(1,3)
        self.IMAGE_NUM=random.randint(1,4)
        self.IMAGE_NAME="SNOW"+str(self.IMAGE_NUM)+".png"
        self.IMAGE=pygame.image.load(self.IMAGE_NAME).convert_alpha()
        self.IMAGE=pygame.transform.scale(self.IMAGE,(SNOW_SIZE,SNOW_SIZE))

    def MOVE_SNOW(self):
        """Moving of snow directions"""
        self.Y+=self.SPEED
        if self.Y>MAX_Y:    #Move down
            self.Y=(0-SNOW_SIZE)
        MOVE=random.randint(1,3)
        if MOVE==1:         #Move right
            self.X+=1
            if self.X>MAX_X:
                self.X=(0-SNOW_SIZE)
        elif MOVE==2:       #Move left
            self.X-=1
            if self.X<(0-SNOW_SIZE):
                self.X=MAX_X


    def DRAW_SNOW(self):
        """Where to draw the snowflakes"""
        SCREEN.blit(self.IMAGE,(self.X,self.Y))


def INITIALIZE_RANDOM_SNOW(MAX_SNOW,SNOWFALL):
    """Initialized snow and gives them random place"""
    for MOVE in range(0,MAX_SNOW):
        RANDOM_X=random.randint(0,MAX_X)
        RANDOM_Y=random.randint(0,MAX_Y)
        SNOWFALL.append(Snow(RANDOM_X,RANDOM_Y))


def CHECK_EXIT():
    """How to exit"""
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                sys.exit()
            
    
#----------------Main Init--------------------
pygame.init()
SCREEN=pygame.display.set_mode((MAX_X,MAX_Y),pygame.FULLSCREEN)
BACKGROUND_COLOR=(0,0,0)
SNOWFALL=[]
INITIALIZE_RANDOM_SNOW(MAX_SNOW,SNOWFALL)
while True:
    SCREEN.fill(BACKGROUND_COLOR)
    CHECK_EXIT()
    for MOVE in SNOWFALL:
        MOVE.MOVE_SNOW()
        MOVE.DRAW_SNOW()
    time.sleep(0.0005)
    pygame.display.flip()
    