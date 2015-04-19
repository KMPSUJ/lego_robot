import signal
import random
import time
import sys


class Robot():
    B = False 				# for disabling obstacle check while moving backward
    s = 600

    def run(self, value1=self.S, value2=self.S):
        print ('run()')

    def go(self):
        pass

    def check_obstacle(self):
        return (random.random() > 0.9 and (not self.B))

    def sigint_handler(self, signal, frame):    # defines interrupt handler
        self.shutdown()

    def startup(self):
        print ('startup')
        signal.signal(signal.SIGINT, self.sigint_handler)
        # sets handler for keyboard interrupt( CTRL + C)

    def stop(self):
        print ('stop')

    def start(self):
        pass

    def shutdown(self):
        print ('shutdown')
        sys.exit(0)

    def obstacle(self):         # obstacle is present
       print ('obstacle present')
#      self.stop()
#      self.shutdown()

    def still(self):
        return (random.random() > 0.5)

    def turn(self, value=1):
        print ('turn ' + str(2248*value))
        self.go()

    def run_dist(self, value=1):
        print ('run_dist ' + str(value))

    def add_turn(self, value=1):
        print ('added turn' + str(value))

    def add_dist(self, value):
        print ('added distance' + str(value))

    def add_turn(self, value, callibrate=1):
        print ('added turn' + str(value))

    def left_dist(self):
        return (-50 + 300*random.random(),-50 + 300*random.random()

    def set_speed(self, val=600):
        if val > 800:
            print ('Can\'t go so fast!')
            val = 800
        self.S = val