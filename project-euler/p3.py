from math import prod

n = 600851475143
#n = 13195

sqrtn = n**0.5



with open("./1Mprimes.txt",'r') as f:
  primes = f.readlines()
  primes = [int(e) for e in primes]


primes = [e for e in primes if e<sqrtn]
print("going through",len(primes),"primes")
factors = []
i = -1
while i>-len(primes):
  if(n/primes[i] == int(n/primes[i])):
    factors += [primes[i]]
  i -= 1

print(factors)
if(prod(factors) == n):
  print("that's everyone")

