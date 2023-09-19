import machine
import neopixel
import time

np = neopixel.NeoPixel(machine.Pin(48),1)
button = machine.Pin(0,machine.Pin.IN,machine.Pin.PULL_UP)
value = 0

def toggle_led(p):
    global value
    if value == 0:
        value = 255
    elif value == 255:
        value = 0
    np[0] = (value,0,0)
    np.write()
    
button.irq(trigger=machine.Pin.IRQ_FALLING,handler=toggle_led)

while True:
    try:
        time.sleep(5)
    except KeyboardInterrupt:
        print("EXIT")
        break

            







