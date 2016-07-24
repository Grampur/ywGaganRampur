import pygame
from pygame.locals import *
from random import randint
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((640,640))
foodx=(randint(0,640) // 10)*10
foody=(randint(0,640) // 10)*10
snakex=(randint(0,640) // 10)*10
snakey=(randint(0,640) // 10)*10
pygame.display.set_caption('Snake')
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
up=0
down=0
left=0
right=0
while True:
    clock.tick(50)
    pygame.display.update()
    screen.fill((0,0,0))
    pygame.draw.rect(screen,red,(foodx,foody,10,10),5)
    pygame.draw.rect(screen,green,(snakex,snakey,10,10),5)
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
        foodx,foody=randint(0,640) // 10)*10
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_w:
                up=1
                down=0
                left=0
                right=0
            if event.key==K_s:
                down=1
                up=0
                right=0
                left=0
            if event.key==K_a:
                left=1
                down=0
                up=0
                right=0
            if event.key==K_d:
                right=1
                up=0
                down=0
                left=0
        if event.type==QUIT:
            pygame.quit()
            exit()
