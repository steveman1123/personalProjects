import lightFxns as l

def main():

  #halloween colors (red for blood, orange and purple
  endSet = l.everyNthLight([l.col['r']],1)
  startSet = l.everyNthLight([l.col['o'],l.col['p']],1)
  
  l.updateLights()
  
  #run the fade strip once
  runFadeStrip(startSet, endSet, -1)

  #run the pix tower with 2 lights, 3 times
  runTower(20,0)





#fade between two sets, default to running forever
def runFadeStrip(startSet, endSet, n=-1):
  c=0
  while c<n or n<0:
    if(n>=0):
      c+=1
    done = False
    l.time.sleep(10)
    while(not done):
      done = l.fadeStrip(endSet,2)
      l.updateLights()
    l.time.sleep(3)
    done = False
    while(not done):
      done = l.fadeStrip(startSet,20)
      l.updateLights()
#  l.updateLights()
#  l.time.sleep(10)
#  l.clearLights()

#default to running forever
def runTower(lightNum=1, n=-1):
  c=0
  while c<n or n<0:
    if(n>=0):
      c+=1
    l.pixTower(lightNum)




if __name__=='__main__':
  main()

