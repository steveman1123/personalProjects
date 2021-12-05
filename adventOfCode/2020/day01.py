from functools import reduce

with open("./day01in.txt",'r') as f:
  t = f.read()

t = t.split('\n')
t = [int(e) for e in t if len(e)>0 and int(e)<2020]

out = []


#given list l, find n numbers that add to s
#return the numbers that add to s
def findSum(l, n, s):
  if(n>len(l)):
    raise("Out of Bounds")
  if(len(l)==0):
    raise("List Empty")
  
  
  


for i in range(0,len(t)-1):
  for j in range(i+1,len(t)-1):
    for k in range(j+1,len(t)-1):
      if(t[i]+t[j]+t[k]==2020):
        out = [t[i],t[j],t[k]]
        break

out = reduce((lambda x, y: x * y), out)

print(out)