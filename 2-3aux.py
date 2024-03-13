
import RPi.GPIO as GPIO
import time


leds = [2,3,4,17,27,22,10,9]


aux = [21,20,26,16,19,25,23,24]


GPIO.setmode(GPIO.BCM)


for led in leds:
    GPIO.setup(led, GPIO.OUT)


for aux_pin in aux:
    GPIO.setup(aux_pin, GPIO.IN)

try:
    while True:
        
        for i, aux_pin in enumerate(aux):
            if GPIO.input(aux_pin) == GPIO.LOW:
                
                GPIO.output(leds[i], GPIO.LOW)
            else:
                
                GPIO.output(leds[i], GPIO.HIGH)

finally:
  
    GPIO.cleanup()

print("Скрипт успешно выполнен! Подключите провод к пину GND в области AUX и проверьте работу светодиодов.")
