import time
from modules import Robot as r

k = 0

R = r.Robot()
R.startup()
R.start()
<<<<<<< HEAD
s = open("out", 'w')
=======
s = open("out",'w')
>>>>>>> 87033328f92405016d35943f5808870c2149faeb

while(True):
    time.sleep(.1)
    s.write(str(R.C.rgb))
    s.write('\n')
    if(R.check_obstacle()):
        R.obstacle()
        k = k+1
    else:
        R.start()
        #     k = 0
    if(k > 10 or R.K.backspace):
<<<<<<< HEAD
        s.close()
        R.shutdown()
=======
      s.close()
      R.shutdown()
>>>>>>> 87033328f92405016d35943f5808870c2149faeb
