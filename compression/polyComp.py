#the purpose of this scirpt is to try and create my own high density compression algorithm
#as of 2021-10-10, it doesn't work

import random, string, os, json
from math import *
from common import *

##begin data compression


#pts should be 2d array of format [[x1,y1],[x2,y2]]
#get the largest coefficient (eg "a" in ax^2+bx+c or "a" in ax^3+cx+d)
#eqtn format is (a-b)/(c-d)
#where a and b recurse down to singular y values, and c and d are x values
#pts = list of points [[x1,y1],[x2,y2]]
#n = point index. Should init with len of  pts
#pow = power. Should init with len(pts)-1
def getBigNum(pts, n, pow):
  if (n>0):
    if (pow<=0):
      return pts[0][1]
    elif (pow==1):
      return (pts[n-1][1] - pts[0][1])/(pts[n-1][0] - pts[0][0])
    else:
      return (getBigNum(pts, n, pow-1)-getBigNum(pts, n-1, pow-1))/(pts[n-1][0] - pts[n-pow][0])
  else:
    return 0


#calculates all possible ways of obtaining pow power with n number, a initiates as 0
#eg 3, 1, 0 returns x1+x2+x3 -- 2, 3, 0 returns x1(x1(x1+x2)+x2(x2))+x2(x2(x2))
#pts = list of points [[x1,y1],[x2,y2]]
#n=number of points
#pow=power to look at
#a=counter?
def mult(pts, n, pow, a=0):
  out = 0
  if(pow<1):
    out = 0
  elif(pow==1): #sums x vals from a thru n-1 inclusively
    if (a<=n-1):
      for i in range(a,n):
        out += pts[i][0]
  else:
    for b in range(a,n):
      out += pts[b][0]*mult(pts, n, pow-1, b)
  return out


#generate the coefficients of the polynomial given a set of points
#pts = list of points [[x1,y1],[x2,y2]]
#TODO: figure out how to return fractional components rather than decimal since decimals can be lossy with computers
def geteqtn(pts):
  n = len(pts)
  pow = n-1
  eqtn = [None for e in range(n)]
  
  for a in range(pow+1):
    sum=0
    for b in range(a,0,-1):
      sum += eqtn[a-b]*mult(pts, n-a, b)
    eqtn[a] = getBigNum(pts, n-a, pow-a) - sum
  
  return eqtn






'''
x=i=0
pts = []
while True:
  i+=1
  x = float(input(f"x{i}: "))
  if(x in [e[0] for e in pts]): break
  y = float(input(f"y{i}: "))
  pts.append([x,y])
  c = geteqtn(pts)
  print(c)
'''


#generate list of random data
#comression rates will be proptional to how often the data changes (per digit)
'''
so how an we find data that changes the least?
in what base? 2 may be too low, 16 may be too high though it might work for the upper half of the bytes.
8 or 10 or 12 could work. 

Also what direction? are there fewer changes reading along then entire byte array, or reading across xN matrix:
byte #  01234567...
0th bit>01011010
        01001001
        00101101
        11010010
        01011000
        11010110
        10110010
        01111100
nth bit -------^

digits needed = roundup(log(2^(byte size))/log(base))
2   11111111- 8eqtns <- doing this would be bad because they would change quite frequently
3   122222  - 11 
4   3333    - 12 <- or what if instead of looking across all, we'd only have to do 3eqtns? How often would they change?
5   2444    - 14
6   1555    - 16
7   566     - 17
8   377     - 17
9   388     - 19
10  299     - 20
11  2AA     - 22
12  1BB     - 23
13  1CC     - 25
14  1DD     - 27
15  1EE     - 29
16  FF      - 30 <- or what if instead of looking across all we'd have to do is 15eqtns?
'''

#compare input vs output sizes

'''
#get the random data
byteSize = 8
rndByteNum = int(input("# of random bytes: "))
rndByteList = [random.randint(0,2**byteSize) for _ in range(rndByteNum)]

#convert bytes to the new base
base = 2
cBytes = [int2base(e,base) for e in rndByteList]


#isolates the individual digits per byte
digits = [b.zfill(ceil(log(2**byteSize)/log(base))) for b in cBytes]

#change from list of strings to list of lists where each list contains the nth digit
digits = [[int(i[d]) for i in digits] for d in range(len(digits[0]))]


print(digits)

#TODO: what does this section do again?
xints = {}
for i,d in enumerate(digits):
  xints[i] = {}
  for e in list(set(d)): #for every unique value
    if(e>0): #no need to count 0's, since everything that's not 0 for the others after summation is 0 (process of elimination)
      isVal = [digit==e for digit in d] #determine whether the value is the one we want or not
      
      if(not isVal[0]):
        e = -e #if the first value is false (that is, the digit doesn't start until later), then set to negative
      xints[i][e] = [] #get the x-intercepts - when a value becomes
      for val in range(len(isVal)-1): #loop thru the T/F values
        if(isVal[val]!=isVal[val+1]): #see when a change occurs
          xints[i][e].append(val+.5) #append the change time as an x intercept

#print(json.dumps(xints,indent=2))

for d in xints:
  for y in xints[d]:
    pts = [[0,y]]
    for x in xints[d][y]:
      pts.append([x,0])
    eqtn = geteqtn(pts)
    eqtn = [round(e,3) for e in eqtn]
    print(d,y,eqtn)
'''



'''
compression process:
get data
apply window
record positions of every switch
y-int=prod(positions)
x-ints=positions
get eqtn
trim off first and last numbers (since they will always be 1 and prod(positions)
record numbers


decompression process:
append 1 and prod of positions to eqtn
if etqn>0, then 1, else 0
'''

#get the random data
#TODO: incorporate the data file, add as parameter so that it's easy to switch between the file or 
def getRandData(byteSize=8):
  rndByteNum = int(input("# of random bytes: "))
  rndByteList = [random.randint(0,2**byteSize) for _ in range(rndByteNum)]
  return rndByteList


byteSize = 8
rndByteList = getRandData(byteSize)
#convert to binary string (padded with the byte size)
base = 2
cBytes = "".join(map(str,[int2base(e,base,byteSize) for e in rndByteList]))

#amount of data in bits to look at per loop
windowSize = 12

print(cBytes)
eqtns = []
i=0
while i<len(cBytes):
  #get the data inside of the window
  windowData = cBytes[i:i+windowSize]
  print(windowData)
  
  #get the switch locations (where 1->0 or 0->1)
  switches = [i+1 for i in range(len(windowData)-1) if windowData[i]!=windowData[i+1]]
  #set the y-intercept to be the product of the switch locations
  yint = prod(switches)
  if(windowData[0]==0): yint = -yint
  pts = [[0,yint]]+[[e,0] for e in switches]
  
  print(pts)
  eq = geteqtn(pts)
  print(eq)
  print(eq[1:-1])
  print()
  eqtns.append(eq[1:-1]+[switches[0]])
  i+=windowSize

print(eqtns)