from ev3.lego import TouchSensor
from ev3.ev3dev import Motor
from ev3.ev3dev import LED
from ev3.ev3dev import Tone
from ev3.ev3dev import Key 
import unittest
import time
import signal
import sys

class Robot():
    touch = TouchSensor()
    M = Motor(port=Motor.PORT.A)
    K = Key()
    L = LED()
    T = Tone()
    
    def run(self, value=-50):
      M.run_forever(value)
    
    def check_obstacle():
      return touch.is_pushed
    
    def sigint_handler(signal, frame): #defines interrupt handler
      shutdown_sequence()
    
    def startup():
      M.stop_mode = 'brake'	#robot stops in place
      L.left.color=LED.COLOR.GREEN
      L.right.color=LED.COLOR.GREEN
      signal.signal(signal.SIGINT, sigint_handler)  #sets handler for keyboard interrupt( CTRL + C)
      
    def stop():
      M.stop()
      
    def start():
      l.left.color=LED.COLOR.GREEN
      l.left.on()
      self.run()
     
    def shutdown():
      self.stop()
      M.stop_mode = 'coast'	#free motor
      L.left.color=LED.COLOR.AMBER
      L.left.on()
      T.play(440)
      time.sleep(0.1)
      L.left.color=LED.COLOR.GREEN
      L.left.on()
      T.stop()
      sys.exit(0)
      
    def obstacle():	#obstacle is present
      L.left.color=LED.COLOR.YELLOW
      L.left.on()
      self.stop()
      
      
    
