import RPi.GPIO as GPIO
from time import sleep
import time
from threading import Thread
def myfunc(i):
    print('Sleeping 5 sec from thread',i)
    time.sleep(5)
    print('finished sleeping from thread ',i)
class Car:
    def __init__(self,lwa,lwb,rwa,rwb):
        self.lwa=lwa
        self.lwb=lwb
        self.rwa=rwa
        self.rwb=rwb
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.rwa,GPIO.OUT)
        GPIO.setup(self.rwb,GPIO.OUT)
        GPIO.setup(self.lwa,GPIO.OUT)
        GPIO.setup(self.lwb,GPIO.OUT)
    def Forward(self):
        GPIO.output(self.rwa,GPIO.HIGH)
        GPIO.output(self.rwb,GPIO.LOW)
        GPIO.output(self.lwa,GPIO.LOW)
        GPIO.output(self.lwb,GPIO.HIGH)
    def Backward(self):
        GPIO.output(self.rwa,GPIO.LOW)
        GPIO.output(self.rwb,GPIO.HIGH)
        GPIO.output(self.lwa,GPIO.HIGH)
        GPIO.output(self.lwb,GPIO.LOW)
    def Stop(self):
        GPIO.output(self.rwa,GPIO.LOW)
        GPIO.output(self.rwb,GPIO.LOW)
        GPIO.output(self.lwa,GPIO.LOW)
        GPIO.output(self.lwb,GPIO.LOW)      
    def Left(self):
        GPIO.output(self.rwa,GPIO.HIGH)
        GPIO.output(self.rwb,GPIO.LOW)
        GPIO.output(self.lwa,GPIO.LOW)
        GPIO.output(self.lwb,GPIO.LOW)
    def Right(self):
        GPIO.output(self.rwa,GPIO.LOW)
        GPIO.output(self.rwb,GPIO.LOW)
        GPIO.output(self.lwa,GPIO.LOW)
        GPIO.output(self.lwb,GPIO.HIGH)
    def getch(self):
        import sys, tty, termios
        fd=sys.stdin.fileno()
        old_settings=termios.tcgetattr(fd)
        try:
              tty.setraw(sys.stdin.fileno())
              ch=sys.stdin.read(1)
        finally:
              termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    def setupsensors(self):
        GPIO_TRIGGER=12
        GPIO_ECHO=6
        GPIO.setup(21,GPIO.IN)
        GPIO.setup(16,GPIO.OUT)
        GPIO.setup(GPIO_TRIGGER,GPIO.OUT)       #Trigger    
        GPIO.setup(GPIO_ECHO,GPIO.IN)           #Echo
        GPIO.output(GPIO_TRIGGER,False)
        stop=time.time()
        start=time.time()
        while True:
            GPIO.output(GPIO_TRIGGER, True)
            time.sleep(1)
            GPIO.output(GPIO_TRIGGER,False)
            start=time.time()
            while GPIO.input(GPIO_ECHO)==0:
                start=time.time()
                #print("Start:",start)
            while GPIO.input(GPIO_ECHO)==1:
                stop=time.time()
                #print("Stop:",stop)
            if stop-start>=0:
                elapsed=stop-start
                distance=elapsed*34000 
                distance=distance/2
                print('Distance :',distance)

def Sensor(i):          
    while True:
        sleep(2)
        a=GPIO.input(i)
        print(a)
def Moves():
    while True:
        key=Car0.getch()
        print(key,'*****************')
        if key=='w':
              Car0.Forward()
        if key=='s':
              Car0.Backward()
        if key=='a':
              Car0.Left()
        if key=='d':
              Car0.Right()
        if key=='e':
              Car0.Stop()
        if key=='q':
              GPIO.cleanup()
              quit()
    
Car0=Car(2,3,14,15)
S1=Thread(target=Sensor, args=(21,))
S1.start()
#Car0.setupsensors()
S2=Thread(target=Car0.setupsensors)
S2.start()
#S3=Thread(target=Moves)
#S3.start()
Moves() #Mainthread


