import RPi.GPIO as gpio
import time
import sys
import tkinter as tk
#from sensor import distance
from sensor import distance

var = 1

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    #gpio.setup(11, gpio.OUT)
    #gpio.setup(13, gpio.OUT)
    #gpio.setup(15, gpio.OUT)
    #gpio.cleanup()

while var == 1:
   # curDis = distance("cm")
   # print("Distance:", curDis)
   # time.sleep(1)

   # if curDis >50:
   #     init()
   #    gpio.output(7, True)

   # if curDis <50:
   #     init()
   #     gpio.output(7, False)

    curDis = distance("cm")
    print("Distance:", curDis)
    #time.sleep(1)

    if curDis >15:
        init()
        gpio.output(7, True)

    if curDis <15:
        init()
        gpio.output(7, False)
        

command = tk.Tk()
command.mainloop()


