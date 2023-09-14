from machine import Pin
from time import sleep

led1 = Pin(2,Pin.OUT)
led2 = Pin(4,Pin.OUT)

def toggle_leds():
     led1.value(not led1.value())
     led2.value(not led2.value())
     
while True:
    toggle_leds()
    sleep(0.2)
   
   


    