import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [2,3,4,17, 27,22,10,9]

GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)

c = 7
i = 1
while i <4:
    while c>=0:
        GPIO.output(leds[c],1)
        time.sleep(0.2)
        GPIO.output(leds[c],0)
        c-=1
    i+=1
    c=7
GPIO.output(leds,0)    
GPIO.cleanup()

