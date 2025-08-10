import time
import RPi.GPIO as GPIO
import spidev as SPI
from lib import LCD_2inch
from PIL import Image,ImageDraw,ImageFont

RST = 27
DC = 25
BL = 18
disp = LCD_2inch.LCD_2inch()
disp.Init()
img = Image.open('frame10.png')
while True:
    disp.ShowImage(img)