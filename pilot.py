from modules import Robot
import time

r = Robot.Robot()
while(True):
	a = r.Read()
	if not a[0] and not a[1]:
		r.stop()
	elif a[0] == 1:
		r.A.run_forever(r.S/2)
	elif a[0] == 2:
		r.A.run_forever(-r.S/2)
	if a[0] == 3:
		r.C.run_forever(r.S/2)
	elif a[0] == 4:
		r.C.run_forever(-r.S/2)
	if a[1] == 1:
		r.B.run_forever(r.S) 
	if a[1] == 2:
		r.B.run_forever(-r.S) 
		
		
