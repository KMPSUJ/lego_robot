from ev3.ev3dev import Lcd
from PIL import Image, ImageDraw, ImageFont
import time
from ev3.ev3dev import Key
from ev3.ev3dev import Tone
import os
from modules import Robot


class TestLcd():
    count = [1, 1, 0, 0, 0]
    pos = 0
    d = Lcd()
    k = Key()
    t = Tone()
    r = Robot.Robot()

    def test(self):
        self.d.draw.ellipse((20, 20, 60, 60))
        self.d.update()
        time.sleep(2)
        self.d.reset()
        font = ImageFont.load_default()
        self.d.draw.text((10, 10), "Hello", font=font)
        self.d.draw.text((20, 20), "World", font=font)
        self.d.draw.text((25, 25), "Hi", font=font)
        self.d.update()

    def prt(self):

        self.d.reset()
        font = ImageFont.load_default()
        s = ""
        for i in range(self.pos):
            s = s+" "
        s = s+"^"
        self.d.draw.text((10, 10), s, font=font)
        s = str(self.count[0])+str(self.count[1])
        s+=str(self.count[2])+str(self.count[3])+str(self.count[4])
        self.d.draw.text((10, 20), s, font=font)
        s = ""
        for i in range(self.pos):
            s = s+" "
        s = s+"v"
        self.d.draw.text((10, 30), s, font=font)
        self.d.update()

    def switch(self):
        self.r.S = 550
        while(1):
            self.prt()
            if(self.k.up):
                self.count[self.pos] = (self.count[self.pos]+1) % 10
            if(self.k.down):
                self.count[self.pos] = (self.count[self.pos]-1) % 10
            if(self.k.right):
                self.pos = (self.pos+1) % 5
            if(self.k.left):
                self.pos = (self.pos-1) % 5
            if(self.k.enter):
                s = ''.join(str(e) for e in self.count)
                self.r.turn(value=self.count[0], callibrate=(int(s[1:]))*0.001)
#               self.r.turn(value=1,callibrate=1)
            if(self.k.backspace):
                break
T = TestLcd()
# T.test()
time.sleep(1)
T.switch()
