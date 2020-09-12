import lightFxns as l

def main():
#  l.everyNthLight([l.col['w'],l.col['r'],l.col['g']],5)
  '''
    while(tuple(l.pixels[l.numLights-1]) != endColor): #loop until color is reached
      for i in range(l.numLights):
        l.fade2color(i,endColor,15)
      l.updateLights()
  '''
  c=0
  while c<3:
    c+=1
    l.pixTower(2)



  l.time.sleep(1)
  l.clearLights()

if __name__=='__main__':
  main()

