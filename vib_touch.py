import time
import RPi.GPIO as GPIO

touch_pin = 17
vibratio_pin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(vibratio_pin, GPIO.IN)
GPIO.setup(touch_pin, GPIO.IN)

while True:
    if(GPIO.input(touch_pin) == GPIO.HIGH):
        print("touch hello")
    if(GPIO.input(vibratio_pin) == GPIO.HIGH):
        print("vibration hello")
    time.sleep(0.2)