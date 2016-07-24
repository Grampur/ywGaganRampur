import pygame
from pygame.locals import *
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption('Menu')
pygame.init()
fpsClock=pygame.time.Clock()
#COLOR GROUP
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
def button(msg,ic,ac,x,y,w,h,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed() 
    if x+w > mouse[0]>x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h)) 
    show_text( msg, blue,x+w/2,y+h/2)
def show_text(msg,color,x,y):
    fontobj= pygame.font.SysFont('comicsans',20)
    msgobj = fontobj.render(msg,False,color)
    a,b,w,h=msgobj.get_rect()
    screen.blit(msgobj,(x-w/2,y-h/2))
def game1player():
    from random import randint
    from time import sleep
    screen=pygame.display.set_mode((640,480))
    pygame.display.set_caption('Ping Pong!')
    pygame.init()
    leftpaddlex=150
    leftpaddley=300
    rightpaddlex=450
    rightpaddley=350
    r_pad_up=0
    r_pad_down=0
    l_pad_up=0
    l_pad_down=0
    pspeed=3.5
    circlex=310
    circley=280
    red=(255,0,0)
    green=(0,255,0)
    blue=(0,0,255)
    white=(255,255,255)
    black=(0,0,0)
    screen.fill(white)
    speedx=2
    speedy=0
    scoreleft=0
    scoreright=0
    def show_text(msg,x,y,color):
        fontobj=pygame.font.SysFont('freesans',32)
        msgobj=fontobj.render(msg,False,color)
        screen.blit(msgobj,(x,y))
    while True:    
        pygame.display.update()
        fpsClock.tick(120)
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(0,12,113),(120,60,400,400))
        pygame.draw.circle(screen,white,(circlex,circley),5,3)
        pygame.draw.line(screecolorn,green,(leftpaddlex,leftpaddley),(leftpaddlex,leftpaddley+80),3)
        pygame.draw.line(screen,green,(rightpaddlex,rightpaddley),(rightpaddlex,rightpaddley+80),3)
        show_text('The Score is',210,5,red)
        show_text(str(scoreleft)+'-'+str(scoreright),277,29,red)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            elif event.type==KEYDOWN:
                if event.key==colorK_DOWN:
                    r_pad_down=1
                elif event.key==K_UP:
                    r_pad_up=1
            elif event.type==KEYUP:
                if event.key==K_DOWN:
                    r_pad_down=0
                elif event.key==K_UP:
                    r_pad_up=0
        circlex=circlex+speedx
        circley=circley+speedy
        if circlex==rightpaddlcolorex and rightpaddley<=circley<=(rightpaddley+70):
            speedx=-speedx
            speedy=randint(-1,1 )
        if circlex==leftpaddlex and leftpaddley<=circley<=(leftpaddley+70):
            speedx=-speedx
        if circley<=60:
            speedy=-speedy
        if circley>=450:
            speedy=-speedy
        if circlex>=520:
            circlex=310
            scoreleft=scoreleft+1
        if circlex<=60:
            circlex=310
            scoreright=scoreright+1
        if r_pad_up==1:
           if rightpaddley>=65:
                rightpaddley=rightpaddley-pspeed
        if r_pad_down==1:
            if rightpaddley<=376:
                rightpaddley=rightpaddley+pspeed      
        if circley > leftpaddley:
            l_pad_down=1
            l_pad_up=0
            if leftpaddley>=376:
                l_pad_down=0
        if circley < leftpaddley:
            l_pad_up=1
            l_pad_down=0
            if leftpaddley<=65:
                 l_pad_up=0
        if l_pad_up==1:
            leftpaddley=leftpaddley-pspeed
        if l_pad_down==1:
            leftpaddley=leftpaddley+pspeed
    if circley == leftpaddley:
            l_pad_up=0
            l_pad_down=0
def game2player():
    from random import randint
    from time import sleep
    pygame.display.set_caption('Ping Pong!')
    leftpaddlex=150
    pygame.init()
    leftpaddley=300
    rightpaddlex=450
    rightpaddley=350
    r_pad_up=0
    r_pad_down=0
    l_pad_up=0
    l_pad_down=0
    pspeed=4
    circlex=310
    circley=280
    red=(255,0,0)
    green=(0,255,0)
    blue=(0,0,255)
    white=(255,255,255)
    black=(0,0,0)
    screen.fill(white)
    speedx=2
    speedy=0
    scoreleft=0
    scoreright=0
    while score==21:
    def show_text(msg,x,y,color):
        fontobj=pygame.font.SysFont('freesans',32)
        msgobj=fontobj.render(msg,False,color)
        screen.blit(msgobj,(x,y))
    def GAME_OVER(msg,x,y,color):
        fontobj=pygame.font.SysFont('freesans',320)
        msgobj=fontobj.render(msg,False,color)
        screen.blit(msgobj,(x,y))
    while True:    
        pygame.display.update()
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(0,12,113),(120,60,400,400))
        pygame.draw.circle(screen,white,(circlex,circley),5,3)
        pygame.draw.line(screen,green,(leftpaddlex,leftpaddley),(leftpaddlex,leftpaddley+80),3)
        pygame.draw.line(screen,green,(rightpaddlex,rightpaddley),(rightpaddlex,rightpaddley+80),3)
        show_text('The Score is',210,5,red)
        show_text(str(scoreleft)+'-'+str(scoreright),277,29,red)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            elif event.type==KEYDOWN:
                if event.key==K_DOWN:
                    r_pad_down=1
                elif event.key==K_UP:
                    r_pad_up=1
                if event.key==K_s:
                    l_pad_up=1
                elif event.key==K_w:
                    l_pad_down=1
            elif event.type==KEYUP:
                if event.key==K_DOWN:
                    r_pad_down=0
                elif event.key==K_UP:
                    r_pad_up=0
                if event.key==K_s:
                    l_pad_up=0
                elif event.key==K_w:
                    l_pad_down=0
        circlex=circlex+speedx
        circley=circley+speedycolor
        if circlex==rightpaddlex and rightpaddley<=circley<=(rightpaddley+70):
            speedx=-speedx
            speedy=randint(-2,2 )
        if circlex==leftpaddlex and leftpaddley<=circley<=(leftpaddley+70):
            speedx=-speedx
        if circley<=60:
            speedy=-speedy
        if circley>=450:
            speedy=-speedy
        if circlex>=520:
            circlex=310
            scoreleft=scoreleft+1
        if circlex<=60:
            circlex=310
            scoreright=scoreright+1
        if r_pad_up==1:
            if rightpaddley>=65:
                rightpaddley=rightpaddley-pspeed
        if r_pad_down==1:
            if rightpaddley<=356:
                rightpaddley=rightpaddley+pspeed
        if l_pad_down==1:
            if leftpaddley>=65:
                leftpaddley=leftpaddley-pspeed
        if l_pad_up==1:
            if leftpaddley<=356:
                leftpaddley=leftpaddley+pspeed   
    screen.fill(255,255,255)
    GAME_OVER('GAME OVER',210,55,red)
while True:
    screen.fill((0,0,0)) 
    button('1-Player',red,green,250,350,100,50,game1player)
    button('2-Player',red,green,50,350,100,50,game2player)
    button("QUIT",green,red,450,350,100,50,exit)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
