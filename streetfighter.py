import pygame
screen=pygame.display.set_mode((1080,640))
from pygame.locals import*
pygame.display.set_caption('Street Fighter')
from streetfighterclass import Sfighter
S1=Sfighter('p',140,240)
S2=Sfighter('pD',780,240)
clock=pygame.time.Clock()
Background=pygame.transform.scale(pygame.image.load('images/SR6.gif'),1080,640)
#####################################
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
######################################
k=0
j=0
l=0
m=0
while True:
    clock.tick(5)
    pygame.display.update()
    screen.fill((0,0,0))
    screen.blit(Background,(0,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_d:
                a=1
            if event.key==K_e:
                b=1
            if event.key==K_SPACE:
                e=1
            if event.key==K_f:
                f=1
            if event.key==K_w:
                g=1
            if event.key==K_r:
                h=1
            if event.key==K_k:
                k=1
            if event.key==K_j:
                j=1
            if event.key==K_l:
                l=1
            if event.key==K_m:
                m=1
        if event.type==KEYUP:
            if event.key==K_d:
                a=0
            if event.key==K_e:
                b=0
            if event.key==K_SPACE:
                e=0
            if event.key==K_f:
                f=0
            if event.key==K_w:
                g=0
            if event.key==K_r:
                h=0
            if event.key==K_k:
                k=0
            if event.key==K_j:
                j=0
            if event.key==K_l:
                l=0
            if event.key==K_m:
                m=0
    if a==1:
        S1.Move(screen,S1.RunForward)
    elif b==1:
        S1.Spritecount=0 
        S1.Move(screen,S1.Punch)        
    elif e==1:
        S1.Spritecount=0
        S1.Move(screen,S1.Jump)
    elif f==1:
        S1.Spritecount=0
        S1.Move(screen,S1.Duck)
    elif g==1:
        S1.Spritecount=0
        S1.Move(screen,S1.Slide)
    elif h==1:
        S1.Spritecount=0
        S1.Move(screen,S1.SpecialMove)
    else:
        screen.blit(S1.l[0],(140,240))
    if k==1:
        #S2.Spritecount=0
        S2.Move(screen,S2.Jump)
    elif j==1:
        #S2.Spritecount=0
        print(S2.RunForward)
        S2.Move(screen,S2.RunForward)
    elif l==1:
        #S2.Spritecount=0
        S2.Move(screen,S2.Duck)
    elif m==1:
        #S2.Spritecount=0
        S2.Move(screen,S2.SpecialMove)
    else:
        screen.blit(S2.l[0],(780,240))
