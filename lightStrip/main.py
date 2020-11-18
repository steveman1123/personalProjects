import lightFxns as l
import datetime as dt
import threading, time


def main():
  while True:
    startTime = dt.time(19,00) #time of day to start (7pm)
    endTime = dt.time(6,00) #time of day to stop (6am)
    
    runFadeStrip(
      #halloween colors
      #l.everyNthLight([l.col['o'],l.col['v']],1),
      #l.everyNthLight([l.col['r']],1),
      #generic fall colors
      l.everyNthLight([l.col['o'],l.col['p'],l.col['y'],l.col['r']],1),
      l.everyNthLight([l.col['o'],l.col['y']],1),
      #christmas colors
      # l.everyNthLight([l.col['r'],l.col['g'],l.col['w']],5),
      # l.everyNthLight([l.col['c'],l.col['b'],l.col['c'],l.col['w']],1),
      
      
      -1,
      startTime,
      endTime
    )
    print(str(dt.datetime.now().time()))
    print(str(dt.datetime.now().time()>=startTime)+" - "+str(dt.datetime.now().time()<endTime))
    time.sleep(15)
    l.clearLights()


  #run the pix tower with 2 lights, 3 times
  #runTower(20,0)





#fade between two setsn times or between two day times, default to running forever
def runFadeStrip(startSet, endSet, n=-1, startTime=dt.time(0), endTime=dt.time(0)):
  c=0
  while (c<n or n<0) and (dt.datetime.now().time()>=startTime or dt.datetime.now().time()<endTime):
    #l.updateLights()
    if(n>=0):
      c+=1
    done = False
    while(not done):
      done = l.fadeStrip(endSet,2)
      l.updateLights()
    time.sleep(20)

    done = False
    while(not done):
      done = l.fadeStrip(startSet,2)
      l.updateLights()
    time.sleep(20)

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

if __name__ == '__main__':
  main()

