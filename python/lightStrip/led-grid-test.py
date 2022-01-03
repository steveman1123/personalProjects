#use this file for a MxN led grid based on back and forth ws28xx led strips

import board,neopixel,time,random,json
from adafruit_pixel_framebuf import PixelFramebuffer

#lookup table for converting text into a 4x4 grid
#CHARS4X4 = json.loads(open("./4x4-chars.json",'r').read())

'''
https://cdn-learn.adafruit.com/downloads/pdf/easy-neopixel-graphics-with-the-circuitpython-pixel-framebuf-library.pdf

https://circuitpython.readthedocs.io/projects/pixel_framebuf/en/latest/examples.html
'''

pixel_pin = board.D18
pixel_width = 4
pixel_height = 4

pixels = neopixel.NeoPixel(
    pixel_pin,
    pixel_width * pixel_height,
    brightness=0.1,
    auto_write=False,
)

pixel_framebuf = PixelFramebuffer(
    pixels,
    pixel_width,
    pixel_height,
    alternating=False,
)

pixel_framebuf.fill(0x000088)
pixel_framebuf.pixel(5, 1, 0xFFFF00)
pixel_framebuf.line(0, 0, pixel_width - 1, pixel_height - 1, 0x00FF00)
pixel_framebuf.display()