#generate a dataset that is greater than or less than based on a pattern

import random


#generate a dataset and write it to a file
#datapoints = number of datapoints to put into the set
#pattern = list of 0's and 1's determining if the number should be even or odd (eg [0,0,0,1] would yield a repeating dataset of even, even, even, odd)
#datafile = where to store the dataset
def makedataset(datapoints,pattern,datafile,verbose=False): 
  print(datafile)
  ds = [random.randint(2*datapoints,4*datapoints)]
  for i in range(datapoints):
    if(pattern[i%len(pattern)]):
      #this number should be larger than the previous number (but make sure we can keep increasing if need be)
      lobound = ds[-1]
      hibound = 4*datapoints+i
    else:
      #this number should be smaller than the previous number
      lobound = datapoints-i
      hibound = ds[-1]
      
    # print(pattern[i%len(pattern)],lobound,hibound,sep="\t",end="\t")
    n = random.randint(lobound,hibound)
    # print(n)

    ds+=[n]

  with open(datafile,'w') as f:
    f.write("\n".join([str(e) for e in ds]))
    f.close()

#generate three datasets with the given number of datapoints
datapoints = 25

#first dataset should have even, even, even, odd
makedataset(datapoints,[0,0,0,1],"ds1ls.txt")
makedataset(datapoints,[0,1],"ds2ls.txt")
makedataset(datapoints,[1,1,0,0,0,1,0],"ds3ls.txt")
makedataset(datapoints,[1,1,1,1,0,1,0],"ds4ls.txt")
makedataset(datapoints,[1,0],"ds5ls.txt")


print("done")