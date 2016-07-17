import pygame
pygame.display.locals import *
from random import randint
pygame.init()
screen.pygame.display.set.mode((640,1080))
foodx=randint((1,10))
foody=randint((1,10))
snakex=(random.randint(0,640) // 10)*10
snakey=(random.randint(0,640) // 10)*10
while True:
    pygame.display.update()
    pygame.display.set_caption('Snake')
    pygaem.draw.rect(screen,red,(50,50,10,10),5)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
