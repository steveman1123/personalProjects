

import random, string, os
'''
dataFile = "./rndFile.dat"

if(not os.path.isfile(dataFile)):
  #generate a long random string
  chars = [chr(i) for i in range(128)]
  strlen = 5000000

  print(f"generating string of len {strlen}")
  rndstr = ''.join([random.choice(chars) for i in range(strlen)])
  print("writing to file")
  open(dataFile,'w').write(rndstr)
  print("done writing to file")

else:
  rndstr = open(dataFile,'r').read()
'''

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
  print()
  x = float(input(f"x{i}: "))
  if(x in [e[0] for e in pts]):
    break
  y = float(input(f"y{i}: "))
  pts.append([x,y])
  
  c = geteqtn(pts)
  print(c)
'''


#generate list of random data
#combine some data (like every 3 elements. eg [a,b,c,d,e,f,g,h,...] => {a,bcd,e,fgh,...} note that that will not work as a good method for a real compressor since 'a' and 'e' could be identical (unless more elements were combined to make them, but then would be fighting entropy/stats rather than being properly unique)
#produce equation based on the values
#compare sizes

rndByteNum = int(input("# of random bytes: "))
maxeqtn = int(input("max number of coefficients: "))

#get the random data
rndByteList = [random.randint(0,256) for _ in range(rndByteNum)]

#convert it into points (combine every other one into 1 number (eg 1,2,3,4 => 12,34
#pts = [[i,int(str(rndByteList[i]).zfill(3)+str(rndByteList[i+1]).zfill(3))] for i in range(0,len(rndByteList),2)]

#combine 1,2,3,4,5,6 to be x1=123,y1=456
#pts = [[int(str(rndByteList[i]).zfill(3)+str(rndByteList[i+1]).zfill(3)+str(rndByteList[i+2]).zfill(3)+str(rndByteList[i+3]).zfill(3)),int(str(rndByteList[i+4]).zfill(3)+str(rndByteList[i+5]).zfill(3)+str(rndByteList[i+6]).zfill(3)+str(rndByteList[i+7]).zfill(3))] for i in range(0,len(rndByteList),8)]

#pts format should be x=10^(number of digits of combined points-1), y=combined points
ypts = [int(str(rndByteList[i]).zfill(3)+str(rndByteList[i+1]).zfill(3)+str(rndByteList[i+2]).zfill(3)+str(rndByteList[i+3]).zfill(3)) for i in range(0,len(rndByteList),4)]
xpts = [10^(len(str(i))-1) for i in ypts]
pts = [[xpts[i],ypts[i]] for i in range(len(xpts))]


print(rndByteList)


'''
pts = []
if(len(rndByteList)%2==0): #if the data is even length
  for i in range(0,len(rndByteList)-1,2):
    pts.append([rndByteList[i],rndByteList[i+1]])
else:
  for i in range(0,len(rndByteList)-2,2):
    pts.append([rndByteList[i],rndByteList[i+1]])
'''

print(pts)

eq = geteqtn(pts)

print(eq)