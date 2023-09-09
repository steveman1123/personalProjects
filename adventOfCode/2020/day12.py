import math

with open('day12in.txt','r') as f:
  d = f.read().split('\n')

d = [[e[0],int(e[1:])] for e in d if len(e)>0]

lat=lon=h=0

for e in d:
  if(e[0]=='N'):
    lon-=e[1]
  elif(e[0]=='S'):
    lon+=e[1]
  elif(e[0]=='E'):
    lat+=e[1]
  elif(e[0]=='W'):
    lat-=e[1]
  elif(e[0]=='L'):
    h-=e[1]
  elif(e[0]=='R'):
    h+=e[1]
  elif(e[0]=='F'):
    lat+=round(math.cos(h/180*math.pi),0)*e[1]
    lon+=round(math.sin(h/180*math.pi),0)*e[1]
    
pt1 = abs(lat)+abs(lon)
print(pt1)


wlat = 10 #waypoint position
wlon = 1
slat = slon = 0 #ship position

for e in d:
  if(e[0]=='N'):
    wlon+=e[1]
  elif(e[0]=='S'):
    wlon-=e[1]
  elif(e[0]=='E'):
    wlat+=e[1]
  elif(e[0]=='W'):
    wlat-=e[1]
  elif(e[0]=='L'):
    if e[1]%360==90:
      [wlat,wlon]=[-wlon,wlat]
    if e[1]%360==180:
      [wlat,wlon]=[-wlat,-wlon]
    if e[1]%360==270:
      [wlat,wlon]=[wlon,-wlat]
  elif(e[0]=='R'):
    if e[1]%360==90:
      [wlat,wlon]=[wlon,-wlat]
    if e[1]%360==180:
      [wlat,wlon]=[-wlat,-wlon]
    if e[1]%360==270:
      [wlat,wlon]=[-wlon,wlat]
  elif(e[0]=='F'):
    slat+=wlat*e[1]
    slon+=wlon*e[1]

pt2 = abs(slat)+abs(slon)
print(pt2)
