'''
purpose:
preprocess data into the following format:
b (seed)
bb (combo type)
11...10 b...b (number of qits (formatted as all 1's, then a 0), then the second digit of the qits (first digit is implied by the seed. Should oscillate 1-0-1-0... or 0-1-0-1... based on the seed))
...
1...1 (append 1's at the end to round to the next highest byte (for proper storage)

the process can be iterated so that the output of the previous processing can become the input for the next processing
'''

'''
basic process:
get original data as byte string
iterate the following as desired:
  convert (from base 16) into base 4
  transform based on the combo type (23 types: permutations minus original data format)
  determine seed from transformed data
  determine run lengths
  generate output as byte string

'''

'''
advanced process:

specify file (optionally specify number of bytes (for testing))
read data into a byte string

find the best reduction of entropy (runs of 1) for the number of desired iterations

find that reduction by doing:
  for each iteration:
    for each combo:
      process the data using the combo
      determine if the latest combo is better than the last
    
    set the input of the next iteration as the output of the best combo
  return the data from the last iteration (as byte string)


process the combo by doing:
  convert to base 4
  transform according to the combo
  get seed from first bit of transformed data
  init output with seed and combo
  
  init run start (0 - bit in the data that the runs will start at)
  init run length (0 - length of each run)
  init group (seed - oscillator to switch between 0-1-0-1 or 1-0-1-0 based on the seed)
  
  while within the data set:
    ensure run length is 0
    while still within data set and data still matches group:
      add to the run length
    append index and data to the output
    toggle the group
    set the start of the next group to the end of the last group
  append 1's to the end of the output to have properly defined output to the byte level (fill 1's to the next multiple of 8)
  return the output (as a byte string)
'''

from common import *
import sys, time

#TODO: test each function for proper functionality


#transform data according to the combo type (permutation number)
#data is base 4 string (0123)
#eg: data=1023 1011 2330, combo=7, output=2103 2122 0331
#TODO: can this be done more efficiently?
def b4xfrm(data,combo,verbose=False):
  if(verbose): print("b4xfrm","combo",combo,"din",data)
  if(combo==0): #0132
    data = data.replace("2","4").replace("3","2").replace("4","3")
  elif(combo==1): #0213
    data = data.replace("1","4").replace("2","1").replace("4","2")
  elif(combo==2): #0231
    data = data.replace("1","4").replace("3","1").replace("2","3").replace("4","2")
  elif(combo==3): #0312
    data = data.replace("1","4").replace("2","1").replace("3","2").replace("4","3")
  elif(combo==4): #0321
    data = data.replace("1","4").replace("3","1").replace("4","3")
  elif(combo==5): #1023
    data = data.replace("0","4").replace("1","0").replace("4","1")
  elif(combo==6): #1032
    data = data.replace("0","4").replace("1","0").replace("4","1").replace("2","4").replace("3","2").replace("4","3") #TODO: can this be done more efficiently?
  elif(combo==7): #1203
    data = data.replace("0","4").replace("2","0").replace("1","2").replace("4","1")
  elif(combo==8): #1230
    data = data.replace("0","4").replace("3","0").replace("2","3").replace("1","2").replace("4","1")
  elif(combo==9): #1302
    data = data.replace("0","4").replace("2","0").replace("3","2").replace("1","3").replace("4","1")
  elif(combo==10): #1320
    data = data.replace("0","4").replace("3","0").replace("1","3").replace("4","1")
  elif(combo==11): #2013
    data = data.replace("0","4").replace("1","0").replace("2","1").replace("4","2")
  elif(combo==12): #2031
    data = data.replace("0","4").replace("1","0").replace("3","1").replace("2","3").replace("4","2")
  elif(combo==13): #2103
    data = data.replace("0","4").replace("2","0").replace("4","2")
  elif(combo==14): #2130
    data = data.replace("0","4").replace("3","0").replace("2","3").replace("4","2")
  elif(combo==15): #2301
    data = data.replace("0","4").replace("2","0").replace("4","2").replace("1","4").replace("3","1").replace("4","3")
  elif(combo==16): #2310
    data = data.replace("0","4").replace("3","0").replace("1","3").replace("2","1").replace("4","2")
  elif(combo==17): #3012
    data = data.replace("0","4").replace("1","0").replace("2","1").replace("3","2").replace("4","3")
  elif(combo==18): #3021
    data = data.replace("0","4").replace("1","0").replace("3","1").replace("4","3")
  elif(combo==19): #3102
    data = data.replace("0","4").replace("2","0").replace("3","2").replace("4","3")
  elif(combo==20): #3120
    data = data.replace("0","4").replace("3","0").replace("4","3")
  elif(combo==21): #3201
    data = data.replace("0","4").replace("2","0").replace("1","2").replace("3","1").replace("4","3")
  elif(combo==22): #3210
    data = data.replace("0","4").replace("3","0").replace("4","3").replace("1","4").replace("2","1").replace("4","2")
  else:
    pass
  if(verbose): print("b4xfrm","combo",combo,"dout",data)
  return data


#TODO: do we want to just store the number of iterations at the end instead of doing it every loop?
#process the combo (transform into the new format outlined in the purpose comment) - combo has a max of 23 (but can go up to 32)
#datain and dataout are byte strings, combo is an int 0-31
#eg:
#input: b'ID3\x03', 5
# = 01001001 01000100 00110011 00000011 (base2)
# = 01001001 01000100 00110011 00000011
# = 1021 1010 0303 0003 (base4)
#convert to combo 5:
# = 0120 0101 1313 1113
# = 00 01 10 00 00 01 00 01 01 11 01 11 01 01 01 11
#expected output:
#0 00 00101 1001 00 111110001011 01 01 01 110111 01
#| |  |     |    |  |            |  |  |  |      |  +-1 pad ending
#| |  |     |    |  |            |  |  |  |      +----3
#| |  |     |    |  |            |  |  |  +-----------111
#| |  |     |    |  |            |  |  +--------------3
#| |  |     |    |  |            |  +-----------------1
#| |  |     |    |  |            +--------------------3
#| |  |     |    |  +---------------------------------001011
#| |  |     |    +------------------------------------2
#| |  |     +-----------------------------------------01
#| |  +-----------------------------------------------combo
#} +--------------------------------------------------iteration
#+----------------------------------------------------seed
# = b'\x05\x93\xe2\xd5\xdd'
def processCombo(data,combo,iteration,verbose=False):
  #enure combo is in the proper range
  combo = max(0,min(combo,31))
  if(iteration>3): raise ValueError("too many iterations")
  
  #convert data to base 4 (qits)
  data = "".join([int2base(e,4,4) for e in data])
  #transform data according to the combo (change qits as the combo says)
  if(verbose): print("processCombo","b4data",data)

  data = b4xfrm(data,combo)
  
  if(verbose): print("processCombo","xfrm data",data)
  
  #get the seed from the first bit of the transformed data
  seed = int(int(data[0])>1) #as a single bit
  
  #init output with seed and combo (as a binary string)
  b2out = str(seed)+int2base(iteration,2,2)+int2base(combo,2,5) #ensure iterationonly has 2 bits and combo has only 5 bits (up to 31)
  
  if(verbose): print("processCombo","seed, iter, & combo ",b2out)
  
  #init run start to the start of the data (0th bit)
  runStart = 0
  #init run length (no run made yet)
  runLen = 0
  #init group (oscillate, starting with the seed)
  group = seed
  
  #while end (start+run len) is within the data set:
  while runStart+runLen<len(data):
    #while end still within data set and still matching the group:
    while runStart+runLen<len(data) and (int(int(data[runStart+runLen])>1)==group):
      #add to the run len
      runLen+=1
    
    #append index to the output ((run len)-1 1's, then 1 0)
    idx = "1"*(runLen-1)+"0"
    b2out += idx
    
    #append data (2nd bit of the transformed qit)
    databits = "".join([str(int(e)%2) for e in data[runStart:runStart+runLen]])
    b2out += databits
    
    if(verbose): print("processCombo","group",group,"b2out",b2out)
    
    #toggle group (so it oscillates between 0 and 1)
    group = (group+1)%2
    
    #set the run start to end of the last group
    runStart += runLen
    
    #ensure run length is 0 (reiniting for the start of the new run)
    runLen=0
  
  #round the bits up to a multiple of 8 to have valid bytes. append 1's to the end
  b2out+= "1"*(ceil(len(b2out)/8)*8-len(b2out))
  
  if(verbose): print("processCombo","b2out (bin)  ",b2out)
  
  #convert from binary string to byte string
  dataout = bin2byte(b2out)
  if(verbose): print("processCombo","dataout(bytes)",dataout)
  
  return dataout



#iterate finding the best reduction of runs of length 1 of various combos
#where data is a byte string, and iters is an int
#input: b'ID3\x03', 2
#expected output:
#combo 17 - b'DtO\xf6\xbb'
#combo 0 - b'\x03\xd5:\xb8\x1fk'
def findMin(data,iters,verbose=False):
  if(iters>4): raise ValueError("too many iters")
  #for each iteration:
  for i in range(iters):
    #set/reset the min runs of 1 and the min combo
    minrunsof1=len(data)*4 #set to max value to be minimized later
    mincombo=0 #init to some value 0-31
    if(verbose): print("findMin","i",i)
    
    #for each combo:
    for c in range(24): #every available combo
      if(verbose): print("findMin","c",c)
      #process the data
      processedData = processCombo(data,c,i)
      #determine if the latest combo is the best combo by...
      #get the number of runs (convert it to base 4 and see if it's >1 or not)
      runs = getRuns(processedData)
      if(verbose): print("findMin","runs",runs)
      runsof1 = runs[list(runs)[0]]
      #determine the minimum runs so far
      #TODO: add another check for the second shortest if the first shortest is already present(eg in the example, in the first iteration 8 and 16 are both the shortest for 1. 17 is chosen bc it's evaluated after 8, but it should be chosen because the second shortest (4:1) is greater than 8's second shortest (2:2) and the number of the second shortest is lower than 8's)
      minrunsof1 = min(minrunsof1,runsof1)
      #compare to previous run counts, if the latest is the minimum:
      if(runsof1==minrunsof1):
        #set the new min count and the new min combo
        mincombo=c
        if(verbose): print("findMin","mincombo updated")
      
    #set the input of the next iteration as the output of the best combo
    if(verbose): print("findMin","i",i,"mincombo",mincombo,"data",data)
    data=processCombo(data,mincombo,i)
    if(verbose): print("findMin","processedData",data)
    
  #return the data from the last iteration (as a byte string)
  return data



#procure the original data from processed data
#data in and data out sohuld be byte strings
def getOrig(data):
  return origData


if(__name__=='__main__'):
  #specify the file using arguments (optionally specify number of bytes (for testing))
  dataFile = sys.argv[1] if len(sys.argv)>=2 else None
  fileData = getDataFromFile(dataFile)
  dataSize = int(sys.argv[2]) if len(sys.argv)>=3 else len(fileData)
  
  #get the original data
  origdata = fileData[:dataSize]
  
  #find the best reduction of runs based on some number of iterations
  iters = 2
  starttime=time.time()
  mindata = findMin(origdata,iters)
  exectime = time.time()-starttime
  #display the results
  #print(origdata)
  print(len(origdata))
  #print(mindata)
  print(len(mindata))
  
  print("exec time (s):",exectime)
  
  print()
  origruns = getRuns(origdata)
  minruns = getRuns(mindata)
  print("original runs")
  for e in origruns: print(e,origruns[e])
  print("min runs")
  for e in minruns: print(e,minruns[e])
