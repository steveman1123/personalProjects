#generate a dataset that has even or odd numbers based on a pattern

import random


#generate a dataset and write it to a file
#datapoints = number of datapoints to put into the set
#pattern = list of 0's and 1's determining if the number should be even or odd (eg [0,0,0,1] would yield a repeating dataset of even, even, even, odd)
#datafile = where to store the dataset
def makedataset(datapoints,pattern,datafile,verbose=False): 
  print(datafile)
  ds = []
  for i in range(datapoints):
    n=1
    while n%2:
      n = random.randint(0,99)
    n+=pattern[i%len(pattern)]
    # print(n)
    ds+=[n]

  with open(datafile,'w') as f:
    f.write("\n".join([str(e) for e in ds]))
    f.close()

#generate three datasets with the given number of datapoints
datapoints = 50

#first dataset should have even, even, even, odd
makedataset(datapoints,[0,0,0,1],"datasets/ds1eo.txt")
makedataset(datapoints,[0,1],"datasets/ds2eo.txt")
makedataset(datapoints,[1,1,0,0,0,1,0],"datasets/ds3eo.txt")
makedataset(datapoints,[1,1,1,1,0,1,0],"datasets/ds4eo.txt")
makedataset(datapoints,[1,0],"datasets/ds5eo.txt")


print("done")