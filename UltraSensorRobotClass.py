import RPi.GPIO as GPIO
from time import sleep
class Car:
      def __init__(self,lma,lmb,rma,rmb):
            self.lma=lma
            self.lmb=lmb
            self.rma=rma
            self.rmb=rmb
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.rma,GPIO.OUT)
            GPIO.setup(self.rmb,GPIO.OUT)
            GPIO.setup(self.lma,GPIO.OUT)
            GPIO.setup(self.lmb,GPIO.OUT)
            GPIO.setup(self.
      def Forward(self):
            GPIO.output(self.rma,GPIO.HIGH)
            GPIO.output(self.rmb,GPIO.LOW)
            GPIO.output(self.lma,GPIO.LOW)
            GPIO.output(self.lmb,GPIO.HIGH)
      def Backward(self):
            GPIO.output(self.rma,GPIO.LOW)
            GPIO.output(self.rmb,GPIO.HIGH)
            GPIO.output(self.lma,GPIO.HIGH)
            GPIO.output(self.lmb,GPIO.LOW)
      def Stop(self):
            GPIO.output(self.rma,GPIO.LOW)
            GPIO.output(self.rmb,GPIO.LOW)
            GPIO.output(self.lma,GPIO.LOW)
            GPIO.output(self.lmb,GPIO.LOW)      
      def Left(self):
            GPIO.output(self.rma,GPIO.HIGH)
            GPIO.output(self.rmb,GPIO.LOW)
            GPIO.output(self.lma,GPIO.LOW)
            GPIO.output(self.lmb,GPIO.LOW)
      def Right(self):
            GPIO.output(self.rma,GPIO.LOW)
            GPIO.output(self.rmb,GPIO.LOW)
            GPIO.output(self.lma,GPIO.LOW)
            GPIO.output(self.lmb,GPIO.HIGH)
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

Car0=Car(2,3,14,15,21)
while True:
      key=Car0.getch()
      print(key)
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
            
      
      
