import RPi.GPIO as GPIO
from time import sleep
from UltraSensorRobotClass import Car
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(21,GPIO.IN)
GPIO.setup(16,GPIO.OUT)

GPIO.output(2,GPIO.HIGH) #Makes the right wheel go forward 
GPIO.output(3,GPIO.LOW)

GPIO.output(2,GPIO.LOW) #Makes the right wheel go backwards 
GPIO.output(3,GPIO.HIGH)

GPIO.output(14,GPIO.LOW) #Makes the left wheel go forward
GPIO.output(15,GPIO.HIGH)
sleep(30)

GPIO.output(14,GPIO.HIGH) #Makes the left wheel go backwards
GPIO.output(15,GPIO.LOW)
sleep(25)

GPIO.cleanup()
