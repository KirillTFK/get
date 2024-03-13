import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

GPIO.setup(19, GPIO.OUT)

GPIO.setup(16, GPIO.IN) 

GPIO.output(19, GPIO.input(16))

print(GPIO.input(16))