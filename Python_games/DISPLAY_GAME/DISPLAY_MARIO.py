        #DISPLAY MARIO
import pygame
pygame.init()

#----------------CONFIGURATIONS-------------
MAX_X=1280
MAX_Y=720
IMAGE_X=550
IMAGE_Y=300
SCALE_X=70
SCALE_Y=90
BACKGROUND_COLOR=(0,0,0)
#-----------------DISPLAY------------------

SCREEN=pygame.display.set_mode((MAX_X,MAX_Y))
pygame.display.set_caption("IMAGE GAME V1.0")
MARIO=pygame.image.load("Mario.png").convert()
MARIO=pygame.transform.scale(MARIO,(SCALE_X,SCALE_Y))

#------------MAIN GAME LOOP----------------
GAME_OVER=False
while GAME_OVER==False:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                GAME_OVER=True
            if event.key==pygame.K_UP:
                IMAGE_Y-=10
            if event.key==pygame.K_DOWN:
                IMAGE_Y+=10
            if event.key==pygame.K_LEFT:
                IMAGE_X-=10
            if event.key==pygame.K_RIGHT:
                IMAGE_X+=10
        if event.type==pygame.MOUSEBUTTONDOWN:
            IMAGE_X,IMAGE_Y=event.pos
    SCREEN.fill(BACKGROUND_COLOR)
    SCREEN.blit(MARIO,(IMAGE_X,IMAGE_Y))
    pygame.display.flip()
