import time
from modules import Robot as r

k = 0

R = r.Robot()
R.startup()
R.start()
s = open("out",'w')

while(True):
    time.sleep(.1)
    s.write(str(R.C.rgb))
    s.write('\n')
    if(R.check_obstacle()):
      R.obstacle()
      k = k+1
    else:
      R.start()
  #    k = 0
    if(k > 10 or R.K.backspace):
      s.close()
      R.shutdown()
