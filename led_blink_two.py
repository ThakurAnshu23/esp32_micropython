import machin
import time

class Flasher:
    def __init__(self,pin,on_time,off_time):
        self.pin = pin
        self.on_time = on_time
        self.off_time = off_time
        self.led_state = 0
        self.last_change = 0
        self.led = machine.Pin(self.pin,machine.Pin.OUY)
     def update(self):
         if(time.ticks_ms()-self.last_change)>=self.off_time and self.led_state ==0:
             self.last_change = time.ticks_ms()
             self.led_state = 1
             self.led.value(self.led_state)
             print(f"LED at pin [self.pin] is ON")
          elif(time.ticks_ms()-self.last_change)>=self.on_time and self.led_state == 1:
              self.last_change = time.ticks_ms()
              self.led_state = 0
              self.led.value(self.led_state)
              print(f"LED at pin {self.pin} is OFF")
              
            
            
#object for led 1
led1= Flasher(8,500,900)
#object for led 2
led2 = Flasher(47,250,300)
              
        
        
        
        
while True:
    try:
        led1.update()
        led2.update()
    except KeyboardInterrupt:
        print("EXIT")
        break
        