
'''
process of testing:
transform data like we were intending with the b4rle
compare how many long rungers there are between the original and the new data
compare run lengths for multiple iterations

if a significant number of long runs can be generated, then 
'''

import sys
from runMetrics import runMetrics
from common import *
from math import ceil


#datain is a string of bytes, combo is the type of combination for base 4 (0=none,1=xor,2=>1,3=even/odd)
#this doesn't compress it (it should just add 1 bit (the seed), and any additional padding and meta data)
'''
process:
convert data to base 4
transform according to combo
find seed (first bit of transformed data)
find length of qits that are the same type (determined by combo) (where the first bit of each qit is the same)
append n-1 1's then a 0 for how many qits for a given group, then the second bit of the qits

eg:
01001001 01000100 00110011 00000011 = 32bits
1021 1010 0303 0003
using xor grouping:
10001110 10001000 00010001 00000001
2032 2020 0101 0001
could be:
1 (seed, all following lines have an asumed bit oscillating 1-0-1-0..)
00 (group type (xor))
0 0 (2)
0 0 (0)
110 100 (322)
0 0 (0)
0 0 (2)
111111110 001010001 (001010001)
11111 (1 pad to get a full byte)
=40 bits

'''
def apply(datain,combo=1,verbose=False):
  #convert to b4
  datain = "".join([int2base(e,4,0).zfill(4) for e in datain])
  if(verbose): print("datain:", datain)
  
  #convert to specified combo
  if(combo==0): #xor
    datain = datain.replace("1","4").replace("3","1").replace("2","3").replace("4","2") #1->2,3->3,3->1
  elif(combo==1): #>1, aka original data
    pass
  elif(combo==2): #even/odd
    datain = datain.replace("0","4").replace("1","0").replace("2","3").replace("3","1").replace("4","2") #0->2,1->0,2->3,3->1
  #else: no conversion
  
  if(verbose): print("transformed datain:",datain)
  
  seed = int(int(datain[0])>1)
  
  if(verbose): print("seed",seed,"combo",int2base(combo,2,2))
  
  dataout=str(seed)+int2base(combo,2,2) #init start of dataout with seed bit and combo type
  
  start=0 #bit where the group starts
  count=0 #how many in the group
  group=seed #toggling group
  while start+count<len(datain):
    count=0
    #while data matches group (and within data limit)
    while (start+count)<len(datain) and (int(int(datain[start+count])>1)==group):
      count+=1
    
    dataout += "1"*(count-1)+"0"+"".join([str(int(e)%2) for e in datain[start:start+count]]) #add index and values
    if(verbose): print(dataout)
    
    
    group=(group+1)%2 #toggle group
    start+=count #reset index
  
  dataout+= "1"*(ceil(len(dataout)/8)*8-len(dataout)) #append 1's to get a full byte (multiple of 8)
  if(verbose): print(dataout)
  
  return dataout



#find the minimum combo set given:
#datain=original data to transform
#iters=number of times to process the data
def findmin(datain,iters,verbose=False):
  
  '''
  process for testing different combos:
  
  specify how many iterations should be performed
  init the first data with the orig
  for the number of iters:
    for each combo:
      see which combo works best with the data
    set data as applied data from the best combo
  '''
  
  #get the original data
  data = datain
  
  for i in range(iters): #for each iteration
    mincombo=0 #init combo that has the best changes (fewest lengths of 1)
    minmetric=len(data)*4 #init to the length of the qits of the data
    for c in range(3): #test on each type of combo (0,1,and 2)
      testdata = bin2byte(apply(data,c))
      metric = runMetrics(testdata) #generate the metrics
      minmetric=min(minmetric,metric[list(metric)[0]]) #get the lowest metric
      #if the new metric is the minimum, then set the min combo
      #TODO: there's probably a more efficient way to get this result
      if(metric[list(metric)[0]]==minmetric):
        mincombo=c
      
      if(verbose): print(" ",c,metric[list(metric)[0]],minmetric,mincombo)
    
    if(verbose): print(mincombo)
    if(verbose): print(runMetrics(data,2))
    #set the data to the new combo
    data = apply(data,mincombo)
    if(verbose): print(data)
    data = bin2byte(data)


  return data
  



if(__name__=='__main__'):
  
  dataFile = sys.argv[1] if len(sys.argv)>=2 else None
  fileData = getDataFromFile(dataFile)
  dataSize = int(sys.argv[2]) if len(sys.argv)>=3 else len(fileData)
  
  origData = fileData[:dataSize]
  #get the metrics for the original data
  origRuns = runMetrics(origData)
  
  data = findmin(origData,1,True) #process the data to try and get longer runs
  newmetric=runMetrics(data)

  #display the original data runs vs the latest one
  print()
  for e in origRuns: print(e,origRuns[e])
  print()
  for e in newmetric: print(e,newmetric[e])
  
  
  print(byte2bin(origData))
  print(len(origData))
  print(byte2bin(data))
  print(len(data))
