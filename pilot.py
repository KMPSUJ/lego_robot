# -*- coding: utf-8 -*-
from modules import Robot
import time

r = Robot.Robot()
state = [0, 1000, 1500]
(run, move, write) = range(3)
i = run
slowdown = 1
flag_A = 0
flag_C = 0
lock = [0, 0, 0, 0]

while(True):
    a = r.Read()
    for it in range(len(lock)):
        if lock[it]:
            lock[it] = lock[it] - 1

    if a[0]:                                        # kontrolka ciągła
        flag_A = 0
        flag_C = 0
        if a[0] == 1 or a[0] == 5 or a[0] == 6:
            r.A.run_forever(r.S/slowdown)
        elif a[0] == 2 or a[0] == 7 or a[0] == 8:
            r.A.run_forever(-r.S/slowdown)
        else:
            r.A.stop()
        if a[0] == 3 or a[0] == 5 or a[0] == 7:
            r.C.run_forever(r.S/slowdown)
        elif a[0] == 4 or a[0] == 6 or a[0] == 8:
            r.C.run_forever(-r.S/slowdown)
        else:
            r.C.stop()

    elif a[1] and not lock[1]:                         # kontrolka lewa: dyskretna
        if a[1] == 1 and i is not run:              # kontrolka prawa: ciągła
            r.changestate(state[i]-state[i-1])
            i = i-1
            time.sleep(0.5)                         # (state[i]-state[i-1])/r.S
            if i is run:
                slowdown = 1
        elif a[1] == 2 and i is not write:
            r.changestate(state[i]-state[i+1])
            i = i+1
            slowdown = 5
            time.sleep(0.5)                         # (state[i+1]-state[i])/r.S
        elif a[1] == 3:
            r.B.run_forever(r.S)
        elif a[1] == 4:
            r.B.run_forever(-r.S)
        elif a[1] == 9:
	    r.B.stop() 
        else:
            pass

    elif a[2]:                                      # kontrolka one-klick
        if a[2] == 1 or a[2] == 5 or a[2] == 6:     # stop na 9 (beacon)
                if flag_A == -1:
                        r.A.stop()
                        flag_A = 0
                        lock[0] = 30                # lock = 30
                elif not lock[0]:
                        r.A.run_forever(r.S/slowdown)
                        flag_A = 1
        elif a[2] == 2 or a[2] == 7 or a[2] == 8:
            if flag_A == 1:
                r.A.stop()
                flag_A = 0
                lock[1] = 30                        # lock = 30
            elif not lock[1]:
                r.A.run_forever(-r.S/slowdown)
                flag_A = -1
        if a[2] == 3 or a[2] == 5 or a[2] == 7:
            if flag_C == -1:
                r.C.stop()
                flag_C = 0
                lock[2] = 30                        # lock = 30
            elif not lock[2]:
                r.C.run_forever(r.S/slowdown)
                flag_C = 1
        elif a[2] == 4 or a[2] == 6 or a[2] == 8:
            if flag_C == 1:
                r.C.stop
                flag_C = 0
                lock[3] = 30                        # lock = 30
            elif not lock[3]:
                r.C.run_forever(-r.S/slowdown)
                flag_C = -1
        if a[2] == 9:
            r.stop()
            flag_A = 0
            flag_C = 0

    elif a[3]:                                      # alternatywna one-klick
        if a[3] == 1:                               # 1 przycisk - oba silniki
            if flag_A == -1 and flag_C == -1:
                r.stop()
                flag_A = 0
                flag_C = 0
                lock[0] = 30                        # lock = 30
            elif not lock[0]:
                r.run(r.S/slowdown, r.S/slowdown)
                flag_A = 1
                flag_C = 1
        elif a[3] == 2:
            if flag_A == 1 and flag_C == 1:
                r.stop()
                flag_A = 0
                flag_C = 0
                lock[1] = 30                        # lock = 30
            elif not lock[1]:
                r.run(-r.S/slowdown, -r.S/slowdown)
                flag_A = -1
                flag_C = -1
        elif a[3] == 3:
            if flag_A == 1 and flag_C == -1:
                r.stop()
                flag_A = 0
                flag_C = 0
                lock[2] = 30                        # lock = 30
            elif not lock[2]:
                r.run(-r.S/slowdown, r.S/slowdown)
                flag_A = -1
                flag_C = 1
        elif a[3] == 4:
            if flag_A == -1 and flag_C == 1:
                r.stop()
                flag_A = 0
                flag_C = 0
                lock[3] = 30                        # lock = 30
            elif not lock[3]:
                r.run(r.S/slowdown, -r.S/slowdown)
                flag_A = 1
                flag_C = -1
        elif a[3] == 9:
            r.stop()
            flag_A = 0
            flag_C = 0
    else:
        if not flag_A:
            r.A.stop()
        if not flag_C:
            r.C.stop()

