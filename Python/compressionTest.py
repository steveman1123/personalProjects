
import random, string, os

dataFile = "./rndFile.dat"

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
  rndstr = open(dataFile,'r').read()


##begin data compression


#ptList should dict of format {x:y}
def geteqtn(ptList,layer=0):
  #call this as a recursive function to generate the values
  
  
  return []