#do rle on base 4
import sys
from common import *
import time

'''
process:
convert bin data to base 4 (qits)
have 1 bit represent either 00 or 01
next 2 bits have the number of bits for the bit count (00 for 1 qit of data, 01 for 2-5qits, 10 for 6-9qits, 11 for 10-18qits)
next m bits determine how many to encode with this pattern (-1. 000=1)
next n bits are 0 or 1 for if it's the define bit as is or inverted

possibly have option that looks for perfect alternation (that is, every other row is 0 or 1 (this may not always happen since there could be a long string of 0's or 1's))

'''

#take data in as bytes
#fixed length indexing
def apply1(datain):
  '''
  eg (old) (use fixed length qit count instead of variable length):
  01001001 01000100 0011001100000011 = 32bits
  1021 1010 0303 0003
  could be:
  1 000 0
  0 000 0
  1 010 100
  0 000 0
  1 000 0
  0 111 00101000
  0 000 1
  =44bits
  '''
  #convert from byte to base 4
  datain = "".join([int2base(e,4,0).zfill(4) for e in datain])
  # print(datain)
  countBits = 3
  start = 0
  dataout = ""
  while start<len(datain):
    count=0
    #add the value type
    # print(int(datain[start]))
    if(int(datain[start]) in [0,3]):
      dataout+="0 "
    elif(int(datain[start]) in [1,2]):
      dataout+="1 "
    else:
      raise ValueError(f"invalid! {start}: {datain[start]}")
    
    #add the count value
    if(int(dataout[-2])): #1 or 2
      while start+count<len(datain) and int(datain[start+count]) in [1,2]:
        count+=1
    else: #0 or 3
      while start+count<len(datain) and int(datain[start+count]) in [0,3]:
        count+=1
      
    dataout+=int2base(count-1,2,3)+" "
    dataout+="".join([str(int(int(e)>1)) for e in datain[start:start+count]])+"\n"
    #add the data
    
    
    # print(dataout)
    start+=count
    # time.sleep(1)
  
  return dataout

#take data in as bytes
#variable length indexing (with max)
def apply2(datain):
  '''
  process:
  convert data to b4
  find length of qits that are the same type (all 1|2 or all 0|3)
  find length of bits for length of qits
  find type of qit for the length (0|3 or 1|2)
  append data as {type}{length of length}{length}{qit inversion}
  
  
  eg:
  01001001 01000100 0011001100000011 = 32bits
  1021 1010 0303 0003
  could be:
  1 00 0
  0 00 0
  1 01 01 100
  0 00 0
  1 00 0
  0 11 1000 001010001
  =40bits
  '''
  #convert to b4
  datain = "".join([int2base(e,4,0).zfill(4) for e in datain])
  # print(datain)
  dataout=""
  
  start=0
  while start<len(datain):
  
    #find length of qits of same type
    count=0
    if(int(datain[start]) in [0,3]):
      while start+count<len(datain) and int(datain[start+count])in [0,3] and count<18:
        count+=1
    elif(int(datain[start]) in [1,2]):
      while start+count<len(datain) and int(datain[start+count])in [1,2] and count<18:
        count+=1
    else:
      raise ValueError("invalid")
    datalen=count
    
    if(count>=18):
      print(count)
      time.sleep(3)
    
    #find the length of bits for the length of qits (datalen)
    lenlen = len(int2base(datalen-2,2)) if datalen>1 else 0
  
    #find qit type (0 for 00|11, 1 for 01|10)
    datatype = int(int(datain[start]) in [1,2])
    
    
    #append data
    dataset = f"{datatype} {int2base(lenlen,2,2)} {int2base(datalen-1,2) if datalen>1 else ''} "+"".join([str(int(int(e)>1)) for e in datain[start:start+count]])+"\n"
    
    dataout += dataset
    
    start+=count
  
  return dataout

#variable lens
#start with a seed (either 0 or 1 depending what the first data is)
#in each section:
#if section=0: 
def apply3(datain):
  '''
  process:
  
  
  
  ex:
  1021 1010 0303 0003
  01001001 01000100 00110011 00000011
  
  
  '''
  
  
  return dataout

if(len(sys.argv)!=2):
  raise ValueError("please pass a numeric number of bytes as an argument")
else:
  rndBytes = int(sys.argv[1])
# fullData = getRandData(rndBytes,fromFile=True)
fullData = getDataFromFile("./nggyu.mp3")[:rndBytes]
print(fullData)
# c = oneeqtn(fullData,window)
c = apply2(fullData)

# print(*c,sep="\n")
print(c)

newlen = len(c.replace(" ","").replace("\n",""))
print(len(fullData)*8,newlen,round(newlen/(len(fullData)*8),2))