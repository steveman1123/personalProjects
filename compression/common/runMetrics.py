#see how often certain run lengths occur in bin data converted to basse 4 (qits)

#pass filename and size limit as arguments only if running as main
#else allow it to be imported and count the data based off that

from common import *
import sys

#fulldata is a string of bytes, combo is the type of combination for base 4 (1=xor,2=none/>1,3=even/odd)
#return dict of format {runLen:number of run}
def runMetrics(fullData,combo=1,verbose=False):
  #convert data to base 4
  b4 = "".join([int2base(int(e),4,4) for e in fullData])
  if(verbose): print(b4)
  
  if(combo==0): #xor
    group1=[0,3]
    group2=[1,2]
  elif(combo==1): #>1, aka original data
    group1=[0,1]
    group2=[2,3]
  elif(combo==2): #even/odd
    group1=[0,2]
    group2=[1,3]
  else:
    raise ValueError("Invalid combo")

  runs = {}

  start=0 #start of the run
  while start<len(b4):
    i=0 #length of the run
    if(int(b4[start+i]) in group1): #test group 1 runs
      while start+i<len(b4) and int(b4[start+i]) in group1:
        i+=1
    elif(int(b4[start+i]) in group2): #test group 2 runs
      while start+i<len(b4) and int(b4[start+i]) in group2:
        i+=1
    else: #invalid data (shouldn't be possible, but weirder things have happened)
      raise ValueError("invalid")
    
    if(verbose): print(i)
    
    if(i in runs): runs[i]+=1
    else: runs[i]=1
    
    start+=i
    
  runs = {e:runs[e] for e in sorted(runs)} #sort by value
  return runs



if(__name__=='__main__'):
  
  dataFile = sys.argv[1] if len(sys.argv)>=2 else None
  dataSize = int(sys.argv[2]) if len(sys.argv)>=3 else None
  fileData = getDataFromFile(dataFile)
  fullData = fileData[:min(dataSize,len(fileData))]
  
  print(f"File: {dataFile}")
  print(f"Size Limit: {dataSize}")
  print(f"Data size (bytes): {len(fullData)}")
  print()
  
  runs = runMetrics(fullData)
  
  for e in runs:
    print(e,runs[e])


