from modules import Robot
import time

r = Robot.Robot()
while(True):
	a = r.Read()
	if not a[0] and not a[1]:
		r.stop()
	if a[0] == 1 or a[0] == 5 or a[0] == 6:
		r.A.run_forever(r.S/2)
	elif a[0] == 2 or a[0] == 7 or a[0] == 8:
		r.A.run_forever(-r.S/2)
	else:
		r.A.stop()
	if a[0] == 3 or a[0] == 5 or a[0] == 7:
		r.C.run_forever(r.S/2)
	elif a[0] == 4 or a[0] == 6 or a[0] == 8:
		r.C.run_forever(-r.S/2)
	else:
		r.C.stop()
	if a[1] == 1:
		r.B.run_forever(r.S) 
	if a[1] == 2:
		r.B.run_forever(-r.S) 
		
		
