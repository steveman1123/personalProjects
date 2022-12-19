import board,neopixel

pin = board.D18 #set this to the pin the lights are connected to
numLights = 256 #set this to however many lights should get turned off

pixels = neopixel.NeoPixel(pin, numLights)
pixels.fill(0x000000)

