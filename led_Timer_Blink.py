#Timer two has desaided hardware PWM controller
# timer1 timer2 timer3 


import machine


led = machine.Pin(8,machine.Pin.Out)_

timer0 = machine.Timer(0)

def timer0_(t):
    led.value(not led.value())
    print("LED is on" if led.value() else "LED is off")
    
    
timer0.init(mode=machine.Timer.PERIODIC, period=1000, callback=timer0_isr)

while true:
    try:
    except KeyboardInterrupt:
            print("EXIT")
            break
            