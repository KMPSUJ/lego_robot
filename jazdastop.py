from ev3.lego import TouchSensor
from ev3.ev3dev import Motor
from ev3.ev3dev import LED
from ev3.ev3dev import Tone
from ev3.ev3dev import Key 
import unittest
import time
import signal
import sys

def startup_sequence():
    global d = TouchSensor()
    global m = Motor(port=Motor.PORT.A)
    global k = 0
    global K = Key()
    global l = LED()
    m.run_forever(-50)
    m.stop_mode = 'brake'
    l.left.color=LED.COLOR.GREEN
    l.right.color=LED.COLOR.GREEN
    signal.signal(signal.SIGINT, sigint_handler)  #sets handler for keyboard interrupt( CTRL + C)

def sigint_handler(signal, frame): #defines interrupt handler
    shutdown_sequence()

def shutdown_sequence():
    m.stop()
    m.stop_mode = 'coast'
    l.left.color=LED.COLOR.AMBER
    l.left.on()
    Tone.play(440)
    sleep(0.1)
    l.left.color=LED.COLOR.GREEN
    Tone.stop()
    sys.exit(0)

#end of definitions
startup_sequence()
while(True):
    time.sleep(.1)
    if(d.is_pushed):
      m.stop()
      k = k+1
    else:
      m.start()
      k = 0
    if(k > 10 or K.backspace)):
      shutdown_sequence()
