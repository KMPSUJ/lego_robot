from ev3.lego import TouchSensor
from ev3.lego import ColorSensor
from override import m_over as Motor
from ev3.ev3dev import LED
from ev3.ev3dev import Tone
from ev3.ev3dev import Key 
import unittest
import time
import signal
import sys
import random

class Robot():
    touch = TouchSensor()
    M1 = Motor(port=Motor.PORT.A)
    M2 = Motor(port=Motor.PORT.D)
    K = Key()
    L = LED()
    T = Tone()
    C = ColorSensor()
    B = False 				#for disabling obstacle check while moving backward
    
    def run(self, value1=300, value2=300):
     self.M1.run_forever(value1)
     self.M2.run_forever(value2)
     

   
    def go(self):
     self.M1.start()
     self.M2.start()

    def check_obstacle(self):
      return (self.touch.is_pushed and (not self.B))
    
    def sigint_handler(self, signal, frame): #defines interrupt handler
      self.shutdown()
    
    def startup(self):
      self.M1.stop_mode = 'brake'	#robot stops in place
      self.M2.stop_mode = 'brake'	#robot stops in place
      self.M1.regulation_mode = True
      self.M2.regulation_mode = True
      self.L.left.color=LED.COLOR.GREEN
      self.L.right.color=LED.COLOR.GREEN
      signal.signal(signal.SIGINT, self.sigint_handler)  #sets handler for keyboard interrupt( CTRL + C)
      
    def stop(self):
      self.M1.stop()
      self.M2.stop()
      
    def start(self):
      self.L.left.color=LED.COLOR.GREEN
      self.L.left.on()
      self.run()
     
    def shutdown(self):
      self.stop()
      self.M1.stop_mode = 'coast'	#free motor
      self.M2.stop_mode = 'coast'	#free motor
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
      self.B = True
      self.run_dist(-1)
      time.sleep(0.1)
      while(not self.ru()):
	time.sleep(0.1)
#      time.sleep(1)
      self.turn(1/6.0 + 0.25 * random.random())
      time.sleep(0.1)
      while(not self.ru()):
	time.sleep(0.1)
      self.B = False
#      self.stop()
#      self.shutdown()

    def ru(self):
      return ((self.M1.pulses_per_second == 0) and (self.M2.pulses_per_second == 0))

    def turn(self, value = 1, callibrate = 1):
      self.M1.set_rel_position( 2248*value*callibrate, speed_sp= 600)
      self.M2.set_rel_position(-2248*value*callibrate, speed_sp=-600)
      self.go()

    def run_dist(self,value = 1):
      self.M1.set_rel_position(720*value, speed_sp=300)
      self.M2.set_rel_position(720*value, speed_sp=300)
      self.go()

     
    
