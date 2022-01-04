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


#flash characters one at a time on the grid
#where text is a string of valid characters
#color is the text color
#back color is the background color
#ontime is how long each char should be displayed for (in sec)
#offtime is how long of a wait between characters
def dispChars(text,color,backcolor,ontime=0.25,offtime=0.05):
  for char in text.lower(): #esure lowercase since CHARS4X4 is all in lowercase
    chargrid = [e['grid'].split("|") for e in CHARS4X4 if e['char']==char][0]
    if(len(chargrid)>0): #only display if the character is valid, else skip it as if it wasn't there in the first place
      for c,col in enumerate(chargrid):
        for r,px in enumerate(col):
          if(int(px)):
            pixel_framebuf.pixel(r,pixel_width-1-c,color)
          else:
            pixel_framebuf.pixel(r,pixel_width-1-c,backcolor)
      pixel_framebuf.display()
      print(char)
      time.sleep(ontime)
      pixel_framebuf.fill(0x000000)
      pixel_framebuf.display()
      time.sleep(offtime)


def main():
  
  while True:
    dispChars("the quick brown fox jumps over the lazy dog.  ",0x0000FF,0x000000)

  '''
  #test scrolling
  while True:
    pixel_framebuf.pixel(0,0,0xFF0000)
    for col in range(pixel_width):
      pixel_framebuf.scroll(1,0)
      tmpbuf = pixel_framebuf
      pixel_framebuf.fill(0x000000)
      pixel_framebuf = tmpbuf
      pixel_framebuf.display()
      time.sleep(1)
    for row in range(pixel_height):
      pixel_framebuf.scroll(0,1)
      pixel_framebuf.display()
      time.sleep(1)
      
  '''
  '''
  #initial test
  while True:
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

