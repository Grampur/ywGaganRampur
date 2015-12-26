import pygame
screen=pygame.display.set_mode((1080,640))
from pygame.locals import*
pygame.display.set_caption('Street Fighter')
'''img0=pygame.image.load('images/p0.png')
img1=pygame.image.load('images/p1.png')
img2=pygame.image.load('images/p2.png')
img3=pygame.image.load('images/p3.png')
img4=pygame.image.load('images/p4.png')

l=[img0,img1,img2,img3,img4]'''
l=[]
for a in range(0,18,1):
    l.append(pygame.transform.scale(pygame.image.load('images/p'+str(a)+'.png'),(100,100)))
x=0
clock=pygame.time.Clock()
while True:
    clock.tick(5)
    pygame.display.update()
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
    screen.blit(l[x],(540,320))
    x=x+1
    if x>=18:
        x=0
