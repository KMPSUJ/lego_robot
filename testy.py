from modules import Robot
from time
r = Robot()
print(absolute 60deg)
r.M1.run_mode='position'
r.M1.position_mode='absolute'
r.M1.regulation_mode = True
r.M1.pulses_per_second = 300
r.M1.position_sp = r.M1.position + 60
r.M1.start()
r.T.play(440,100)
time.sleep(1)
print(absolute -60deg)
r.M1.pulses_per_second = -300
r.M1.position_sp = r.M1.position - 60
r.M1.start()
r.T.play(440,100)
time.sleep(1)
print(relative 60deg)
r.M1.position_mode = 'relative'
r.M1.position = 0
r.M1.position_sp = 60 
r.M1.start()
r.T.play(440,100)
time.sleep(1)
print(relative -60deg)
r.M1.position = 0
r.M1.position_sp = -60 
r.M1.start()
r.T.play(440,100)
time.sleep(1)
