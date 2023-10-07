import machine
import time

def led_toggle(pin,on_time,off_time):
       #object for led
    led = machine.Pin(pin,machine.Pin.OUT)
    #variables
    led_state = 0
    last_change = 0
    if (time.ticks_ms()-Last_change)>=off_time and led_state is o:
        last change = time.ticks_ms()
        led_state = 1
        led.value(led_state)
        print("LED is on")
    elif (time.ticks_ms()-last_change)>=on_time and led_state is 1:
        last change = time.ticks_ms()
        led_state = 0
        led.value(led_state)
        print("LED is off")
        
while True:
    try:
        led_toggle(8,1000,2000)
    except keyboardInterrup:
        print("EXIT")
        break  
        