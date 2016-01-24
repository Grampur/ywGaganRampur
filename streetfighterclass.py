import pygame
class Sfighter:
    def __init__(self):
        self.l=[]
        self.Jump=[]
        self.RunForward=[]
        self.Punch=[]
        self.Duck=[]
        self.Slide=[]
        self.SpecialMove=[]
        self.Spritecount=0
        for a in range(0,19,1):
            self.l.append(pygame.transform.scale(pygame.image.load('images/p'+str(a)+'.png'),(100,100)))
            if a==7 or a==18:
                self.Punch.append(pygame.transform.scale(pygame.image.load('images/p'+str(a)+'.png'),(100,100)))
            if a==6:
                self.Jump.append(pygame.transform.scale(pygame.image.load('images/p'+str(a)+'.png'),(100,100)))
            if a==3 or a==4 or a==5:
                self.RunForward.append(pygame.transform.scale(pygame.image.load('images/p'+str(a)+'.png'),(100,100)))    
            if a==9:
                self.Duck.append(pygame.transform.scale(pygame.image.load('images/p'+str(a)+'.png'),(100,100)))    
            if a==8:
                self.Slide.append(pygame.transform.scale(pygame.image.load('images/p'+str(a)+'.png'),(100,100)))
            if a==10:
                self.SpecialMove.append(pygame.transform.scale(pygame.image.load('images/p'+str(a)+'.png'),(100,100)))
    def Move(self,screen,Spritelist):
        self.Spritelist=Spritelist
        print(self.Spritecount,len(self.Spritelist))
        screen.blit(self.Spritelist[self.Spritecount],(540,320))
        if len(self.Spritelist)>1:
            print(self.Spritecount)
            self.Spritecount=self.Spritecount+1
            if self.Spritecount>=len(self.Spritelist):
                self.Spritecount=0
                print(self.Spritecount)

        
    
