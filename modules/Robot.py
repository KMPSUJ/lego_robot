# -*- coding: utf-8 -*-
from ev3.lego import TouchSensor
from ev3.lego import ColorSensor
from ev3.lego import InfraredSensor
from override import m_over as Motor
from override  import mm_over as MMotor
from ev3.ev3dev import LED
from ev3.ev3dev import Tone
from ev3.ev3dev import Key
import time
import signal
import sys
import os

class Robot():
	def say(self, text='Nie mam nic do powiedzenia', lang='pl',speed=120):
		os.system('espeak -s '+str(speed)+' -a 200 -g 1 -v ' + str(lang) +' "'+ str(text) + '" --stdout | aplay')


	
	def __init__(self):
		self.K = Key()
		self.L = LED()
		self.T = Tone()
		self.B = False 		# for disabling obstacle check while moving backward
		self.S = 600                 # speed
		
		try:
			self.A = Motor(port=Motor.PORT.A)
			self.C = Motor(port=Motor.PORT.C)
			self.B = MMotor(port=MMotor.PORT.B)

		except:
			self.L.left.color = LED.COLOR.RED
			self.say("Brak silników")
		try:
			touch = TouchSensor()
		except:
			self.L.left.color = LED.COLOR.RED
			self.say("Brak sensora dotyku", speed=200)
		try:
			self.Color = ColorSensor()
		except:
			self.L.left.color = LED.COLOR.RED
			self.say("Brak sensora koloru", speed=200)
		try:
			self.IR = InfraredSensor()
			self.IR.mode = "IR-REMOTE"
		except:
			self.L.left.color = LED.COLOR.RED
			self.say("Brak sensora podczerwieni",200)	

		self.A.stop_mode = 'brake'     # robot stops in place
		self.C.stop_mode = 'brake'     # robot stops in place
		self.B.stop_mode = 'brake'
		self.A.regulation_mode = True
		self.C.regulation_mode = True
		self.B.regulation_mode = True
		self.L.left.color = LED.COLOR.GREEN
		self.L.right.color = LED.COLOR.GREEN
		signal.signal(signal.SIGINT, self.sigint_handler)
		# sets handler for keyboard interrupt( CTRL + C)

	def Read(self):
	        """valueN is channel N+1 
		1 U
		2 D
		3  U
		4  D
		5 UU
		6 UD
		7 DU
		8 DD
		9 beacon"""
		return [self.IR.value0, self.IR.value1, self.IR.value2, self.IR.value3]
		

	def run(self, value1=600, value2=600):
		self.A.run_forever(value1)
		self.C.run_forever(value2)

	def go(self):
		self.A.start()
		self.C.start()

	def check_obstacle(self):
		return (self.touch.is_pushed and (not self.B))

	def sigint_handler(self, signal, frame):    # defines interrupt handler
		self.shutdown()

	def stop(self, val=0):
		self.A.stop()
		self.C.stop()
		self.B.stop()

	def start(self):
		self.L.left.color = LED.COLOR.GREEN
		self.L.left.on()
		# self.run()

	def shutdown(self):
		self.stop()
		self.A.stop_mode = 'coast'     # free motor
		self.C.stop_mode = 'coast'     # free motor
		self.B.stop_mode = 'coast'
		self.L.left.color = LED.COLOR.AMBER
		self.L.left.on()
		self.T.play(440)
		time.sleep(0.1)
		self.L.left.color = LED.COLOR.GREEN
		self.L.left.on()
		self.T.stop()
		sys.exit(0)

	def obstacle(self):         # obstacle is present
		self.L.left.color = LED.COLOR.YELLOW
		self.L.left.on()
		self.T.play(880, 0.01)
	#       self.stop()
	#       self.shutdown()

	def still(self):
		return ((self.M1.pulses_per_second == 0)
			and (self.M2.pulses_per_second == 0))

	def turn(self, value=1, callibrate=1):
		self.A.set_rel_position(2248*value*callibrate, speed_sp=self.S)
		self.C.set_rel_position(-2248*value*callibrate, speed_sp=-self.S)
		self.go()

	def run_dist(self, value=1):
		self.A.set_rel_position(720*value, speed_sp=self.S)
		self.C.set_rel_position(720*value, speed_sp=self.S)
		self.go()

	def add_dist(self, value):
		self.A.add_rel_position(value)
		self.C.add_rel_position(value)

	def add_turn(self, value, callibrate=1):
		self.A.add_rel_position(2248*value*callibrate)
		self.C.add_rel_position(-2248*value*callibrate)

	def left_dist(self):
		return (self.A.position - self.A.position_sp,
			self.C.position - self.C.position_sp)

	def set_speed(self, val=600):
		if val > 800:
		    print ('Can\'t go so fast!')
		    val = 800
		self.S = val

        def changestate(self, value=0):
                self.B.set_rel_position(value, speed_sp=300)
		self.B.start()
