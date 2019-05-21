import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while 1:
    i=0
    j=0
    while i<10:
        j=j+GPIO.input(17)
        time.sleep(0.1)
        i+=1
    print(j)


