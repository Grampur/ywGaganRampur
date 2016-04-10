import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER=12
GPIO_ECHO=6
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)       #Trigger    
GPIO.setup(GPIO_ECHO,GPIO.IN)           #Echo
GPIO.output(GPIO_TRIGGER,False)
sleep(0.5)
GPIO.output(GPIO_TRIGGER, False)
sleep(0.00001)
GPIO.output(GPIO_TRIGGER,False)
start=time.time()
while GPIO.input(GPIO_ECHO)==0:
    start=time.time()
while GPIO.input(GPIO_ECHO)==1:
    stop=time.time()
elapsed=stop-start
distance=elapsed*34000
distance=distance/2
