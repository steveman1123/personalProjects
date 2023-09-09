#more advanced light blinker - uses keyboard input

from os import system as sys
import getKeys as gk
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)


#init key, light status, light pin
k = 0
out = 0b0
lightPin = 19


gpio.setup(lightPin, gpio.OUT)


#disable echo
sys("stty -echo")


print("Press Space to stop")

while k<>" ":
  k = gk.getkey() #.decode()
  if k=="s":
    #print(ord(k))
    out = ~out #toggle light
    gpio.output(lightPin, out) #write light
    time.sleep(0.5) #wait
  if k=="w":
    out = ~out
    gpio.output(lightPin, out)
    time.sleep(0.1)

#reenable echo
sys("stty echo")
