from math import prod


def prodofstr(s):
  l = list(s)
  l = [int(e) for e in l]
  p = prod(l)
  return p



window = 13

data = open("p7.txt",'r').read()

maxprod = 0
for i in range(len(data)-window):
  maxprod = max(maxprod,prodofstr(data[i:i+window]))

print(maxprod)


