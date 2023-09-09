#get the digital roots and 1's place for various numbers and their powers

from functools import reduce

def digitalRoot(n):
  while n > 9:
    n = sum(int(x) for x in str(n))
  return n

#where xs is the number of numbers to read into, and ns are the number of powers to read to
def digitalRootPowers(xs=10,ns=5):
  for n in range(ns):
    print(f"x^{n} : ",end="")
    for x in range(xs):
      print(f"{digitalRoot(pow(x,n))},",end="")
    print("")


#where xs is the number of numbers to read into, and ns are the number of powers to read to
def onesDigitPowers(xs=10,ns=5):
  for n in range(ns):
    print(f"x^{n} : ",end="")
    for x in range(xs):
      print(str(pow(x,n))[-1]+",",end="")
    print("")


xs=10
ns=20

print("digital roots")
digitalRootPowers(xs,ns)
print("")
print("1's digits")
onesDigitPowers(xs,ns)



#TODO: should generate some images with this info