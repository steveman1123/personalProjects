#use this to test the basic functionality of a light strip
#just cycles through RGB forever

import board,neopixel,time,sys


#must give the number of pixels as an integar argument
if(len(sys.argv)==2):
  numLights = int(sys.argv[1])
else:
  raise ValueError("Must have exactly 1 argument of the number of pixels")

#set the output pin to GPIO 18 - see: https://pinout.xyz/
pin = board.D18

# define pixels
order = neopixel.GRB
pixels = neopixel.NeoPixel(pin, numLights, brightness=0.1, auto_write=False, pixel_order=order)

try:
  while True:
    #red
    print("R",end="",flush=True)
    pixels.fill((255,0,0))
    pixels.show()
    time.sleep(1)
    #green
    print("G",end="",flush=True)
    pixels.fill((0,0,255))
    pixels.show()
    time.sleep(1)
    #blue
    print("B")
    pixels.fill((0,255,0))
    pixels.show()
    time.sleep(1)
    
    pixels.fill((0,0,0))
    for i in range(len(pixels)):
      pixels[-(i+1)] = (255,0,0)
      pixels.show()
      time.sleep(0.25)
    pixels.fill((0,192,255))
    time.sleep(1)

except KeyboardInterrupt:
  pixels.fill((0,0,0))
  pixels.show()
  print("\ndone")
