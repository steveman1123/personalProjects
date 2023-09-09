import time
import RPi.GPIO as gpio

#blink light faster if button is pushed, else blink slow

btnPin = 21
lightPin = 20

out = 0b0

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)


gpio.setup(btnPin, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(lightPin, gpio.OUT)

while True:
  out = ~out
  if(gpio.input(btnPin)):
    time.sleep(0.1)
  else:
    time.sleep(1.0)
  gpio.output(lightPin, out)
