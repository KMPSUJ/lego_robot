import time, datetime
from modules import Robot as r

k = 0

R = r.Robot()
R.startup()
R.start()
R.S = 200
# R.run()
R.turn(2)
s = open("out",'a')
st = ''
s.write(str(datetime.datetime.today()))

while(True):
    time.sleep(.01)
    ref = R.C.rgb
    if ref[1] < 145:
        R.T.play(440,80)
    st += (str(ref))
    st += ('\n')
    if(R.check_obstacle()):
        R.obstacle()
        k = k+1
    else:
        R.start()
        #     k = 0
    if(k > 10 or R.K.backspace):
        s.write(st)
        s.close()
        R.shutdown()
