import pygame
from pygame.locals import *
from random import randint
from time import sleep
import sys
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((640,640))
foodx=(randint(10,630) // 10)*10
foody=(randint(10,630) // 10)*10
snakex=(randint(10,630) // 10)*10
snakey=(randint(10,630) // 10)*10
pygame.display.set_caption('Snake')
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
up=0
down=0
left=0
right=0
score=0
snakelist=[]
snakelength=0
def snakebody():
    for snake in snakelist:
        pygame.draw.rect(screen,green,(snake[0],snake[1],10,10),5)
def show_text(msg,x,y,color):
    fontobj= pygame.font.SysFont('comicsans',20)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
while True:
    clock.tick(20)
    pygame.display.update()
    screen.fill((0,0,0))
    snakehead=[]
    snakehead.append(snakex)
    snakehead.append(snakey)
    snakelist.append(snakehead)
    if len(snakelist) > snakelength:
        del snakelist[0]
    snakebody()
    pygame.draw.rect(screen,red,(foodx,foody,10,10),5)
    pygame.draw.rect(screen,green,(snakex,snakey,10,10),5)
    show_text('Your score is:',460,5,blue)
    show_text(str(score),550,5,blue)
    if up==1:
        snakey=snakey-10
    if down==1:
        snakey=snakey+10
    if left==1:
        snakex=snakex-10
    if right==1:
        snakex=snakex+10
    #print(up,down,left,right)
    if (foodx,foody)==(snakex,snakey):
        print('collision')
        foodx=(randint(10,630) // 10)*10
        foody=(randint(10,630) // 10)*10
        score=score+1
        snakelength=snakelength+1
    print(snakelist)
    if 0>snakex or 640<snakey or 640<snakex or 0>snakey:
        print('YOu lost the game')
        sleep(2)
        pygame.quit()
        sys.exit()
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_w and down==0:
                up=1
                down=0
                left=0
                right=0
            if event.key==K_s and up==0:
                down=1
                up=0
                right=0
                left=0
            if event.key==K_a and right==0:
                left=1
                down=0
                up=0
                right=0
            if event.key==K_d and left==0:
                right=1
                up=0
                down=0
                left=0
        if event.type==QUIT:
            pygame.quit()
            exit()
