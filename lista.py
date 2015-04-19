try:
    from modules import Robot as r
except:
    from modules import Robot_test as r
import math
import time
import random


class order():
    order_type = str()
    value = float()

    def __init__(self, tp='vd', val=0):
        self.order_type = tp
        self.value = val
        return

    # VoiD, ForWard, BacK, TurnRight, SetSpeed

    def __add__(x, y):
        ret = order()
        ret.order_type = x.order_type
        ret.value = x.value + y.value
        if x.order_type == 'ss':
            ret.value = y.value
        return ret

    def __iadd__(x, y):
        x = x+y
        return x

    def __repr__(x):
        return x.order_type+str(x.value)

    def __and__(x, y):
        return x.order_type == y.order_type


class o_list():
    def __repr__(l):
        return repr(l.L)

    def __getitem__(self, i):
        return self.L[i]

    L = []

    def cntr(self):
        i = 0
        while i < len(self.L)-1:
            if self.L[i] & self.L[i+1]:
                self.L[i] += self.L.pop(i+1)

    def cntr_i(self, a):
        if len(self.L) - 1 >= a:
            pass
        elif self.L[a] & self.L[a+1]:
            self.L[a] += self.L.pop(a + 1)

    def head(self, order):
        self.L.insert(0, order)
        if len(self.L) > 1:
            self.cntr_i(0)

    def tail(self, order):
        self.L.append(order)
        self.cntr_i(len(self.L)-2)

    def pop(self, i=0):
        return self.L.pop(i)


class execution():
    R = r.Robot()
    O = order()                 # active order
    L = o_list()                # list of future orders

    cntr_dic = {'fw': R.add_dist,
                'tr': R.add_turn}

    exe_dic = {'fw': R.run_dist,
               'tr': R.turn,
               'ss': R.set_speed,
               'vd': R.stop}

    passable = ['ss', 'vd']

    def __init__(self):
        self.R = r.Robot()
        self.R.startup()
        self.O = vd()

    def cntr(self):
        try:
            if self.O & self.L[0]:
                self.cntr_dic[self.O.order_type](self.L.pop())
        except:
            pass

    def exe(self):
        self.cntr()
        if self.R.still() or (self.O.order_type in self.passable):
            try:
                self.O = self.L.pop()
                self.exe_dic[self.O.order_type](self.O.value)
            except:
                self.R.shutdown()

    def stop(self):
        self.R.stop()
        self.O.order_type = 'vd'
        return self.R.left_dist()

    def loop(self):
        k = 0
        self.L.tail(fw(2000))
        while(True):
            time.sleep(.1)
            if self.R.check_obstacle():
                self.R.obstacle()
                self.R.stop()
                self.L.tail(fw(max(self.stop())))
                self.L.head(tr(1/6.0 + 0.25 * random.random()))
                self.L.head(bk(1))
                k += 1
            else:
                self.R.start()
                self.exe()
            if (k > 10) or self.R.K.backspace:
                    self.R.shutdown()

"""while(True):
        time.sleep(.1)
        if(R.check_obstacle()):
            R.obstacle()
            k = k+1
        else:
            R.start()
        #   k = 0
            if(k > 10):
            R.shutdown()"""


class give_order():
    global tl, tr, tp, ss, fw, vd, bk

    def fw(val):                # ForWard
        return order('fw', val)

    def vd(val=0):            # VoiD
        return order('vd', val)

    def bk(val):                # Back
        return order('fw', -val)

    def tl(val=0.25):         # TurnLeft
        return order('tr', -val)

    def tr(val=0.25):         # TurnRight
        return order('tr', val)

    def tp(val):                # Turn to Position (the shortest turn)
        val = math.modf(val)[0]
        if val > 0.5:
            val = -val
        return order('tr', val)

    def ss(val=600):            # SetSpeed
        return order('ss', val)


'''l = list()
l.cntr()
print (l.L)
O = order()
O.value=10
O1 = order()
O1.value = 10
O2 = O+O1
print (O2.value)
O+=O2
print (O.value)
print (O.order_type)
print (repr(O))
O = 'fw10'''
e = execution()
e.loop()
