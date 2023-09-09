#driving functions for quad omni wheel drive train
#50% DC is a stop

import RPi.GPIO as gpio

pwmPins = [0, 0, 0, 0]
pwmDC = [50, 50, 50, 50]

#updates the pwm outputs
def updateSpeeds():
  for i in range(len(pwmPins)):
    if pwmDC[i] > 100:
      pwmDC[i] = 100
    elif pwmDC[i] < 0:
      pwmDC[i] = 0
    pwmPins[i].ChangeDutyCycle(pwmDC[i])


#set pwmPins as motorPins, then as PWM output, and activate
def init(motorPins):
  gpio.setup(motorPins, gpio.OUT)

  for i in range(len(pwmPins)):
    pwmPins[i] = gpio.PWM(motorPins[i], 100)
    pwmPins[i].start(pwmDC[i])



def addFwd(amt):
  pwmDC[0] += amt
  pwmDC[2] -= amt
  updateSpeeds()

def addR(amt):
  pwmDC[1] += amt
  pwmDC[3] -= amt
  updateSpeeds()

def addCW(amt):
  #may be able to remove this loop - learn about addition to arrays in python
  for i in range(len(pwmDC)):
    pwmDC[i] += amt
  '''
  pwmDC[0] = 70
  pwmDC[1] = 30
  pwmDC[2] = 70
  pwmDC[3] = 30
  '''
  updateSpeeds()

#stop all motors
def stop():
  for i in range(len(pwmDC)):
    pwmDC[i] = 50
  updateSpeeds()


def getDC():
  return pwmDC
