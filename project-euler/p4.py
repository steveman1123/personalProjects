n = 3
a = 10**n - 1
b = 10**n - 1

allps = []
for ai in range(a,0,-1):
  for bi in range(ai,0,-1):
    p = ai*bi
    if str(p) == str(p)[::-1]:
      #print(ai,bi,p)
      allps += [p]

print(max(allps))
