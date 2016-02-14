import pygame
screen=pygame.display.set_mode((1080,640))
from pygame.locals import*
pygame.display.set_caption('Street Fighter')
from streetfighterclass import Sfighter
S1=Sfighter()
clock=pygame.time.Clock()
x=0
r=0
p=0
s=0
c=0
d=0
f=0
q=0
t=0
while True:
    clock.tick(5)
    pygame.display.update()
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_d:
                r=1
            if event.key==K_e:
                p=1
            if event.key==K_SPACE:
                s=1
            if event.key==K_f:
                f=1
            if event.key==K_q:
                q=1
            if event.key==K_t:
                t=1
        if event.type==KEYUP:
            if event.key==K_d:
                r=0
            if event.key==K_e:
                p=0
            if event.key==K_SPACE:
                s=0
            if event.key==K_f:
                f=0
            if event.key==K_q:
                q=0
            if event.key==K_t:
                t=0
    if r==1:
        S1.Move(screen,S1.RunForward)
    elif p==1:
        S1.Spritecount=0
        S1.Move(screen,S1.Punch)        
    elif s==1:
        S1.Spritecount=0
        S1.Move(screen,S1.Jump)
    elif f==1:
        S1.Spritecount=0
        S1.Move(screen,S1.Duck)
    elif q==1:
        S1.Spritecount=0
        S1.Move(screen,S1.Slide)
    elif t==1:
        S1.Spritecount=0
        S1.Move(screen,S1.SpecialMove)
    else:
        screen.blit(S1.l[0],(540,320))

