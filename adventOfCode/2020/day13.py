with open('day13in2.txt','r') as f:
  s=f.read().split('\n')

dTime = int(s[0]) #departure timestamp
buses = [int(e) for e in s[1].split(',') if e!='x'] #get the bus numbers (and ignore the 'x's)

minDtimes = {e-dTime%e:e for e in buses}

pt1 = minDtimes[min(minDtimes)]*min(minDtimes)

print(pt1)

count = max(buses) #find the bus that comes the least often (we're going to iterate by that to speed things up)
bus2 = [[i,int(e)] for i,e in enumerate(s[1].split(',')) if e != 'x'] #remove x's and get the numbers & indicies

'''
# startInit = 100000000000000 #100000000000000 comes from the main page where is says it must be greater than this number
startInit = 0
startTime=startInit+(count-startInit%count)
timeDiffs=1
while(timeDiffs>0):
  timeDiffs=0
  for i,e in enumerate(bus2):
    if(e != 'x'):
      timeDiffs += (startTime-bus2.index(str(count))+i)%int(e)
  print(f"{startTime} / {timeDiffs}")
  startTime+=count
pt2 = startTime-bus2.index(str(count))-count

print(pt2)
'''

#harmonics
print(bus2)
#how often does it take for two numbers to line up? So find how long it takes to line up
#


#find the minimum number that a and b will be d distance apart
def findDiff(a,b,d):
  












