#sinecomp but for base 4


from common import *
import sys
from scipy.integrate import quad
from matplotlib import pyplot as plt

#could try 1eqtn with 3 levels (1,2,3), or 2eqtns with being 0 or 1 and 2 or 3

#treat the data as a single equation with 4 levels (0, 1, 2, or 3)
#advantages: single equation
#disadvantages: requires high resolution
def oneeqtn(fullData,window,plotData=True,resolution=10,verbose=False):
  ftdata = [] #data generated by the fourier transform
  ftterms = [] #terms generated by the fourier transform, should be formatted as list of lists of terms
  winStart=winEnd=0 #starting point for where the window should be placed
  
  #while there's still data to process
  while winEnd<len(fullData):
    ftterms.append([]) #append the next set of data
    winStart = winEnd #set the starting bit to the last ending bit (since data is captured from start (inclusive) to end (exclusive))
    winEnd = winStart+min(len(fullData)-winStart,window) #set the end to either the window length or the remaining data points
    datachunk = [int(e) for e in fullData[winStart:winEnd]] #get the data from the start to end points
    
    m=n=0 #m and n constants in the fourier transform
    T = len(datachunk) #T constant in the fourier transform
    a0 = 1/T*sum(datachunk)
    # a0 = round(1/T*sum(datachunk),roundconst) #because data is square waves of height=1, then the integral over a period is simply the sums of the 1's
    ftterms[-1] += [a0] # set the first element of the latest list of constants to the dc offset
    
    #keep adding terms until the approximation becomes good enough
    while ftdata!=datachunk: #do until data is valid
      n+=1 #summation starts at 1 and can go up to infinity
      m+=1
      am = 2/T*quad(cosfxn,0,T,args=(2*pi*m/T,datachunk))[0]
      bn = 2/T*quad(sinfxn,0,T,args=(2*pi*n/T,datachunk))[0]
      #have a cutoff that if the abs(am|bn)<cutoff: am|bn=0, reduce data
      # print(am,bn,end="\t")
      constCutoff = 0.04
      if(abs(am)<=constCutoff): am=0
      if(abs(bn)<=constCutoff): bn=0
      #round constants to nearest power of 2 of the number of bits we want
      bitsPerConst = 6
      am = roundbits(am,bitsPerConst)
      bn = roundbits(bn,bitsPerConst)
      # print(am,bn)
      
      
      #append the new terms onto the recorded fourier transform
      ftterms[-1] += [[am,bn]]
      
      ts = [i/resolution for i in range(resolution*len(datachunk))] #generate the time samples at the given resolution
      y = calcFxn(ftterms[-1],ts,m,n,T) 
      
      #generate ftdata from y - group by resolution size, round the average of each group if >a0
      ftdata = zip(*(iter([round(e) for e in y]),)*resolution)
      ftdata = [int(round(sum(e)/len(e))) for e in ftdata]
      
      if(verbose): print(*datachunk,sep="")
      if(verbose): print(*ftdata,sep="",end="\t")
      if(verbose): print(ftdata==datachunk,n,end="\n\n")
      

    
    
    #plot the data
    if(plotData):
      plt.plot(ts,y,label="ft")
      origdata = [datachunk[int(t)] for t in ts]
      recondata = [round(e) for e in y] #round to get appx values
      
      #generate plottable data
      recondata = zip(*(iter(recondata),) * resolution)
      recondata = [round(sum(e)/len(e)) for e in recondata]
      recondata = [recondata[int(e/resolution)] for e in range(len(recondata)*resolution)]
      
      plt.plot(ts,origdata,label="orig")
      plt.plot(ts,recondata,label="recon")
      plt.legend(bbox_to_anchor=(1,1), loc="upper left")
      plt.grid(True)
      plt.show()
    
  return ftterms

#treat the data as two different equations (one determines if it's odd or even, the other if it's low or high)
#advantages: low resolution needed
#disadvantages: needs 2 equations
def twoeqtn(fullData,window,plotData=True,resolution=10,verbose=True):
  ftdata = [] #data generated by the fourier transform
  ftterms = [] #terms generated by the fourier transform, should be formatted as list of lists of terms
  winStart=winEnd=0 #starting point for where the window should be placed
  
  #while there's still data to process
  while winEnd<len(fullData):
    ftterms.append([[],[]]) #append the next set of data
    winStart = winEnd #set the starting bit to the last ending bit (since data is captured from start (inclusive) to end (exclusive))
    winEnd = winStart+min(len(fullData)-winStart,window) #set the end to either the window length or the remaining data points
    datachunk = [int(e) for e in fullData[winStart:winEnd]] #get the data from the start to end points
    isOdd = [e%2 for e in datachunk] #0 for 0 or 2, 1 for 1 or 3
    isHigh = [e>=2 for e in datachunk] #0 for 0 or 1, 1 for 2 or 3
    
    m=n=0 #m and n constants in the fourier transform
    T = len(datachunk) #T constant in the fourier transform
    odda0 = 1/T*sum(isOdd)
    higha0 = 1/T*sum(isHigh)
    # a0 = round(1/T*sum(datachunk),roundconst) #because data is square waves of height=1, then the integral over a period is simply the sums of the 1's
    ftterms[-1][0] += [odda0]
    ftterms[-1][1] += [higha0]
    
    
    #keep adding terms until the approximation becomes good enough
    while ftdata!=datachunk: #do until data is valid
      n+=1 #summation starts at 1 and can go up to infinity
      m+=1
      higham = 2/T*quad(cosfxn,0,T,args=(2*pi*m/T,isHigh))[0]
      highbn = 2/T*quad(sinfxn,0,T,args=(2*pi*n/T,isHigh))[0]
      oddam = 2/T*quad(cosfxn,0,T,args=(2*pi*m/T,isOdd))[0]
      oddbn = 2/T*quad(sinfxn,0,T,args=(2*pi*n/T,isOdd))[0]
      
      
      #round constants to nearest power of 2 of the number of bits we want
      bitsPerConst = 6
      higham = roundbits(higham,bitsPerConst)
      highbn = roundbits(highbn,bitsPerConst)
      oddam = roundbits(oddam,bitsPerConst)
      oddbn = roundbits(oddbn,bitsPerConst)
      # print(am,bn)
      #have a cutoff that if the abs(am|bn)<cutoff: am|bn=0, reduce data
      # print(am,bn,end="\t")
      constCutoff = 0.04
      if(abs(higham)<=constCutoff): higham=0
      if(abs(highbn)<=constCutoff): highbn=0
      if(abs(oddam)<=constCutoff): oddam=0
      if(abs(oddbn)<=constCutoff): oddbn=0
      
      #append the new terms onto the recorded fourier transform
      ftterms[-1][0] += [[higham,highbn]]
      ftterms[-1][1] += [[oddam,oddbn]]
      
      ts = [i/resolution for i in range(resolution*len(datachunk))] #generate the time samples at the given resolution
      highy = calcFxn(ftterms[-1][0],ts,m,n,T)
      oddy = calcFxn(ftterms[-1][1],ts,m,n,T)
      
      #generate ftdata from y - group by resolution size, round the average of each group if >a0
      highdata = zip(*(iter([round(e) for e in highy]),)*resolution)
      odddata = zip(*(iter([round(e) for e in oddy]),)*resolution)
      highdata = [int(round(sum(e)/len(e))) for e in highdata]
      odddata = [int(round(sum(e)/len(e))) for e in odddata]
      ftdata = [odddata[i]+2*highdata[i] for i in range(len(highdata))]
      
      if(verbose): print(*datachunk,sep="")
      if(verbose): print(*ftdata,sep="",end="\t")
      if(verbose): print(ftdata==datachunk,n,end="\n\n")
      
    #plot the data
    if(plotData):
      plt.plot(ts,highy,label="high")
      plt.plot(ts,oddy,label="odd")
      origdata = [datachunk[int(t)] for t in ts]
      
      #generate plottable data
      reconhigh = zip(*(iter(highy),) * resolution)
      reconodd = zip(*(iter(oddy),) * resolution)
      
      reconhigh = [round(sum(e)/len(e)) for e in reconhigh]
      reconodd = [round(sum(e)/len(e)) for e in reconodd]
      
      recondata = [reconodd[int(i/resolution)]+2*reconhigh[int(i/resolution)] for i in range(len(reconhigh)*resolution)]
      
      plt.plot(ts,origdata,label="orig")
      plt.plot(ts,recondata,label="recon")
      plt.legend(bbox_to_anchor=(1,1), loc="upper left")
      plt.grid(True)
      plt.show()
    
  return ftterms





#treat the data as three different equations (one determines if it's 1, another 2, another 3 (could also treat as >0,>1,or >2)
def threeeqtn(fullData,window,plotData=True,resolution=10,verbose=True):
  ftdata = [] #data generated by the fourier transform
  ftterms = [] #terms generated by the fourier transform, should be formatted as list of lists of terms
  winStart=winEnd=0 #starting point for where the window should be placed
  
  #while there's still data to process
  while winEnd<len(fullData):
    ftterms.append([[],[]]) #append the next set of data
    winStart = winEnd #set the starting bit to the last ending bit (since data is captured from start (inclusive) to end (exclusive))
    winEnd = winStart+min(len(fullData)-winStart,window) #set the end to either the window length or the remaining data points
    datachunk = [int(e) for e in fullData[winStart:winEnd]] #get the data from the start to end points
    isOdd = [e%2 for e in datachunk] #0 for 0 or 2, 1 for 1 or 3
    isHigh = [e>=2 for e in datachunk] #0 for 0 or 1, 1 for 2 or 3
    
    m=n=0 #m and n constants in the fourier transform
    T = len(datachunk) #T constant in the fourier transform
    odda0 = 1/T*sum(isOdd)
    higha0 = 1/T*sum(isHigh)
    # a0 = round(1/T*sum(datachunk),roundconst) #because data is square waves of height=1, then the integral over a period is simply the sums of the 1's
    ftterms[-1][0] += [odda0]
    ftterms[-1][1] += [higha0]
    
    
    #keep adding terms until the approximation becomes good enough
    #TODO: have bitsPerConst defined outside this loop, but have it increment if n|m get too high (like>20 or so)
    while ftdata!=datachunk: #do until data is valid
      n+=1 #summation starts at 1 and can go up to infinity
      m+=1
      higham = 2/T*quad(cosfxn,0,T,args=(2*pi*m/T,isHigh))[0]
      highbn = 2/T*quad(sinfxn,0,T,args=(2*pi*n/T,isHigh))[0]
      oddam = 2/T*quad(cosfxn,0,T,args=(2*pi*m/T,isOdd))[0]
      oddbn = 2/T*quad(sinfxn,0,T,args=(2*pi*n/T,isOdd))[0]
      
      
      #round constants to nearest power of 2 of the number of bits we want
      bitsPerConst = 6
      higham = roundbits(higham,bitsPerConst)
      highbn = roundbits(highbn,bitsPerConst)
      oddam = roundbits(oddam,bitsPerConst)
      oddbn = roundbits(oddbn,bitsPerConst)
      # print(am,bn)
      #have a cutoff that if the abs(am|bn)<cutoff: am|bn=0, reduce data
      # print(am,bn,end="\t")
      constCutoff = 0.04
      if(abs(higham)<=constCutoff): higham=0
      if(abs(highbn)<=constCutoff): highbn=0
      if(abs(oddam)<=constCutoff): oddam=0
      if(abs(oddbn)<=constCutoff): oddbn=0
      
      #append the new terms onto the recorded fourier transform
      ftterms[-1][0] += [[higham,highbn]]
      ftterms[-1][1] += [[oddam,oddbn]]
      
      ts = [i/resolution for i in range(resolution*len(datachunk))] #generate the time samples at the given resolution
      highy = calcFxn(ftterms[-1][0],ts,m,n,T)
      oddy = calcFxn(ftterms[-1][1],ts,m,n,T)
      
      #generate ftdata from y - group by resolution size, round the average of each group if >a0
      highdata = zip(*(iter([round(e) for e in highy]),)*resolution)
      odddata = zip(*(iter([round(e) for e in oddy]),)*resolution)
      highdata = [int(round(sum(e)/len(e))) for e in highdata]
      odddata = [int(round(sum(e)/len(e))) for e in odddata]
      ftdata = [odddata[i]+2*highdata[i] for i in range(len(highdata))]
      
      if(verbose): print(*datachunk,sep="")
      if(verbose): print(*ftdata,sep="",end="\t")
      if(verbose): print(ftdata==datachunk,n,end="\n\n")
      
    #plot the data
    if(plotData):
      plt.plot(ts,highy,label="high")
      plt.plot(ts,oddy,label="odd")
      origdata = [datachunk[int(t)] for t in ts]
      
      #generate plottable data
      reconhigh = zip(*(iter(highy),) * resolution)
      reconodd = zip(*(iter(oddy),) * resolution)
      
      reconhigh = [round(sum(e)/len(e)) for e in reconhigh]
      reconodd = [round(sum(e)/len(e)) for e in reconodd]
      
      recondata = [reconodd[int(i/resolution)]+2*reconhigh[int(i/resolution)] for i in range(len(reconhigh)*resolution)]
      
      plt.plot(ts,origdata,label="orig")
      plt.plot(ts,recondata,label="recon")
      plt.legend(bbox_to_anchor=(1,1), loc="upper left")
      plt.grid(True)
      plt.show()
    
  return ftterms
  
  






if(len(sys.argv)!=2):
  raise ValueError("please pass a numeric number of bytes as an argument")
else:
  rndBytes = int(sys.argv[1])
# fullData = getRandData(rndBytes,fromFile=True)
fullData = getDataFromFile("./nggyu.mp3")[:rndBytes]
# print(fullData)
fullData = "".join([int2base(e,4,0).zfill(4) for e in fullData])
#window = int(input("window size:"))
window=len(fullData)

print(fullData)

print(fullData,window)
# c = oneeqtn(fullData,window)
c = twoeqtn(fullData,window)

print(*c,sep="\n")