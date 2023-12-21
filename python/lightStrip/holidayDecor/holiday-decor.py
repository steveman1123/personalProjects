import lightFxns as l
import datetime as dt
import threading, time


def main():
  while True:
    startTime = dt.time(17,30) #time of day to start (5:30pm)
    endTime = dt.time(23,0) #time of day to stop (11pm)
    
    
    #halloween colors
    runFadeStrip(
      l.everyNthLight([l.col['o'],l.col['v']],1),
      l.everyNthLight([l.col['r']],1),
      -1,
      startTime,endTime,
      dt.date(dt.date.today().year,10,1),
      dt.date(dt.date.today().year,11,1)
    )

    #generic fall colors
    runFadeStrip(
      l.everyNthLight([l.col['o'],l.col['p'],l.col['y'],l.col['r']],1),
      l.everyNthLight([l.col['o'],l.col['y']],1),
      -1,
      startTime,endTime,
      dt.date(dt.date.today().year,11,1),
      dt.date(dt.date.today().year,12,1)
    )

    #christmas colors
    runFadeStrip(
      l.everyNthLight([l.col['r'],l.col['g'],l.col['w']],5),
      l.everyNthLight([l.col['c'],l.col['b'],l.col['c'],l.col['w']],1),
      -1,
      startTime,endTime,
      dt.date(dt.date.today().year,12,1),
      dt.date(dt.date.today().year+1,1,1)
    )

    #generic winter colors
    runFadeStrip(
      l.everyNthLight([l.col['c'],l.col['b'],l.col['c'],l.col['w']],1),
      l.everyNthLight([l.col['w'],l.col['v'],l.col['c']],3),
      -1,
      startTime,endTime,
      dt.date(dt.date.today().year,1,1),
      dt.date(dt.date.today().year,2,1)
    )

    #valentine's colors
    runFadeStrip(
      l.everyNthLight([l.col['c'],l.col['b'],l.col['c'],l.col['w']],1),
      l.everyNthLight([l.col['w'],l.col['p'],l.col['r'],l.col['p']],3),
      -1,
      startTime,endTime,
      dt.date(dt.date.today().year,2,1),
      dt.date(dt.date.today().year,2,16)
    )


    #st pattys day
    runFadeStrip(
      l.everyNthLight([l.col['g'],l.col['g'],l.col['y'],l.col['g'],l.col['w']],1),
      l.everyNthLight([l.col['g'],l.col['w'],l.col['o']],3),
      -1,
      startTime,endTime,
      dt.date(dt.date.today().year,2,16),
      dt.date(dt.date.today().year,3,17)
    )

    #generic spring colors
    runFadeStrip(
      l.everyNthLight([l.col['p'],l.col['g'],l.col['c'],l.col['y'],l.col['v']],2),
      l.everyNthLight([l.col['w'],l.col['g'],l.col['g'],l.col['b'],l.col['g']],1),
      -1,
      startTime,endTime,
      dt.date(dt.date.today().year,3,17),
      dt.date(dt.date.today().year,4,20)
    )




    time.sleep(15)
    l.clearLights()


  #run the pix tower with 2 lights, 3 times
  #runTower(20,0)





#fade between two sets n times or between two day times, default to running forever
#where startSet=the list of tuple colors to display first
#endSet=the list of tuple colors to display second
#n=the number of times to flip between the two (-1 for infinite)
#startTime=time of day to start displaying
#endTime=time of day to end displaying
#startDate=day of year to start displaying
#endDate=day of year to stop displaying

def runFadeStrip(startSet, endSet, n=-1, startTime=dt.time(0), endTime=dt.time(0),startDate=dt.date(2000,1,1),endDate=dt.date(2000,1,1)):
  c=0
  while (c<n or n<0) and (dt.datetime.now().time()>=startTime or dt.datetime.now().time()<endTime) and (startDate<=dt.date.today()<endDate):
    #l.updateLights()
    if(n>=0): c+=1
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

