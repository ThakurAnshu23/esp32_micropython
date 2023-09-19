import machine
import neopixel
import time

np = neopixel.NeoPixel(machine.Pin(48),1)

while True:
    try:
       np[0] = (255,0,0)
       np.write()
       time.sleep(0.1)
       np[0] = (0,255,0)
       np.write()
       time.sleep(0.1)
       np[0] = (0,0,255)
       np.write()
       time.sleep(0.1)
    except KeyboardInterrupt:
         print("EXIT")
         break

