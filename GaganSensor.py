import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER=12
GPIO_ECHO=6
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)       #Trigger    
GPIO.setup(GPIO_ECHO,GPIO.IN)           #Echo
GPIO.output(GPIO_TRIGGER,False)
time.sleep(0.5)
while True:
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER,False)
    start=time.time()
    if GPIO.input(GPIO_ECHO)==0:
        start=time.time()
    if GPIO.input(GPIO_ECHO)==1:
        stop=time.time()
    elapsed=stop-start
    distance=elapsed*34000
    distance=distance/2
    print('Distance :',distance)
GPIO.cleanup()
