import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)
while True:
    try:
        a=GPIO.input(21)
        print(a)
    except:
        GPIO.cleanup()
        exit()
