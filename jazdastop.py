import time
from modules import Robot as r

k = 0

R = r.Robot()
R.startup()
R.start()

while(True):
    time.sleep(.1)
    if(R.check_obstacle()):
      R.obstacle()
      k = k+1
    else:
      R.start()
  #    k = 0
    if(k > 10 or R.K.backspace):
      R.shutdown()
