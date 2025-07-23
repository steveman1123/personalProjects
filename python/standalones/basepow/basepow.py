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


r = 9
d = 1

#maxX = r**(d+1)+r
maxX = 20
maxN = 90

print(f"r={r}, d={d}")
print()

for n in range(maxN):
  print(n,end="\t")
  for x in range(maxX):
    a = x**n
    b = numberToBase(a,r)
    if(len(b)<d+1):
      b = [0]*(d+1-len(b))+b
    #print(b)
    print(b[-(d+1)],end="")
  print("")
  