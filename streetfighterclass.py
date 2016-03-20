import pygame
class Sfighter:
    def __init__(self,image,startx,starty):
        self.l=[]
        self.Jump=[]
        self.RunForward=[]
        self.Punch=[]
        self.Duck=[]
        self.Slide=[]
        self.SpecialMove=[]
        self.startx=startx
        self.starty=starty
        self.Spritecount=0
        z=175
        self.direction=0
        self.xchange=0
        if image=='p':
            for a in range(0,19,1):
                self.l.append(pygame.transform.scale(pygame.image.load('images/'+image+str(a)+'.png'),(z,z)))
                if a==7 or a==18:
                    self.Punch.append(pygame.transform.scale(pygame.image.load('images/'+image+str(a)+'.png'),(z,z)))
                if a==6:
                    self.Jump.append(pygame.transform.scale(pygame.image.load('images/'+image+str(a)+'.png'),(z,z)))
                if a==3 or a==4 or a==5:
                    self.RunForward.append(pygame.transform.scale(pygame.image.load('images/'+image+str(a)+'.png'),(z,z)))    
                if a==9:
                    self.Duck.append(pygame.transform.scale(pygame.image.load('images/'+image+str(a)+'.png'),(z,z)))    
                if a==8:
                    self.Slide.append(pygame.transform.scale(pygame.image.load('images/'+image+str(a)+'.png'),(z,z)))
                if a==10:
                    self.SpecialMove.append(pygame.transform.scale(pygame.image.load('images/'+image+str(a)+'.png'),(z,z)))
        if image=='pD':
            for a in range(0,14,1):
                self.l.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load('images/'+image+str(a)+'.png'),(z,z)),True,False,))
                if a==0 or a==1 or a==2 or a==3 or a==4 or a==5 or a==6:
                    self.RunForward.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load('images/'+image+str(a)+'.png'),(z,z)),True,False,))
                if a==8 or a==9 or a==10:
                    self.Jump.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load('images/'+image+str(a)+'.png'),(z,z)),True,False,))
                if a==11 or a==12:
                    self.Duck.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load('images/'+image+str(a)+'.png'),(z,z)),True,False,))    
                if a==13:
                    self.SpecialMove.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load('images/'+image+str(a)+'.png'),(200,z)),True,False,))
    def Move(self,screen,Spritelist):
        self.Spritelist=Spritelist
        if len(self.Spritelist)>=1:
            self.Spritecount=self.Spritecount+1
            if self.Spritecount>=len(self.Spritelist) or len(self.Spritelist)==1:
                self.Spritecount=0
        print(self.Spritecount,len(self.Spritelist))
        if self.direction==0:
            print('jo')
            screen.blit(self.Spritelist[self.Spritecount],(self.startx,self.starty))
        else:
            screen.blit(pygame.transform.flip(self.Spritelist[self.Spritecount],True,False),(self.startx,self.starty))


        
    
