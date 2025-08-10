import time
import RPi.GPIO as GPIO

vibratio_port = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(vibratio_port, GPIO.IN)

while True:
    if(GPIO.input(vibratio_port) == 1):
        print("hello world")
    time.sleep(0.2)