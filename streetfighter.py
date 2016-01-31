import pygame
screen=pygame.display.set_mode((1080,640))
from pygame.locals import*
pygame.display.set_caption('Street Fighter')
from streetfighterclass import Sfighter
'''img0=pygame.image.load('images/p0.png')
img1=pygame.image.load('images/p1.png')
img2=pygame.image.load('images/p2.png')
img3=pygame.image.load('images/p3.png')
img4=pygame.image.load('images/p4.png')

l=[img0,img1,img2,img3,img4]'''
'''l=[]
Jump=[]
RunForward=[]
Punch=[]
Duck=[]
Slide=[]
SpecialMove=[]
for a in range(0,19,1):
    l.append(pygame.transform.scale(pygame.image.load('images/p'+str(a)+'.png'),(100,100)))
    if a==7 or a==18:
        Punch.append(pygame.transform.scale(pygame.image.load('images/p'+str(a)+'.png'),(100,100)))
    if a==6:
        Jump.append(pygame.transform.scale(pygame.image.load('images/p'+str(a)+'.png'),(100,100)))
    if a==3 or a==4 or a==5:
        RunForward.append(pygame.transform.scale(pygame.image.load('images/p'+str(a)+'.png'),(100,100)))    
    if a==9:
        Duck.append(pygame.transform.scale(pygame.image.load('images/p'+str(a)+'.png'),(100,100)))    
    if a==8:
        Slide.append(pygame.transform.scale(pygame.image.load('images/p'+str(a)+'.png'),(100,100)))
    if a==10:
        SpecialMove.append(pygame.transform.scale(pygame.image.load('images/p'+str(a)+'.png'),(100,100)))

'''
x=0
r=0
p=0
s=0
c=0
d=0
f=0
q=0
t=0

S1=Sfighter()

clock=pygame.time.Clock()
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
                print('"Run or D" key pressed')
                r=1
            if event.key==K_e:
                print('"Punch or E" key pressed')
                p=1
            if event.key==K_SPACE:
                print('"Jump or SPACEBAR" key pressed')
                s=1
            if event.key==K_f:
                print('"Duck or F" key pressed')
                f=1
            if event.key==K_q:
                print('"Slide or q" is pressed')
                q=1
            if event.key==K_t:
                print('"SpecialMove or t" is pressed')
                t=1
            if event.key==K_UP:
              print ('"Up" arrow" key pressed')
        if event.type==KEYUP:
            if event.key==K_d:
                print('"Run or D" key pressed')
                r=0
            if event.key==K_e:
                print('"Punch or E" key pressed')
                p=0
            if event.key==K_SPACE:
                print('"Jump or SPACEBAR" key pressed')
                s=0
            if event.key==K_f:
                print('"Duck or F" key pressed')
                f=0
            if event.key==K_q:
                print('"Slide or q" is pressed')
                q=0
            if event.key==K_t:
                print('"SpecialMove or t" is pressed')
                t=0
            if event.key==K_UP:
              print('"Up arrow" key pressed')
    if r==1:
        S1.Move(screen,S1.RunForward)
        '''print(x)
        screen.blit(RunForward[x],(540,320))
        x=x+1
        if x>=3:
            x=0
            print(x)'''
    elif p==1:
        S1.Move(screen,S1.Punch)        
        '''print(Punch)
        screen.blit(Punch[x],(540,320))
        x=x+1
        if x>=2:
            x=0'''
    elif s==1:
        S1.Move(screen,S1.Jump)
        '''screen.blit(Jump[0],(540,320))
        x=x+1
        if x>=1:
        x=0
        print(Jump,x)'''
    elif f==1:
        S1.Move(screen,S1.Duck)
        '''print(x)
        screen.blit(Duck[0],(540,320))
        x=x+1
        if x>=1:
        x=0'''
    elif q==1:
        S1.Move(screen,S1.Slide)
        '''screen.blit(Slide[0],(540,320))
        x=x+1
        if x>=1:
        x=0'''
    elif t==1:
        S1.Move(screen,S1.Slide)
        '''print(0)
        screen.blit(SpecialMove[0],(540,320))
        x=x+1
        if x>=1:
        x=0'''
    else:
        screen.blit(S1.l[0],(540,320))

