from ev3.lego import TouchSensor
from ev3.lego import ColorSensor
from ev3.lego import InfraredSensor
from override import m_over as Motor
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
			self.A = Motor0(port=Motor.PORT.A)
			self.D = Motor(port=Motor.PORT.C)
			

		except:
			self.L.left.color = LED.COLOR.RED
			self.say("Brak silników")
		try:
			touch = TouchSensor()
		except:
			self.L.left.color = LED.COLOR.RED
			self.say("Brak sensora dotyku", speed=200)
		try:
			C = ColorSensor()
		except:
			self.L.left.color = LED.COLOR.RED
			self.say("Brak sensora koloru", speed=200)
		try:
			IR = InfraredSensor()
			IR.mode = "IR-REMOTE"
		except:
			self.L.left.color = LED.COLOR.RED
			self.say("Brak sensora podczerwieni",200)	

		self.A.stop_mode = 'brake'     # robot stops in place
		self.D.stop_mode = 'brake'     # robot stops in place
		self.A.regulation_mode = True
		self.D.regulation_mode = True
		self.L.left.color = LED.COLOR.GREEN
		self.L.right.color = LED.COLOR.GREEN
		signal.signal(signal.SIGINT, self.sigint_handler)
		# sets handler for keyboard interrupt( CTRL + C)

	def Read():
		return [IR.value0, IR.value1, IR.value2, IR.value3]
		#valueN is channel N+1 
		#1 LU
		#2 Ld
		#3 RU
		#4 RD
		#9 beacon

	def run(self):
		self.A.run_forever(self.S)
		self.D.run_forever(self.S)

	def run(self, value1=300, value2=300):
		self.A.run_forever(value1)
		self.D.run_forever(value2)

	def go(self):
		self.A.start()
		self.D.start()

	def check_obstacle(self):
		return (self.touch.is_pushed and (not self.B))

	def sigint_handler(self, signal, frame):    # defines interrupt handler
		self.shutdown()

	def stop(self, val=0):
		self.A.stop()
		self.D.stop()

	def start(self):
		self.L.left.color = LED.COLOR.GREEN
		self.L.left.on()
		# self.run()

	def shutdown(self):
		self.stop()
		self.A.stop_mode = 'coast'     # free motor
		self.D.stop_mode = 'coast'     # free motor
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
		self.D.set_rel_position(-2248*value*callibrate, speed_sp=-self.S)
		self.go()

	def run_dist(self, value=1):
		self.A.set_rel_position(720*value, speed_sp=self.S)
		self.D.set_rel_position(720*value, speed_sp=self.S)
		self.go()

	def add_dist(self, value):
		self.A.add_rel_position(value)
		self.D.add_rel_position(value)

	def add_turn(self, value, callibrate=1):
		self.A.add_rel_position(2248*value*callibrate)
		self.D.add_rel_position(-2248*value*callibrate)

	def left_dist(self):
		return (self.A.position - self.A.position_sp,
			self.D.position - self.D.position_sp)

	def set_speed(self, val=600):
		if val > 800:
		    print ('Can\'t go so fast!')
		    val = 800
		self.S = val
