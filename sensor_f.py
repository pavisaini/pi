import RPi.GPIO as gpio
import time

#gpio.setwarnings(False) 
gpio.cleanup()

def distance(measure='cm'):
    gpio.setmode(gpio.BOARD)
    gpio.setup(35, gpio.OUT)
    gpio.setup(36, gpio.IN)
  
    time.sleep(0.3)
    gpio.output(35, True)
    time.sleep(0.00001)
    
    gpio.output(35, False)
    while gpio.input(36) == 0:
        nosig = time.time()
    
    while gpio.input(36) == 1:
        sig = time.time()
    
    tl = sig - nosig
    
    if measure == 'cm':
        distance = tl / 0.000058
    elif measure == 'in':
        distance = tl / 0.000148
    else:
        print('Improper choice of measurement: in or cm')
        distance = None
    
    gpio.cleanup()
    return distance
  
print(distance('cm'))
#time.sleep(1)    
