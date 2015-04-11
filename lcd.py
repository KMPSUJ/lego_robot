from ev3.ev3dev import Lcd
from PIL import Image,ImageDraw,ImageFont
import time
from ev3.ev3dev import Key
from ev3.ev3dev import Tone

class TestLcd():
    count = [0,0,0,0]
    pos = 0
    d = Lcd()
    k = Key()
    t =Tone()
    def test(self):
        d.draw.ellipse((20,20,60,60))
        d.update()
        time.sleep(2)
        d.reset()
        font = ImageFont.load_default()
        d.draw.text((10,10),"Hello", font=font)
        d.update()
    
    def prt(self):
        s = ""
        for i in range(self.pos):
            s = s+" "
        s=s+"^\n"+str(count[0])+str(count[1])+str(count[2])+str(count[3])+"\n"

        for i in range(self.pos):
            s = s+" "
        s=s+"_"
        return s
 

    def switch(self):
        while(1):
            d.draw.text((10,10),self.prt(),font=font)
            if(k.up):
                count[pos] = (count[pos]+1)%10
            if(k.down):
                count[pos] = (count[pos]-1)%10
            if(k.right):
                pos = (pos+1)%4
            if(k.left):
                pos = (pos-1)%4
            if(k.enter):
                srt = ''.join(srt(e) for e in count)
                t.play(int(str),500)
            if(k.backspace):
                break

TestLcd.test()
sleep(1)
TestLcd.switch()
        
        
