        #DISPLAY MARIO
import pygame
pygame.init()

#----------------CONFIGURATIONS-------------
MAX_X=1280
MAX_Y=720
IMAGE_X=550
IMAGE_Y=300
SIZE=80
BACKGROUND_COLOR=(0,0,0)
MOVE_R=False
MOVE_L=False
MOVE_UP=False
MOVE_DOWN=False
GAME_OVER=False
#-----------------DISPLAY------------------

SCREEN=pygame.display.set_mode((MAX_X,MAX_Y))
pygame.display.set_caption("IMAGE GAME V1.0")
MARIO=pygame.image.load("Mario.png").convert()
MARIO=pygame.transform.scale(MARIO,(SIZE,SIZE))

#------------MAIN GAME LOOP----------------

while GAME_OVER==False:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                GAME_OVER=True

            if event.key==pygame.K_UP:
                MOVE_UP=True
            if event.key==pygame.K_DOWN:
                MOVE_DOWN=True
            if event.key==pygame.K_LEFT:
                MOVE_L=True
            if event.key==pygame.K_RIGHT:
                MOVE_R=True

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_ESCAPE:
                GAME_OVER=False
            if event.key==pygame.K_UP:
                MOVE_UP=False
            if event.key==pygame.K_DOWN:
                MOVE_DOWN=False
            if event.key==pygame.K_LEFT:
                MOVE_L=False
            if event.key==pygame.K_RIGHT:
                MOVE_R=False

        if event.type==pygame.MOUSEBUTTONDOWN:
            IMAGE_X,IMAGE_Y=event.pos
    if MOVE_UP==True:
        IMAGE_Y-=1
        if IMAGE_Y<0:
            IMAGE_Y=0
    if MOVE_DOWN==True:
        IMAGE_Y+=1
        if IMAGE_Y>MAX_Y-SIZE:
            IMAGE_Y=MAX_Y-SIZE
    if MOVE_L==True:
        IMAGE_X-=1
        if IMAGE_X<0:
            IMAGE_X=0
    if MOVE_R==True:
        IMAGE_X+=1
        if IMAGE_X>MAX_X-SIZE:
            IMAGE_X=MAX_X-SIZE


    SCREEN.fill(BACKGROUND_COLOR)
    SCREEN.blit(MARIO,(IMAGE_X,IMAGE_Y))
    pygame.display.flip()
