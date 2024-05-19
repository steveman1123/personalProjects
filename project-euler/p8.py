'''
a**2 + b**2 = c**2
a + b + c = 1000

c = sqrt(a**2 + b**2)

a + b + sqrt(a**2 + b**2) = 1000
a < b < c

a*b*c = ?
'''

q = 0
a = 0
b = 0
for a in range(-1000,1000):
  for b in range(-1000,1000):
    q = a + b + (a**2 + b**2)**0.5
    if q == 1000:
      break
  
c = (a**2 + b**2)**0.5
print(a,b,c)
print(a*b*c)
