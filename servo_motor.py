import time
from board import SCL, SDA
import busio
from adafruit_servokit import ServoKit


kit = ServoKit(channels = 16)

ServoR = kit.servo[5]

while(True):
    ServoR.angle = 0
    time.sleep(1)
    ServoR.angle = 90
    time.sleep(1)
    ServoR.angle = 180
    time.sleep(1)