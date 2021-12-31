# This script updates some neopixel lights with some functions
#TODO: make this an object with the pin and numLights (or just the strip) passed through


import board, neopixel, time

pin = board.D18
numLights = 99

'''
class lightStrip:
  def __init__(self,numLights,pin=board.D18):
    self.pin = pin
    self.numLights = numLights
'''
  

# define pixels
order = neopixel.GRB
pixels = neopixel.NeoPixel(pin, numLights, brightness=0.2, auto_write=False, pixel_order=order)

#lights that are dead or partially dead, in this strip, only the red lights here are dead
deadR = [0,1,2,4,5,6,7,8,9,10,11,13,15,17,19,20,23,25,27,28,35,36,38,39,45,52,80]
#deadG = []
#deadB = []

col = {
'r':(0,255,0),
'o':(80,255,0),
'y':(180,216,0),
'g':(255,0,0),
'b':(0,0,255),
'i':(0,64,255),
'v':(0,192,255),

'w':(255,255,255), #white
'p':(20,255,100), #pink
'c':(192,0,255) #cyan
}


### functions primarily used by the main functions use

#turn off dead lights
def clearDead():
  for e in deadR:
    if(pixels[e][1]>0): #only turn off lights using red
      pixels[e] = (0,0,0)


def updateLights():
  clearDead()
  pixels.show()
  time.sleep(0.1) #let lights settle for a moment before trying to update again

def clearLights():
  pixels.fill((0,0,0))
  updateLights()

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


#fade a pixel from its current color to a desired color at a given step (default 1)
def fade2color(pixelNum, color, step=1):
  start = pixels[pixelNum]
  for i in range(3): #3 color channels
    if(start[i]<color[i]):
      start[i] += min(step,color[i]-start[i])
    elif(start[i]>color[i]):
      start[i] -= min(step,start[i]-color[i])
  pixels[pixelNum] = start
  clearDead()
  return tuple(start)==tuple(color) #return status if light reached desired color


#fade the whole strip to another strip colorset - colorset should be same size as strip
def fadeStrip(newStrip, step=1): #newStrip should be a list of 3 value color tuples [(x,x,x),(x,x,x),...]
  #TODO: add error checking to make sure newStrip is same length as pixels
  for i,e in enumerate(newStrip):
    fade2color(i,e,step)
  return (sum([tuple(e)==(0,0,0) or e==newStrip[i] for i,e in enumerate(list(pixels))]) == numLights)






### main functions

#fill every nth light with a color from the color list and fill some number of lights with that color
def everyNthLight(colorList,lightsPerColor):
  pattern = ()
  for e in colorList:
    pattern = (pattern+(e,)*lightsPerColor)
  pixels[0:numLights] = (pattern*int(numLights/len(pattern)+1))[0:numLights] #loop pattern till filled, then trim off extra
  return list(pixels)

def color_chase(color, wait):
  for i in range(numLights):
    pixels[i] = color
    time.sleep(wait)
    updateLights()


def rainbow_cycle(wait):
  for j in range(255):
    for i in range(numLights):
      rc_index = (i * 256 // numLights) + j
      pixels[i] = wheel(rc_index & 255)
    updateLights()




#build up a tower of pixels till it's full, then clear and restart
#c is the color to use, default to cyan
#size is number of pixels to add at a time, default to 1
def pixTower(c=col['c'],size=1):
  clearLights()
  for i in range(0,numLights,size):
    pixels[0:i] = (c,)*(i) #display tower
    for j in range(numLights-1,i-1,-1):
      pixels[j] = c
      if(j<len(pixels)-size): #clear out previous one to make a dot
        pixels[j+size] = (0,0,0) #clear the one before to make a dot
      updateLights()
  for i in range(3): #flash lights at end
    clearLights()
    time.sleep(0.1)
    pixels.fill(c)
    updateLights()
    time.sleep(0.1)
  time.sleep(0.75)
  clearLights()
