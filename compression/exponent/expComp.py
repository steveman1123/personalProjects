'''
could have 2 exponentials: a coarse grain and a fine grain
must be added (no negatives)
value must be greater than bit val (eg if 8 bits are used, then value must be greater than 255)
could have a bit or two (or 3) that determines what values should be used (eg 0 for a&b, 1 for c&d, 2 for e&f, 3 for g&h)
^ instead of that, could also have the numbers be derived from data to be compressed

could do 1,5,4,3,3 (max compression of 75 bits to 16 bits)
1=is compressed (1 for reading the new data type, 0 for reading the data directly)
5=base 1 (a) - range 0-31
4=power 1 (b) - range 1-16
3=base 2 (c) - range 0-7
3=power 2 (d) - range 1-8
in a**b+b**c


adtnl bits per group:
sign bit 1
leading 0s 4?

'''

from math import log, ceil
from common import *
import sys



#attempt to calcuate the compression value
#if it doesn't work, shave off the last value, and try again
#do that until 15 bits are left, if it reaches 15, then change first bit to 0 and just use the original data

#take data in as a binary string
def apply(datain,verbose=False):
  #TODO: account for leading zeros
  #min and max base and power values (inclusive), and number of bits for them
  minb1 = 0
  maxb1 = 31
  bitb1 = ceil(log(maxb1-minb1,2))
  minp1 = 1
  maxp1 = 16
  bitp1 = ceil(log(maxp1-minp1,2))
  minb2 = 0
  maxb2 = 7
  bitb2 = ceil(log(maxb2-minb2,2))
  minp2 = 1
  maxp2 = 8
  bitp2 = ceil(log(maxp2-minp2,2))
  
  bits = len(datain)+1 #init to +1 because the length will immediately decriment by 1
  minBits = bitb1+bitp1+bitb2+bitp2 #minimum number of bits before reverting to no compression
  if(verbose):
    print("minb1",minb1,"maxb1",maxb1,"bitb1",bitb1)
    print("minp1",minp1,"maxp1",maxp1,"bitp1",bitp1)
    print("minb2",minb2,"maxb2",maxb2,"bitb2",bitb2)
    print("minp2",minp2,"maxp2",maxp2,"bitp2",bitp2)
    print("bits",bits-1,"minBits",minBits)
    
  found=False
  #try and find the data by looping through (this is a brute force way, there's definitely faster ways to check)
  while not found and bits>minBits:
    bits-=1 #decriment before continuing (this happens first because if found is triggered, then it will pass instead of continuing)
    a=minb1-1 #init with -1 because it will incriment first (since the found check is in the loop (and we don't want it to incriment after it's found)
    while not found and a<=maxb1:
      a+=1

      b=minp1-1
      while not found and b<=maxp1:
        b+=1
        
        c=minb2-1
        while not found and c<=maxb2:
          c+=1
          
          d=minp2
          while not found and d<=maxp2:
            d+=1
            if(a**b+c**d==int(datain[:bits],2)):
              found=True
              if(verbose): print("found!",a,b,c,d,bits)
              break
    
  #determine if the data is compressed or not
  isComp = int(bits>minBits)
  
  if(isComp): #if it is compressed, encode the data
    if(verbose): print("data has been compressed")
    dataout = str(isComp)+" "+\
              int2base(a-minb1,2,bitb1)+" "+\
              int2base(b-minp1,2,bitp1)+" "+\
              int2base(c-minb2,2,bitb2)+" "+\
              int2base(d-minp2,2,bitp2)
  else: #data is not compressed, don't encode it
    if(verbose): print("data has not been compressed")
    dataout = str(isComp)+datain[:bits]
    
    
  
  return dataout,bits #return the compressed data and the number of bits that have been compressed





#this data should compress to 1 11111 1110 111 110
#data = "100111110000000110111101101010000010100101111100001100111100110111011010110"

#this data should compress to 1 10010 1001 101 001
#data = "110011111101010000011011100100010000011001"

data = int(sys.argv[1])
data = int2base(data,2)

cdata,bits = apply(data,True)

print(cdata,bits)

#TODO: ensure leading zeros are accounted for (should be able to be compressed, or at least included with the data I think)
#TODO: make it go faster?
