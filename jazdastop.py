import time
from modules.Robot import Robot as r

k = 0

R = r()
R.startup()
R.start()

while(True):
    time.sleep(.1)
    if(check_obstacle()):
      obstacle()
      k = k+1
    else:
      R.start()
      k = 0
    if(k > 10 or R.K.backspace):
      R.shutdown
