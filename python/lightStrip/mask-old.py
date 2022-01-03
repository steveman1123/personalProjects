#use this file for a MxN led grid based on back and forth ws28xx led strips
#intended use is for a light-up mask
'''
>>>>-dataout
<<<<
>>>>
<<<<-datain
'''

import board,neopixel,time,random,json
#TODO: use csv reader since pandas/numpy is a bit heavy for this (or use json instead)
#from pandas import read_csv

#lookup table for converting text into a 4x4 grid
CHARS4X4 = "" #read_csv("./4x4-chars.csv")


#convert grid type to pixel type and display
#isleft determines if the bottom left is the starting point or the bottom right
'''
isleft:
678
543
012

!isleft:
876
345
210
'''
def updateStrip(grid,pixels,isleft=True,verbose=False):
  #init row and col numbers
  rs = len(grid)
  cs = len(grid[0])
  #for each row
  for r,cols in enumerate(grid):
    #for each column
    for c,pt in enumerate(cols):
      #set the index according to the left/right alignment
      #TODO: this could be made into a single statement to the effect of:
      # idx = (rs-(r+(r+(int(not isleft)))%2))*cs-(c+(r+(int(isleft))%2))
      #if using that statement, add additional comments to decompose how it works
      if(isleft):
        idx = (rs-(r+r%2))*cs-(c+(r+1)%2)
      else:
        idx = (rs-(r+(r+1)%2))*cs-(c+r%2)
      if(verbose): print(rs,cs,r,c,idx) #debug
      pixels[idx] = pt #set the pixel color

  pixels.show() #show the pixels
  if(verbose):
    for r in grid: print(r) #debug



#set all values in the grid to 0
def clearGrid(grid):
  return [[(0,0,0)]*len(grid[0])]*len(grid)

#set the whole strip to a single color (0,0,0) for clearing
def setStripColor(pixels,color):
  pixels.fill(color)
  pixels.show()


#box outlined on the grid
#where grid is a list of lists of tuples
#and color is a tuple length 3
def box(grid,color):
  grid = clearGrid(grid) #start from scratch
  [grid[0],grid[-1]] = [[color]*len(grid[0])]*2 #top and bottom rows
  [grid[1][0],grid[1][-1]] = [color]*2 #first and last column (of first row)
  grid[2:-1] = [grid[1]]*(len(grid)-3) #all the rest of the rows
  return grid



#display alphanumeric text scrolling from right to left
#text is a string to display consisting only of characters present in the lookup table
#grid is the nxm grid
#pixels is the neopixels to output to
#color is the color to display the text as (tuple length 3)
#delay is how long (in seconds) to disply a frame for

#TODO: redo this whole thing so it can use bitshifting and such to speed it up
def scrollText(text,grid,pixels,color,delay=0.125):
  #convert text using a lookup table of characters
  #run this function until end of string is reached
  #if invalid char is passed, just skip it
  text = text.lower() #ensure lowercase since lookup table is in lowercase
  gridcharlist = [] #list of grid array of characters
  #generate the grid char list
  for ch in text:
    tablechar = CHARS4X4[CHARS4X4['char']==ch]
    if(len(tablechar==1)): #ensure character is present
      gridchar = tablechar[0]['grid'].split("|")
      gridchar = [list(e) for e in gridchar] #turn the data into the grid list of lists
      gridchar = [[color if pt=="1" else (0,0,0) for pt in row] for row in gridchar]
      gridcharlist.append(gridchar)
  
  for ch in gridcharlist:
    for l in range(len(grid[0])*3):
      gridout = None
    
      updateStrip(gridout,pixels)
      time.sleep(delay)


#set the columns of the grid to certain colors
#where grid is an MxN list of lists
#colColors is a list of colors
def cols(grid,colColors):
  #if gridCols>colColors: repeat colors
  #if colColors>gridCols: use cols

  #fit the column colors to the columns
  fittedColors = [colColors[c%len(colColors)] for c in range(len(grid[0]))]

  for r in range(len(grid)):
    grid[r] = fittedColors
  return grid


def rows(grid,rowColors):
  #fit colors to rows of the grid
  fittedColors = [rowColors[r%len(rowColors)] for r in range(len(grid))]
  #apply colors to grid
  for r in range(len(grid)):
    grid[r] = [fittedColors[r]]*len(grid[r])
  return grid


def main(verbose=False):
  #number of led rows
  rows=4
  #number of leds per row
  cols=4
  #use a matrix/grid style display
  grid=[[(0,0,0)]*cols]*rows
  for r in grid: print(r)
  pin = board.D18
  numLights = int(rows*cols)
  
  # define pixels
  order = neopixel.GRB
  pixels = neopixel.NeoPixel(pin, numLights, brightness=0.1, auto_write=False, pixel_order=order)
  
  while True:
    #make a box on the grid fading in from black to red
    for c in range(0,255):
      grid = box(grid,(c,0,0))
      updateStrip(grid,pixels)
      time.sleep(0.05)
    
    grid = box(grid,(0,255,0))
    updateStrip(grid,pixels)
    time.sleep(2)
    grid = clearGrid(grid)
    updateStrip(grid,pixels)
    time.sleep(2)
    


if(__name__=='__main__'):
  try:
    
    main()
  except KeyboardInterrupt:
    
