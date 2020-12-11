#from copy import deepcopy

with open('day11in.txt','r') as f:
  b = f.read().split('\n')

#return the number of occupied adjacent seats for a given row/col seat in a given boat
#Note: this function could be optimized to remove conditionals using more mins & max's
def numOcc(b, r, c, symb): #where symb = symbol denoting if something is occupied or not
  if(r>0):
    if(r<len(b)-1):
      occ = b[r-1][max(0,c-1):min(len(b[r-1]),c+2)].count(symb)+ \
            b[r][max(0,c-1):min(len(b[r]),c+2)].count(symb)-(b[r][c]==symb)+ \
            b[r+1][max(0,c-1):min(len(b[r+1]),c+2)].count(symb)
    else:
      occ = b[r-1][max(0,c-1):min(len(b[r-1]),c+2)].count(symb)+ \
            b[r][max(0,c-1):min(len(b[r]),c+2)].count(symb)-(b[r][c]==symb)
  else:
    occ = b[r][max(0,c-1):min(len(b[r]),c+2)].count(symb)-(b[r][c]==symb)+ \
          b[r+1][max(0,c-1):min(len(b[r+1]),c+2)].count(symb) 
  return occ

#return the number of occupied seats in the 8 directions for as long as it takes to find a seat there (or the edge)
#note: this function should be able to be optimized too to not run so many loops
def numOccExt(b, r, c, fs='.',os='#',es='L'): #extended numOcc > fs=floor symb, os=occupied symb, es=empty symb
  occ = 0
  
  ra = r-1
  ca = c-1
  #go up to left
  while (ra>=0 and ca>=0) and b[ra][ca] == fs:
    ra -= 1
    ca -= 1
  occ += (ra>=0 and ca>=0 and b[ra][ca]==os)
  
  ra = r-1
  ca = c
  #go up
  while (ra>=0) and b[ra][ca] == fs:
    ra -= 1
  occ += (ra>=0 and b[ra][ca]==os)

  ra = r-1
  ca = c+1
  #go up to right
  while (ra>=0 and ca<len(b[ra])) and b[ra][ca] == fs:
    ra -= 1
    ca += 1
  occ += (ra>=0 and ca<len(b[ra]) and b[ra][ca]==os)

  ra = r
  ca = c+1
  #go right
  while (ca<len(b[ra])) and b[ra][ca] == fs:
    ca += 1
  occ += (ca<len(b[ra]) and b[ra][ca]==os)

  ra = r+1
  ca = c+1
  #go down to right
  while (ra<len(b) and ca<len(b[ra])) and b[ra][ca] == fs:
    ra += 1
    ca += 1
  occ += (ra<len(b) and ca<len(b[ra]) and b[ra][ca]==os)
  
  ra = r+1
  ca = c
  #go down
  while (ra<len(b)) and b[ra][ca] == fs:
    ra += 1
  occ += (ra<len(b) and b[ra][ca]==os)
  
  ra = r+1
  ca = c-1
  #go down to left
  while (ra<len(b) and ca>=0) and b[ra][ca] == fs:
    ra += 1
    ca -= 1
  occ += (ra<len(b) and ca>=0 and b[ra][ca]==os)
  
  ra = r
  ca = c-1
  #go left
  while (ca>=0) and b[ra][ca] == fs:
    ca -= 1
  occ += (ca>=0 and b[ra][ca]==os)
  
  return occ


'''
rules:
- If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
- If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
- Otherwise, the seat's state does not change.
'''

#part 1
tmp = b[:]
prev = tmp[:]
rounds = 0

while prev != tmp or rounds==0:
  prev = tmp[:]
  for r in range(len(prev)):
    for c in range(len(prev[r])):
      if(prev[r][c]=='L' and numOcc(prev,r,c,'#')==0): #if unoccupied
        tmp[r] = tmp[r][:c]+'#'+tmp[r][c+1:]
      elif(prev[r][c]=='#' and numOcc(prev,r,c,'#')>=4):
        tmp[r] = tmp[r][:c]+'L'+tmp[r][c+1:]
  
  
  rounds+=1

pt1 = sum([e.count('#') for e in tmp])

print pt1


'''
new rules are that we don't look at just the adjacent seats, but seats in all 8 cardinal directions
and also not four or more, but five or more
otherwise, same switching as in part 1
'''
#part 2
tmp = b[:]
prev = tmp[:]
rounds = 0

while prev != tmp or rounds==0:
  prev = tmp[:]
  for r in range(len(prev)):
    for c in range(len(prev[r])):
      if(prev[r][c]=='L' and numOccExt(prev,r,c)==0): #if unoccupied
        tmp[r] = tmp[r][:c]+'#'+tmp[r][c+1:]
      elif(prev[r][c]=='#' and numOccExt(prev,r,c)>=5):
        tmp[r] = tmp[r][:c]+'L'+tmp[r][c+1:]
  
  
  #for e in tmp:
  #  print e
  #print '\n'
  
  rounds+=1

pt2 = sum([e.count('#') for e in tmp])

print pt2
