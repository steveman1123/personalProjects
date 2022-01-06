#use this file on a 4x4 alternating led grid

import board,neopixel,time,random,json
from adafruit_pixel_framebuf import PixelFramebuffer

#lookup table for converting text into a 4x4 grid
CHARS4X4 = json.loads(open("./4x4-chars.json",'r').read())
#TODO: add special chars to 4xM grid such as horizontal smiley and heart
CHARS4XM = json.loads(open("./4xM-chars.json",'r').read())


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


#flash characters one at a time on the grid
#where text is a string of valid characters
#color is the text color
#back color is the background color
#ontime is how long each char should be displayed for (in sec)
#offtime is how long of a wait between characters
#TODO: fix constants so it actually makes sense (currently rows and columns are swapped I think)
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

#scroll text but only 1 character at a time
#text is a string of characters
#color is the character color
#backcolor is the background color
#delay is how long to show each frame (in seconds)
def scroll1char(text,color,backcolor,delay=0.2):
  for char in text.lower(): #ensure it's lowercase since the chars is all in lowercase
    #ensure char is in CHARS
    chargrid = [e['grid'].split("|") for e in CHARS4X4 if e['char']==char][0]
    if(len(chargrid)>0):
      #clear display (set to back color)
      pixels.fill(backcolor)
      #for each column in text*2: #*2 since it starts off screen and ends off screen
      for col in range(2*len(chargrid[0])):
        #shift
        pixel_framebuf.scroll(-1,0)
        #assign new right column
        if(col<len(chargrid[0])):
          for r,row in enumerate(chargrid):
            if(int(row[col])):
              pixel_framebuf.pixel(pixel_width-1,pixel_height-1-r,color)
            else:
              pixel_framebuf.pixel(pixel_width-1,pixel_height-1-r,backcolor)
        else:
          pixel_framebuf.vline(pixel_width-1,0,pixel_height,backcolor) #avoid leaving a trace after scrolling
        #update display
        pixel_framebuf.display()
        #delay
        time.sleep(delay)


def scrollChars(text,color,backcolor,delay=0.15):
  #get all the grids for each valid char into a list
  #comes out as a format of [[row1,row2,row3,row4]...]
  grids = [[e['grid'].split("|") for e in CHARS4XM if e['char']==char][0] for char in text.lower()]
  #transform the list into a list of columns
  #comes out as a format of [col1,col2,col3,col4,col5...]
  #print(grids)
  #TODO: add an empty column if the last column of a character is not empty
  gridcols = [["".join([e[i] for e in g]) for i in range(len(g[0]))] for g in grids]
  gridcols = [e if e[-1]=='0000' else e+["0000"] for e in gridcols]
  gridcols = [e for g in gridcols for e in g] #idk how this works, but I got it from here: https://datascienceparichay.com/article/python-flatten-a-list-of-lists-to-a-single-list/
  #print(gridcols)
  for c in gridcols:
    #shift
    pixel_framebuf.scroll(-1,0)
    #set the rightmost column to the new column
    for r,px in enumerate(c):
      if(int(px)):
        pixel_framebuf.pixel(pixel_width-1,pixel_height-1-r,color)
      else:
        pixel_framebuf.pixel(pixel_width-1,pixel_height-1-r,backcolor)
    #display
    pixel_framebuf.display()
    #delay
    time.sleep(delay)


#display a rainbow
def rainbow():


def main():
  
  
  
  '''
  #test proper text scrolling
  while True:
    #scrollChars("hello, world.  How are you?    ",0xFF0000,0x000000)
    #scrollChars("Hello there!   ",0xFF0000,0x000000,delay=0.1)
    scrollChars(":) <3 ",0x000080,0x000000,delay=0.25)
  '''

  '''
  #test single character displaying
  while True:
    dispChars("test  ",0x0000FF,0x000000)
  '''


  '''
  #test single character scrolling
  while True:
    scroll1char("hello ",0x00FFAA,0x330000,delay=0.2)
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

