#use this file on a 4x4 alternating led grid

import board,neopixel,time,random,json
from adafruit_pixel_framebuf import PixelFramebuffer

#lookup table for converting text into a 4x4 grid
CHARS4X4 = json.loads(open("./4x4-chars.json",'r').read())

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


#scroll text from left to right (since built in framebuff text is 8x8 only, and I'm using 4x4, I need to use a custom one
def scrollText(text,scrollSpeed):
  return False




def main():
  
  while True:
    pixel_framebuf.pixel(0,0,0xFF0000)
    for col in range(pixel_width):
      pixel_framebuf.scroll(1,0)
      pixel_framebuf.display()
    for row in range(pixel_height):
      pixel_framebuf.scroll(0,1)
      pixel_framebuf.display()
      
  #while True:
    '''
    for col in range(pixel_width):
      for row in range(pixel_height):
        pixel_framebuf.fill(0x000000)
        pixel_framebuf.pixel(col,row,0xFF0000)
        pixel_framebuf.display()
        time.sleep(0.125)
    '''
    

if(__name__=="__main__"):
  try:
    main()
  #clear the display if quit by keyboard
  except KeyboardInterrupt:
    pixel_framebuf.fill(0x000000)
    pixel_framebuf.display()

