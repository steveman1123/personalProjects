import numpy as np

f = open("input1.txt","r")

arr = np.fromstring(f.read(),dtype=int,sep="\r\n")

print(sum(arr)) #part 1 - find final frequency


#part 2 - find the first freq that appears twice
import collections as c

multi = []
cumSum = []
initVal = 0

while len(multi)<1:
  #the following line appends the newst group of freqs to the known ones
  #print(cumSum[0:len(cumSum)-1])
  #print(np.cumsum(np.append(initVal,arr)))
  
  cumSum = np.append(cumSum[0:len(cumSum)-1],np.cumsum(np.append(initVal,arr)))
  for i in range(len(cumSum)-len(arr),len(cumSum)):
    print(str(cumSum[i])+", "+str(arr[i]))
  
  y = c.Counter(cumSum) #count occurances of unique values
  multi = [i for i in y if y[i]>1] #check for multiple occurances
  #print(len(multi))
  initVal = cumSum[len(cumSum)-1] #change init value
  
print(multi)


print("Done")