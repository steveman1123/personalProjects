'''
NOTE:
for movement, have 3 main directions:
fwd/rev - fwd only, rev = neg speed
tl/tr - rotational, cw only, ccw = neg cw
sl/sr - sr only, sl = neg sr
'''



#for tele-operation of a robot
#Steven Williams - 14.10.2018

import time
import getKeys as gk
from os import system as sys
import RPi.GPIO as gpio
import drive

#init
sys("stty echo")
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)


k = 0 #key var

motorPins = [6, 13, 19, 26] #motor pins

drive.init(motorPins)

addSpeed = 10

#program to continue running
print("\nPress SPACE to E-stop, press h for help\n")
while k<>" ":
  k = gk.getkey()
  if k=="w": #forwards
    drive.addFwd(addSpeed) #increase fwd DC by 5%
  elif k=="a": #left
    drive.addR(-addSpeed) #decrease right DC by 5%
  elif k=="s": #backwards
    drive.addFwd(-addSpeed)
  elif k=="d": #right
    drive.addR(addSpeed)
  elif k=="q": #ccw
    drive.addCW(-addSpeed)
  elif k=="e": #cw
    drive.addCW(addSpeed)
  elif k=="x": #stop
    drive.stop()
  elif k=="h": #help/controls
    print("w - forwards")
    print("a - straif left")
    print("s - backwards")
    print("d - straif right")
    print("q - CCW movement")
    print("e - CW movement")
    print("x - stop robot movement")
    print("h - this help menu")
    print("space - emergency stop")
  
  print(k, drive.getDC()[0], drive.getDC()[1], drive.getDC()[2], drive.getDC()[3])


sys("stty echo")
