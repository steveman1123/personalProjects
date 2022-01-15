#use this file for a MxN led grid based on back and forth ws28xx led strips

import board,neopixel,time
from adafruit_pixel_framebuf import PixelFramebuffer

#lookup table for converting text into a 4x4 grid
#CHARS4X4 = json.loads(open("./4x4-chars.json",'r').read())

'''
https://cdn-learn.adafruit.com/downloads/pdf/easy-neopixel-graphics-with-the-circuitpython-pixel-framebuf-library.pdf

https://circuitpython.readthedocs.io/projects/pixel_framebuf/en/latest/examples.html

https://docs.micropython.org/en/v1.11/library/framebuf.html#class-framebufferhttps://docs.micropython.org/en/v1.11/library/framebuf.html
'''

pixel_pin = board.D18
pixel_width = 4
pixel_height = 4

pixels = neopixel.NeoPixel(
    pixel_pin,
    pixel_width * pixel_height,
    brightness=0.1,
    auto_write=False,
    pixel_order=neopixel.GRB
)

pixel_framebuf = PixelFramebuffer(
    pixels,
    pixel_width,
    pixel_height,
    alternating=True,
)

#fill with blue
#pixel_framebuf.fill(0x000088)
#set col 2, row 1 to be red
#pixel_framebuf.pixel(2, 1, 0xFF0000)
#set green line from top
#pixel_framebuf.line(0, 0, pixel_width - 1, pixel_height - 1, 0x00FF00)
#update display
#pixel_framebuf.display()

while True:
  for i in range(pixel_width):
    for j in range(pixel_height):
      pixel_framebuf.fill(0x000000)
      pixel_framebuf.pixel(i,j,0xFF0000)
      pixel_framebuf.display()
      time.sleep(0.125)