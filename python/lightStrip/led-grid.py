#use this file on a 4x4 alternating led grid

#TODO: sest blackwhite to be monochrome intead and have specific values that can be set (as optional parameters)
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

import board,neopixel,time,random #,json
from adafruit_pixel_framebuf import PixelFramebuffer
import adafruit_fancyled.adafruit_fancyled as fancy


#lookup table for converting text into a 4x4 grid
#CHARS4X4 = json.loads(open("./4x4-chars.json",'r').read())
#TODO: add special chars to 4xM grid such as horizontal smiley and heart
#CHARS4XM = json.loads(open("./4xM-chars.json",'r').read())


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
    brightness=0.02,
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
      color2 = fancy.CHSV(((h+hoffset)%256),255,255).pack()
      updateFrame=time.time()
      pixel_framebuf.fill(fancy.CHSV(h+int(hoffset/2),255,50).pack())
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
      time.sleep(frameTime)
    isLeft= not isLeft #toggle the side

#outline the grid in one color, and fill the rest with another color
#h is the hue in HSV
#hstep is how different the hues are each frame
#blackwhite is a boolean determining if the colors should be black and white or in color
#dispTime is how long to display the pattern
#frameTime is how long to display the indivdual frames
def box(h=random.randint(0,256),hdiff=random.randint(20,235),hstep=5,blackwhite=False,dispTime=3,frameTime=0.05):
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
    pixel_framebuf.rect(1,1,pixel_width-2,pixel_height-2,c2)

    pixel_framebuf.display()
    time.sleep(frameTime)

#left and right halves of the grid are different colors
#h is the hue in HSV
#hdiff is the hue difference
#hstep is how different the hues are each frame
#dispTime is how long to display the pattern
#frameTime is how long to display the indivdual frames
def leftright(h=random.randint(0,256),hdiff=random.randint(15,240),hstep=5,blackwhite=False,dispTime=3,frameTime=0.05):
  startTime=time.time()
  while time.time()<startTime+dispTime:
    h = (h+hstep)%256
    if(blackwhite):
      c1 = fancy.CHSV(h,0,255*(h%2)).pack()
      c2 = fancy.CHSV(h,0,255*((h+1)%2)).pack()
    else:
      c1 = fancy.CHSV(h,255,255).pack()
      c2 = fancy.CHSV(h+hdiff,255,255).pack()

    pixel_framebuf.rect(0,0,int(pixel_width/2),pixel_height,c1)
    pixel_framebuf.rect(int(pixel_width/2),0,int(pixel_width/2),pixel_height,c2)
    pixel_framebuf.display()
    time.sleep(frameTime)

#top and bottom halves of the grid are different colors
#h is the hue in HSV
#hdiff is the hue difference
#hstep is how different the hues are each frame
#dispTime is how long to display the pattern
#frameTime is how long to display the indivdual frames
def topbot(h=random.randint(0,256),hdiff=random.randint(15,240),hstep=5,blackwhite=False,dispTime=3,frameTime=0.05):
  startTime=time.time()
  while time.time()<startTime+dispTime:
    h = (h+hstep)%256
    if(blackwhite):
      c1 = fancy.CHSV(h,0,255*(h%2)).pack()
      c2 = fancy.CHSV(h,0,255*((h+1)%2)).pack()
    else:
      c1 = fancy.CHSV(h,255,255).pack()
      c2 = fancy.CHSV(h+hdiff,255,255).pack()

    pixel_framebuf.rect(0,0,pixel_width,int(pixel_height/2),c1)
    pixel_framebuf.rect(0,int(pixel_height/2),pixel_width,int(pixel_height/2),c2)
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
def strips(isVert=False,h=random.randint(0,256),hdiff=random.randint(15,240),hstep=5,blackwhite=False,dispTime=3,frameTime=0.05):
  startTime=time.time()
  while time.time()<startTime+dispTime:
    h = (h+hstep)%256
    pixel_framebuf.fill(fancy.CHSV(h,255,255).pack())
    
    if(isVert):
      for c in range(pixel_width):
        if(blackwhite):
          color = fancy.CHSV(h,0,255*random.getrandbits(1)).pack()
        else:
          color = fancy.CHSV(h+(pixel_width-c)*hdiff,255,255).pack()
        pixel_framebuf.vline(c,0,pixel_height,color)
    else:
      for r in range(pixel_height):
        if(blackwhite):
          color = fancy.CHSV(h,0,255*random.getrandbits(1)).pack()
        else:
          color = fancy.CHSV(h+r*hdiff,255,255).pack()
        pixel_framebuf.hline(0,r,pixel_width,color)

    pixel_framebuf.display()
    time.sleep(frameTime)


#single pixels
#numDots is how many dots to show
#clearscreen is a bool that determines if the screen should be cleared between frames
#h is the hue in hsv
#hdiff is the difference between the colors of the dots
#hstep is how much the hue changes per frame
#blackwhite is a bool that says it should be black and white or color
#dispTime is how long to show the pattern
#frameTime is how long to show the individual frame
def dots(numDots=3,clearscreen=True,h=random.randint(0,256),hdiff=25,hstep=5,blackwhite=False,dispTime=3,frameTime=0.03):
  numDots = min(numDots,pixel_width*pixel_height-1)
  startTime=time.time()
  while time.time()<startTime+dispTime:
    h = (h+hstep)%256
    dots = [[random.randint(0,pixel_width),random.randint(0,pixel_height)] for _ in range(0,numDots)]

    if(clearscreen): pixel_framebuf.fill(0x000000)
    for i,dot in enumerate(dots):
      if(blackwhite):
        pixel_framebuf.pixel(dot[0],dot[1],fancy.CHSV(h,0,255*random.getrandbits(1)).pack())
      else:
        pixel_framebuf.pixel(dot[0],dot[1],fancy.CHSV(h+i*hdiff,255,255).pack())

    pixel_framebuf.display()
    time.sleep(frameTime)


#main function to run
def main():
  colorTime = 30 #how long to display colors
  bwTime = 10 #how long to display black and white

  timePerPattern = 3 #time to show each individual pattern, in seconds
  bwFrameTime = 0.1 #how long to display each frame while in the black & white state
  slowFrame = 0.07 #for frames that should be displayed slightly longer
  fastFrame = 0.03 #for frames that should be displayed slightly shorter

  #color patterns
  cpats = [
              'wipe(frameTime=fastFrame,hstep=50,dispTime=timePerPattern)',
              'rainbow(pattern="flat",dispTime=timePerPattern/2,step=random.randint(5,20),frameTime=fastFrame)',
              'rainbow(pattern="spiral",dispTime=timePerPattern/2,step=random.randint(50,150),frameTime=slowFrame)',
              'rainbow(pattern="spiral",dispTime=timePerPattern*2,step=random.randint(8,15),frameTime=slowFrame)',
              'box(hstep=random.randint(5,50),dispTime=timePerPattern*2)',
              'leftright(hstep=random.randint(5,50),dispTime=timePerPattern)',
              'boxes(frameTime=0.1,hstep=random.randint(5,50),dispTime=timePerPattern)',
              'strips(frameTime=0.1,hdiff=50,hstep=random.randint(5,50),dispTime=timePerPattern)',
              'strips(isVert=True,hdiff=75,frameTime=0.1,hstep=random.randint(5,50),dispTime=timePerPattern)',
              'topbot(hstep=random.randint(5,50),dispTime=timePerPattern)',
              'lines(delay1=0.1,delay2=0.07,dispTime=timePerPattern*2)',
              'dots(numDots=random.randint(2,7),hdiff=random.randint(25,200),clearscreen=True,dispTime=timePerPattern,frameTime=random.randint(3,20)/100)',
              'dots(numDots=3,clearscreen=False,dispTime=timePerPattern,frameTime=fastFrame)',
             ]
  #black & white patterns (makes it look glitchy)
  bwpats = [
            'box(frameTime=bwFrameTime,hstep=random.randrange(5,50,2),blackwhite=True,dispTime=random.randrange(1,timePerPattern))',
            'boxes(frameTime=bwFrameTime,blackwhite=True,hstep=random.randrange(5,50,2),dispTime=random.randrange(1,timePerPattern))',
            'strips(isVert=True,blackwhite=True,frameTime=bwFrameTime,hstep=random.randrange(5,50,2),dispTime=random.randrange(1,timePerPattern))',
            'strips(blackwhite=True,frameTime=bwFrameTime,hstep=random.randrange(5,50,2),dispTime=random.randrange(1,timePerPattern))',
            'topbot(blackwhite=True,frameTime=bwFrameTime,hstep=random.randrange(5,50,2),dispTime=random.randrange(1,timePerPattern))',
            'leftright(blackwhite=True,frameTime=bwFrameTime,hstep=random.randrange(5,50,2),dispTime=random.randrange(1,timePerPattern))',
            'dots(numDots=random.randint(2,7),blackwhite=True,hdiff=random.randint(25,200),clearscreen=True,dispTime=timePerPattern,frameTime=random.randint(3,20)/100)',
            'dots(numDots=3,blackwhite=True,clearscreen=False,dispTime=timePerPattern,frameTime=fastFrame)',
           ]
  #pixels.brightness = 0.5 #probably can max out flashlight level to this value
  while True:
    #randomly choose a pattern based on if it's black and white or color
    isBW = False #bool(random.getrandbits(1))

    #set how long the pattern type should be displayed TODO: this should be improved
    if(isBW):
      timePerPatternType = bwTime
    else:
      timePerPatternType = colorTime

    startTime = time.time()
    while time.time()<startTime+timePerPatternType:
      if(isBW):
        exec(random.choice(bwpats))
      else:
        exec(random.choice(cpats))
      
      #TODO: add GPIO switches/buttons here that change what's displayed based on the state
      #eg flashlight mode (red/white), speed controls, brightness control (too high can cause a lot of power draw though)

if(__name__=="__main__"):
  try:
    main()
  #clear the display if quit by keyboard
  except KeyboardInterrupt:
    pixel_framebuf.fill(0x000000)
    pixel_framebuf.display()

