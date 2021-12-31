#use this to test the basic functionality of a light strip
#just cycles through RGB forever

import board,neopixel,time

pin = board.D18
numLights = 99

# define pixels
order = neopixel.GRB
pixels = neopixel.NeoPixel(pin, numLights, brightness=0.1, auto_write=False, pixel_order=order)

try:
  while True:
    #red
    print("test")
    print("R",end=" ")
    #pixels.fill((255,0,0))
    #pixels.show()
    time.sleep(1)
    #green
    print("G",end=" ")
    #pixels.fill((0,0,255))
    #pixels.show()
    time.sleep(1)
    #blue
    print("B")
    #pixels.fill((0,255,0))
    #pixels.show()
    time.sleep(1)

except KeyboardInterrupt:
  pixels.fill((0,0,0))
  pixels.show()
  print("\ndone")
