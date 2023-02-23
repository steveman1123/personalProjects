#test gpio PWMs


import RPi.GPIO as gpio
import time
import getKeys as gk

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

k = 0

lightPin = 16
gpio.setup(lightPin, gpio.OUT)
light = gpio.PWM(lightPin, 300)
light.start(0) #dc = 0 thru 100


'''
for j in range(0,3):
  for i in range(0, 100, 1):
    light.ChangeDutyCycle(i)
    time.sleep(0.01)
  for i in range(100, 0, -1):
    light.ChangeDutyCycle(i)
    time.sleep(0.01)
'''

dc = 0


print("Press SPACE to stop")
while k<>" ":
  k = gk.getkey()
  if k=="w":
    dc=0
  elif k=="s":
    dc=100
  elif k=="a":
    if dc>0:
      dc=dc-1
  elif k=="d":
    if dc<100:
      dc=dc+1

  light.ChangeDutyCycle(dc)

gpio.cleanup()
