class Car:
      def __init__(self,lma,lmb,rma,rmb):
            import RPi.GPIO as GPIO
            from time import sleep
            self.lma=lma
            self.lmb=lmb
            self.rma=rma
            self.rmb=rmb
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.rma,GPIO.OUT)
            GPIO.setup(self.rmb,GPIO.OUT)
            GPIO.setup(self.lma,GPIO.OUT)
            GPIO.setup(self.lmb,GPIO.OUT)
      def Forward(self):
            GPIO.output(self.rma,GPIO.HIGH)
            GPIO.output(self.rmb,GPIO.LOW)
            GPIO.output(self.lma,GPIO.HIGH)
            GPIO.output(self.lmb,GPIO.LOW)
      def Backwards(self):
            GPIO.output(self.rma,GPIO.LOW)
            GPIO.output(self.rmb,GPIO.HIGH)
            GPIO.output(self.lma,GPIO.LOW)
            GPIO.output(self.lmb,GPIO.HIGH)
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
            GPIO.output(self.lma,GPIO.HIGH)
            GPIO.output(self.lmb,GPIO.LOW)
      
