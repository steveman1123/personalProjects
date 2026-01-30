'''
the purpose of this is to generate the sequence of digits from:
x^n _r | d
where:
x = base number
n = power
r = radix/base
d = digit (in the number 1234, d=0 refers to 4, d=1 to 3, d=2 to 2, and d=3 to 1)
all are positive integers

to test and refine the postulate that the sequences will repeat as x increases, and as n increases
'''

def numberToBase(n, b):
  if n == 0:
    return [0]
  digits = []
  while n:
    digits.append(int(n % b))
    n //= b
  return digits[::-1]

#radix
r = 10
#digit significance (0=least significant)
d = 1

maxX = r**(d+1)+r
#maxX = 30
maxN = 100

print(f"r={r}, d={d}")
print()


#TODO: add a set of unique digitstr's and call out if the next exists in the set
occurances = dict()
for n in range(maxN): #[*range(17),*range(140,155)]: #range(maxN):
  print(n,end="\t")
  digitstr = ""
  for x in range(maxX):
    a = x**n
    b = numberToBase(a,r)
    if(len(b)<d+1):
      b = [0]*(d+1-len(b))+b
    digitstr += str(b[-(d+1)])
    if(digitstr in occurances):
      occurances[digitstr] += 1
    else:
      occurances[digitstr] = 0
  print(digitstr,sum([int(e) for e in digitstr]),occurances[digitstr],sep="\t")
  