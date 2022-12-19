#calculate the polynomial coefficients given points using only algebra

#pts should be 2d array of format [[x1,y1],[x2,y2]]
#get the largest coefficient (eg "a" in ax^2+bx+c or "a" in ax^3+cx+d)
#eqtn format is (a-b)/(c-d)
#where a and b recurse down to singular y values, and c and d are x values
#pts = list of points [[x1,y1],[x2,y2]]
#n = point index. Should init with len of  pts
#pow = power. Should init with len(pts)-1
def getBigNum(pts, n, pow):
  if (n>0):
    if (pow<=0):
      return pts[0][1]
    elif (pow==1):
      return (pts[n-1][1] - pts[0][1])/(pts[n-1][0] - pts[0][0])
    else:
      return (getBigNum(pts, n, pow-1)-getBigNum(pts, n-1, pow-1))/(pts[n-1][0] - pts[n-pow][0])
  else:
    return 0


#calculates all possible ways of obtaining pow power with n number, a initiates as 0
#eg (pts, 3, 1, 0) returns x1+x2+x3 -- (pts, 2, 3, 0) returns x1(x1(x1+x2)+x2(x2))+x2(x2(x2))
#pts = list of points [[x1,y1],[x2,y2]]
#n=number of points
#pow=power to look at
#a=counter?
def mult(pts, n, pow, a=0):
  out = 0
  if(pow<1):
    out = 0
  elif(pow==1): #sums x vals from a thru n-1 inclusively
    if (a<=n-1):
      for i in range(a,n):
        out += pts[i][0]
  else:
    for b in range(a,n):
      out += pts[b][0]*mult(pts, n, pow-1, b)
  return out


#generate the coefficients of the polynomial given a set of points
#pts = list of points [[x1,y1],[x2,y2]]
#TODO: figure out how to return fractional components rather than decimal since decimals can be lossy with computers
def geteqtn(pts):
  n = len(pts)
  if(n==0): return None
  if(n==1): return pts[0][1]
  pow = n-1
  eqtn = [None for e in range(n)]
  
  for a in range(pow+1):
    sum=0
    for b in range(a,0,-1):
      sum += eqtn[a-b]*mult(pts, n-a, b)
    eqtn[a] = getBigNum(pts, n-a, pow-a) - sum
  
  return eqtn


i=0
pts = []
while True:
  i+=1
  x = float(input(f"x{i}: "))
  if(x in [pt[0] for pt in pts]): break
  y = float(input(f"y{i}: "))
  pts.append([x,y])
  eq = geteqtn(pts)
  print(eq)