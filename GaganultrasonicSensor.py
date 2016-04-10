import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER=12
GPIO_ECHO=6
GPIO.setup(21,GPIO.IN)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)       #Trigger    
GPIO.setup(GPIO_ECHO,GPIO.IN)           #Echo
GPIO.output(GPIO_TRIGGER,False)

while True:
    try:
        a=GPIO.input(21)
        print(a)
        if a==1:
            GPIO.output(16,GPIO.LOW)
        else:
            GPIO.output(16,GPIO.HIGH)
    except:
        GPIO.cleanup()
        exit()

