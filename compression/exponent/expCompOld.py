#perform the exponential compression version


'''
s=0
for i in range(1,10):
  print(i)
  print(i**15,"\n")
  s+=i**15

print(s)
'''

import time


#compress original data
def compress(data):
  out = ""
  maxPow = 15
  maxBase = 9
  
  #convert data to ascii values (ensure the leading 0 if necessary
  ascii = [str(ord(c)) if ord(c)>=100 else "0"+str(ord(c)) for c in data]
  print("original data size:",len(ascii))
  
  out = "".join(ascii) #join to become a single number
  print("cur:",out,len(out))
  maxVal = sum([i**maxPow for i in range(1,maxBase+1)])
  print("max:",maxVal,len(str(maxVal)))
  
  remaining = int(out)
  
  
  #TODO: figure out how to split into pieces for when the data is too large to fit into some bits
  if(remaining)>sum([i**maxPow for i in range(1,maxBase+1)]):
    print("data too large")
    exit()
  #  outList = 
  
  i=maxBase #start with 9
  powList = []
  while i>0 and remaining>0:
    temp=-1
    print(i,"remaining:",remaining)
    pow=maxPow+1
    #look back through the power
    while temp<0:
      pow-=1
      temp=remaining-i**pow
      print("\tpow,temp:",pow,temp)
    
    #then look back through the scalar
    temp2 = temp
    scale=0
    while temp2>0 and scale<i:
      scale+=1
      temp2 = temp-scale*i**pow #TODO: I think this math here is wrong
      print("\tscalar,temp2:",scale,temp2)
      
      
    powList.append([scale,i,pow])
    remaining -= scale*i**pow
    i-=1
    print("\n\tpowList:",powList,"\n")
    time.sleep(1)
  if(remaining>0):
    print("incomplete")
  out = powList
  return out


#decompress encoded data
def decompress(data):
  out = ""


din = input("test data: ")
#din = "Hello, world."
dout = compress(din)
print(dout)