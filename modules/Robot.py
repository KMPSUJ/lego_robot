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
     self. M.run_forever(value)
    
    def check_obstacle(self):
      return self.touch.is_pushed
    
    def sigint_handler(signal, frame): #defines interrupt handler
      self.shutdown_sequence()
    
    def startup(self):
      self.M.stop_mode = 'brake'	#robot stops in place
      self.L.left.color=LED.COLOR.GREEN
      self.L.right.color=LED.COLOR.GREEN
      signal.signal(signal.SIGINT, self.sigint_handler)  #sets handler for keyboard interrupt( CTRL + C)
      
    def stop(self):
      self.M.stop()
      
    def start(self):
      self.L.left.color=LED.COLOR.GREEN
      self.L.left.on()
      self.run()
     
    def shutdown(self):
      self.stop()
      self.M.stop_mode = 'coast'	#free motor
      self.L.left.color=LED.COLOR.AMBER
      self.L.left.on()
      self.T.play(440)
      time.sleep(0.1)
      self.L.left.color=LED.COLOR.GREEN
      self.L.left.on()
      self.T.stop()
      sys.exit(0)
      
    def obstacle(self):	#obstacle is present
      self.L.left.color=LED.COLOR.YELLOW
      self.L.left.on()
      self.stop()
      
      
    
