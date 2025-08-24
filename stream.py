import time
import RPi.GPIO as GPIO
import streamlit as st

touch_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(touch_pin, GPIO.IN)


while(True):
    if(GPIO.input(touch_pin) == GPIO.HIGH):
        st.title('hello')
        time.sleep(1)
        st.title('world')
    time.sleep(0.2)
