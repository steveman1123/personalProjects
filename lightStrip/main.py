import lightFxns as l
import datetime as dt
import threading

while True:
  startTime = dt.time(19,00) #time of day to start (7pm)
  endTime = dt.time(6,00) #time of day to stop (6am)
  l.clearLights()
  runFadeStrip(
    l.everyNthLight([l.col['o'],l.col['p']],1),
    l.everyNthLight([l.col['r']],1),
    -1,
    startTime,
    endTime
    )

#run the pix tower with 2 lights, 3 times
#runTower(20,0)





#fade between two sets, default to running forever
def runFadeStrip(startSet, endSet, n=-1, startTime=dt.time(0), endTime=dt.time(0)):
  c=0
  while (c<n or n<0) and (dt.datetime.now().time()<=startTime or dt.datetime.now().time()>endTime):
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

