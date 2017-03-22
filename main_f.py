import RPi.GPIO as gpio
import time
import sys
import tkinter as tk
from sensor import distance

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    
def forward():
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)

def stop():
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)
    gpio.cleanup()

def key_input(event):
    init()
    print("Key:", event.char)
    key_press = event.char
    sleep_time = 0.060
    
    if key_press.lower() == "w":
        forward()
    elif key_press.lower() == "p":
        stop() 
    else:
        pass

    curDis = distance("cm")
    print("Distance:", curDis)
    
    if curDis <15:
        init()
        stop()

    if curDis >15:
        init()
        forward()


command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()

    
