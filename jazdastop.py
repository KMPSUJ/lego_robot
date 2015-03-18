from ev3.lego import TouchSensor
from ev3.ev3dev import Motor
from ev3.ev3dev import LED
import unittest
import time

d = TouchSensor()
m = Motor(port=Motor.PORT.A)
k = 0
l = LED()
m.run_forever(-50)

m.stop_mode = 'brake'

while(True):
    time.sleep(.1)
    if(d.is_pushed):
      m.stop()
      k = k+1
    else:
      m.start()
      k = 0
    if(k > 10):
      l.left.color=LED.COLOR.AMBER
      l.left.on()
      break
l.left.off()
