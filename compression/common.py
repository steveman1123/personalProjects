#common functions between the different compression things

import string, os, random
from math import *

#get the random data
#TODO: incorporate the data file, add as parameter so that it's easy to switch between the file or 
def getRandData(rndByteNum=0,fromFile=False,byteSize=8):
  while rndByteNum<=0:
    rndByteNum = int(input("# of random bytes: "))
  
  if(fromFile):
    # rndByteList = [ord(c) for c in getDataFromFile()[:rndByteNum]]
    print(rndByteNum)
    rndByteList = getDataFromFile()[:rndByteNum]
  else:
    rndByteList = [random.randint(0,2**byteSize) for _ in range(rndByteNum)]
  
  
  return rndByteList



#get data from a file
def getDataFromFile(dataFile="./rndFile.dat"):
  if(dataFile is None): dataFile="./rndFile.dat"
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
    rndstr = open(dataFile,'rb').read()

  return rndstr


#convert between different bases with option to lead with specified number of 0's

def int2base(x, base,leadZeros=0):
  digs = string.digits + string.ascii_letters
  if x < 0:
    sign = -1
  elif x == 0:
    return digs[0].zfill(leadZeros)
  else:
    sign = 1

  x *= sign
  digits = []

  while x:
    digits.append(digs[x % base])
    x = x // base

  if sign < 0:
    digits.append('-')

  digits.reverse()

  return ''.join(digits).zfill(leadZeros)

#cosine function to use in quad
def cosfxn(t, M, datachunk):
  return datachunk[int(t)]*cos(M*t)

#sine function to use in quad
def sinfxn(t, N, datachunk):
  return datachunk[int(t)]*sin(N*t)

#calculate the appx function from the recorded terms
#x(t) = a0+sum(am*cos(M*t),m,-inf,inf)+sum(bn*sin(N*t),n,-inf,inf)
#where ftterms are the fourier transform coefficients as a list of 2 elements lists [a0,[a1,b1],[a2,b2],...,[am,bn]]
def calcFxn(ftterms,ts,m,n,T):
  y=[0]*len(ts) #initialize the y values  
  for i,t in enumerate(ts):
    cpt = sum([e[0]*cos(2*pi*(m1+1)/T*t) for m1,e in enumerate(ftterms[1:])]) #cos part
    spt = sum([e[1]*sin(2*pi*(n1+1)/T*t) for n1,e in enumerate(ftterms[1:])]) #sin part
    y[i] = ftterms[0]+cpt+spt
  return y





# round a decimal fraction (btw 0 and 1) to a given number of bits
# return rounded decimal (eg 0.3 @2 bits=01=0.25)
def roundbits(decfrac,resolution=8):
  isNeg = decfrac<0
  decfrac=abs(decfrac)
  if(decfrac>1 or decfrac<0): raise ValueError("out of bounds")
  calced=0 #actual binary value
  i=1 #digit place
  while i<resolution and calced!=decfrac:
    calced+=int(decfrac>=calced+2**-i)*2**-i
    i+=1
  return -calced if isNeg else calced


#convert a string of 1's and 0's to an actual byte character
def bin2byte(binstr):
  bytestr = int(binstr,2).to_bytes(ceil(len(binstr)/8),"big")
  return bytestr

#convert a bytes string to a string of 1's and 0'1
def byte2bin(bytestr):
  binstr=""
  for b in bytestr:
    binstr+=int2base(b,2,8)
  return binstr



#data in is a byte string
#data out is a dict of format {runlen:number of those runs}
#convert data in into base4, calculate bit runs (eg 01001110 would return {1:3,2:1,3:1})
def getRuns(data):
  b4data = "".join([int2base(e,4,4) for e in data])
  runs={}
  ones = "".join([str(int(int(e)>1)) for e in b4data])
  zeros = ones
  
  ones = ones.split("0")
  zeros = zeros.split("1")
  
  for e in ones+zeros:
    if(len(e)>0):
      if(len(e) in runs):
        runs[len(e)]+=1
      else:
        runs[len(e)]=1
  
  #sort the dict
  runs = {e:runs[e] for e in sorted(runs)}
  return runs
