#https://projecteuler.net/problem=50
#which prime less than 1M is the sum of the most consecutive primes?

import math,os

#generate list of primes less than 1M (or read from file if available)
primefile = "./1Mprimes.txt"
if(os.path.isfile(primefile)):
  print("reading from prime file")
  with open(primefile,'r') as f:
    primes = f.read().split("\n")
    f.close()
    primes = [int(e) for e in primes if len(e)>0]
else:
  primes = [2,3] #init with the first couple since they're too close
  #only look at odd numbers
  for i in range(5,1000000,2):
    if(int(math.log(i,10))>int(math.log(i-2,10))): print(i-1)
    j=3
    while (j<math.sqrt(i)) and ((i/j)!=int(i/j)):
      j+=2
    if(j>math.sqrt(i)):
      primes.append(i)
  
  print("writing to file")
  with open(primefile,'w') as f:
    for p in primes:
      f.writelines(str(p)+"\n")
    f.close()

primes = [e for e in primes if e<1000]

print(f"done generating primes - {len(primes)} found")

#this method would work, but it's pretty slow
'''
#create a sliding window that starts as the length of the list and removes one after sliding across every term
maxrange = 1000 #int(len(primes)/2)
for windowlen in range(maxrange,0,-1):
  print(windowlen)
  for windowstart in range(0,len(primes)-windowlen):
    testsum = sum(primes[windowstart:windowstart+windowlen])
    if(testsum in primes):
      print(testsum)
      print("done")
      exit()
'''


#try summing a number and the previous number, and if it's less more than the largest listed prime, go to the next number
#if it's less, then try adding the next number down

for i in range(len(primes),1,-1):
  if(primes[i]+primes[i-1]<primes[-1]):
    print(