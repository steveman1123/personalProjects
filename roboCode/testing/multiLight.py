#pwm output for multiple lights using keyboard


import getKeys as gk
import RPi.GPIO as gpio

#set light pins, pwm duty cycle
pinsOut = [16, 12, 26, 13]
pwmDC = [0, 0, 0, 0]
#init keyboard var
k = 0


gpio.setmode(gpio.BCM)

#set pins as outputs
for i in pinsOut:
  gpio.setup(i, gpio.OUT)

#could probably throw in a loop
#set output pins as pwm
pwmPins = [gpio.PWM(pinsOut[0], 100), gpio.PWM(pinsOut[1], 100), gpio.PWM(pinsOut[2], 100), gpio.PWM(pinsOut[3], 100)]

#start pins
for i in range(len(pwmPins)):
  pwmPins[i].start(pwmDC[i])

while k<>" ":
  k = gk.getkey() #get keyboard input

  if k=="q":
    if pwmDC[0]+1 <= 100:
      pwmDC[0] += 1
  elif k=="a":
    if pwmDC[0]-1 >= 0:
      pwmDC[0] -= 1
  elif k=="w":
    if pwmDC[1]+1 <= 100:
      pwmDC[1] += 1
  elif k=="s":
    if pwmDC[1]-1 >= 0:
      pwmDC[1] -= 1
  elif k=="e":
    if pwmDC[2]+1 <= 100:
      pwmDC[2] += 1
  elif k=="d":
    if pwmDC[2]-1 >= 0:
      pwmDC[2] -= 1
  elif k=="r":
    if pwmDC[3]+1 <= 100:
      pwmDC[3] += 1
  elif k=="f":
    if pwmDC[3]-1 >= 0:
      pwmDC[3] -= 1
  
  print(k, pwmDC[0], pwmDC[1], pwmDC[2], pwmDC[3])
  for i in range(len(pwmPins)):
    pwmPins[i].ChangeDutyCycle(pwmDC[i])

