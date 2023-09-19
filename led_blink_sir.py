import machine
import time

led_pin = machine.Pin(8,machine.Pin.OUT)

while True:
    try:
        led_pin.value(1)
        print("LED IS ON")
        time.sleep(1)
        led_pin(0)
        print("LED IS OF")
        time.sleep(1)
    except KeyboardInterrupt:
     exit
     print("EXIT")
            