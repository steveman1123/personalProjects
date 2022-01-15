#use this file on a 4x4 alternating led grid

#TODO: standardize output and functions so that they can be performed back to back
'''
structure should look something like this:
while True:
  clear display
  set buffer content/pattern based on time or pattern content
  update display

pattern functions should saved states
they should focus on one frame at a time (no loops except for displaying for that frame)
should take in base color from the global hue variable
'''

import board,neopixel,time,random,json
from adafruit_pixel_framebuf import PixelFramebuffer
import adafruit_fancyled.adafruit_fancyled as fancy


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
    brightness=0.05,
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


#display a rainbow like in the infinity mirror
#h is the base hue
#s and v are saturation and v (respectively) - default to max
#step is how much of a difference between the hues there should be
#pattern is what shape the rainbow should take
#flat (fill), spiral (set to a low step for spiral shape, high step for pseudorandom colors
#dispTime is how long to display the pattern
#frameTime is how long to display the individual frames
def rainbow(h=random.randint(0,256),step=5,pattern="flat",dispTime=3,frameTime=0.05):
  validpatterns=['flat','spiral']
  
  startTime=time.time()
  while time.time()<startTime+dispTime:
    h = (h+step)%256
    if(pattern=="flat" or pattern not in validpatterns):
      pixel_framebuf.fill(fancy.CHSV(h,255,255).pack())
    elif(pattern=="spiral"):
      #TODO: this should be put into a couple loops instead of every line (and loops should be dependent on frame size
      pixel_framebuf.pixel(0,0,fancy.CHSV(h,255,255).pack())
      pixel_framebuf.pixel(1,0,fancy.CHSV((h+step)%256,255,255).pack())
      pixel_framebuf.pixel(2,0,fancy.CHSV((h+step*2)%256,255,255).pack())
      pixel_framebuf.pixel(3,0,fancy.CHSV((h+step*3)%256,255,255).pack())
      pixel_framebuf.pixel(3,1,fancy.CHSV((h+step*4)%256,255,255).pack())
      pixel_framebuf.pixel(3,2,fancy.CHSV((h+step*5)%256,255,255).pack())
      pixel_framebuf.pixel(3,3,fancy.CHSV((h+step*6)%256,255,255).pack())
      pixel_framebuf.pixel(2,3,fancy.CHSV((h+step*7)%256,255,255).pack())
      pixel_framebuf.pixel(1,3,fancy.CHSV((h+step*8)%256,255,255).pack())
      pixel_framebuf.pixel(0,3,fancy.CHSV((h+step*9)%256,255,255).pack())
      pixel_framebuf.pixel(0,2,fancy.CHSV((h+step*10)%256,255,255).pack())
      pixel_framebuf.pixel(0,1,fancy.CHSV((h+step*11)%256,255,255).pack())
      pixel_framebuf.pixel(1,1,fancy.CHSV((h+step*12)%256,255,255).pack())
      pixel_framebuf.pixel(2,1,fancy.CHSV((h+step*13)%256,255,255).pack())
      pixel_framebuf.pixel(2,2,fancy.CHSV((h+step*14)%256,255,255).pack())
      pixel_framebuf.pixel(1,2,fancy.CHSV((h+step*15)%256,255,255).pack())
    pixel_framebuf.display()
    time.sleep(frameTime)

#2 lines criscrossing at different speeds constantly changing colors
#h is the hue in HSV
#hstep is how fast the hue should change per frame
#hoffset is how different the two lines should be
#delay1 is how often the first line should move (in sec)
#delay2 is how often the second line should move (in sec)
#fps is how often the display should be updated
#dispTime is how long to display the pattern for
def lines(hstep=1,hoffset=127,delay1=0.3,delay2=0.1,fps=30,dispTime=3):
  h=random.randint(0,256)
  line1up=True
  x1=y1=0

  line2up=False
  x2=y2=pixel_width

  startTime1=startTime2=updateFrame=startTime=time.time()
  while time.time()<startTime+dispTime:
    if(round(time.time()-startTime1,2)>=delay1):
      startTime1=time.time()
      if(line1up):
        x1+=1
        if(x1>=pixel_width*2-2): line1up=False
      else:
        x1-=1
        if(x1<=0): line1up=True
      y1=int(x1*pixel_height/pixel_width)
    
    
    if(round(time.time()-startTime2,2)>=delay2):
      startTime2=time.time()
      if(line2up):
        x2+=1
        if(x2>=pixel_width-1): line2up=False
      else:
        x2-=1
        if(x2<=-pixel_width+1): line2up=True
      y2=pixel_height-1
    
    if(round(time.time()-updateFrame,2)>=round(1/fps,2)):
      h=(h+1)%256
      color1 = fancy.CHSV(h,255,255).pack()
      color2 = fancy.CHSV(((h+127)%256),255,255).pack()
      updateFrame=time.time()
      pixel_framebuf.fill(fancy.CHSV(h+64,255,64).pack())
      pixel_framebuf.line(x1,0,0,y1,color1)
      pixel_framebuf.line(x2,0,pixel_width-1+x2,y2,color2)
      pixel_framebuf.display()


#wipe the colors across the screen alternating from the top left and top right
#h is the hue in hsv
#hstep is how much the color should change per wipe
#frameTime is how long to display each individual frame
#dispTime is how long to display the pattern
def wipe(h=random.randint(0,256),hstep=20,frameTime=0.1,dispTime=3):
  startTime=time.time()
  isLeft=True
  while time.time()<startTime+dispTime:
    h = (h+hstep)%256
    
    for i in range(2*pixel_width):
      if(isLeft):
        x=pixel_width*2-i-1
        pixel_framebuf.line(x,0,x-pixel_height,pixel_height,fancy.CHSV(h,255,255).pack())
      else:
        x=i
        pixel_framebuf.line(x-pixel_width,0,x,pixel_height,fancy.CHSV(h,255,255).pack())

      pixel_framebuf.display()
      time.sleep(frametime)
    isLeft= not isLeft #toggle the side

#outline the grid in one color, and fill the rest with another color
#h is the hue in HSV
#hstep is how different the hues are each frame
#dispTime is how long to display the pattern
#frameTime is how long to display the indivdual frames
def box(h=random.randint(0,256),hstep=5,dispTime=3,frameTime=0.05):
  startTime=time.time()
  while time.time()<startTime+dispTime:
    h = (h+hstep)%256
    pixel_framebuf.fill(fancy.CHSV(h,255,255).pack())
    pixel_framebuf.rect(1,1,pixel_width-2,pixel_height-2,fancy.CHSV((h+127)%256,255,255).pack())
    pixel_framebuf.display()
    time.sleep(frameTime)

#left and right halves of the grid are different colors
#h is the hue in HSV
#hdiff is the hue difference
#hstep is how different the hues are each frame
#dispTime is how long to display the pattern
#frameTime is how long to display the indivdual frames
def leftright(h=random.randint(0,256),hdiff=random.randint(15,240),hstep=5,dispTime=3,frameTime=0.05):
  startTime=time.time()
  while time.time()<startTime+dispTime:
    h = (h+hstep)%256
    pixel_framebuf.rect(0,0,int(pixel_width/2),pixel_height,fancy.CHSV(h,255,255).pack())
    pixel_framebuf.rect(int(pixel_width/2),0,int(pixel_width/2),pixel_height,fancy.CHSV(h+hdiff,255,255).pack())
    pixel_framebuf.display()
    time.sleep(frameTime)

#top and bottom halves of the grid are different colors
#h is the hue in HSV
#hdiff is the hue difference
#hstep is how different the hues are each frame
#dispTime is how long to display the pattern
#frameTime is how long to display the indivdual frames
def topbot(h=random.randint(0,256),hdiff=random.randint(15,240),hstep=5,dispTime=3,frameTime=0.05):
  startTime=time.time()
  while time.time()<startTime+dispTime:
    h = (h+hstep)%256
    pixel_framebuf.rect(0,0,pixel_width,int(pixel_height/2),fancy.CHSV(h,255,255).pack())
    pixel_framebuf.rect(0,int(pixel_height/2),pixel_width,int(pixel_height/2),fancy.CHSV(h+hdiff,255,255).pack())
    pixel_framebuf.display()
    time.sleep(frameTime)

#grid quadrants are two different colors (can also be set to being black and white)
#h is the hue in HSV
#hdiff is the hue difference
#hstep is how different the hues are each frame
#dispTime is how long to display the pattern
#frameTime is how long to display the indivdual frames
def boxes(h=random.randint(0,256),hdiff=random.randint(15,240),hstep=5,blackwhite=False,dispTime=3,frameTime=0.05):
  startTime=time.time()
  while time.time()<startTime+dispTime:
    h = (h+hstep)%256
    if(blackwhite):
      c1 = fancy.CHSV(h,0,255*(h%2)).pack()
      c2 = fancy.CHSV(h,0,255*((h+1)%2)).pack()
      
    else:
      c1 = fancy.CHSV(h,255,255).pack()
      c2 = fancy.CHSV(h+hdiff,255,255).pack()
    pixel_framebuf.fill(c1)
    pixel_framebuf.rect(0,0,int(pixel_width/2),int(pixel_height/2),c2)
    pixel_framebuf.rect(int(pixel_width/2),int(pixel_height/2),pixel_width,pixel_height,c2)

    pixel_framebuf.display()
    time.sleep(frameTime)


#alternating strips that are either horizontal or vertical
#isVert determines if the stripes are verticle or horizontal
#h is the hue in HSV
#hdiff is the hue difference
#hstep is how different the hues are each frame
#dispTime is how long to display the pattern
#frameTime is how long to display the indivdual frames
def strips(isVert=False,h=random.randint(0,256),hdiff=random.randint(15,240),hstep=5,dispTime=3,frameTime=0.05):
  startTime=time.time()
  while time.time()<startTime+dispTime:
    h = (h+hstep)%256
    pixel_framebuf.fill(fancy.CHSV(h,255,255).pack())
    
    if(isVert):
      for c in range(int(pixel_width/2)):
        pixel_framebuf.vline(2*c,0,pixel_height,fancy.CHSV(h+hdiff,255,255).pack())
    else:
      for r in range(int(pixel_height/2)):
        pixel_framebuf.hline(0,2*r,pixel_width,fancy.CHSV(h+hdiff,255,255).pack())

    pixel_framebuf.display()
    time.sleep(frameTime)


#main function to run
def main():
  timePerPattern = 3 #time to show each pattern, in seconds
  #cycle through these patterns
  patterns = [
              'wipe(frametime=0.03,hstep=25,dispTime=timePerPattern)',
              'rainbow(pattern="flat",dispTime=timePerPattern/2,step=random.randint(5,50),frameTime=0.03)',
              'rainbow(pattern="spiral",dispTime=timePerPattern/2,step=random.randint(50,150),frameTime=0.05)',
              'box(hstep=random.randint(5,50),dispTime=timePerPattern)',
              'leftright(hstep=random.randint(5,50),dispTime=timePerPattern)',
              'boxes(frameTime=0.1,hstep=random.randint(5,50),dispTime=timePerPattern)',
              'boxes(frameTime=0.1,blackwhite=True,hstep=random.randrange(5,50,2),dispTime=timePerPattern/2)',
              'strips(frameTime=0.1,hstep=random.randint(5,50),dispTime=timePerPattern)',
              'strips(isVert=True,frameTime=0.1,hstep=random.randint(5,50),dispTime=timePerPattern)',
              'topbot(hstep=random.randint(5,50),dispTime=timePerPattern)',
              'lines(delay1=0.1,delay2=0.07,dispTime=timePerPattern)',
              'rainbow(pattern="spiral",dispTime=timePerPattern,step=random.randint(8,15),frameTime=0.07)',
             ]
  #randomly choose a pattern
  while True:
    exec(random.choice(patterns))


if(__name__=="__main__"):
  try:
    main()
  #clear the display if quit by keyboard
  except KeyboardInterrupt:
    pixel_framebuf.fill(0x000000)
    pixel_framebuf.display()

