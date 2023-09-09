#pt 1 - the score for a single round is the score for the selected shape (X=1,Y=2,Z=3) + outcome (0=lose,3=draw,6=won)

#input data
with open("./day02in.txt",'r') as f:
  din = f.read()
  f.close()

#dinlist = din.split("\n") #seperate by line

'''
just do a simple replace
A X = AA = 1+3
A Y = AB = 2+6
A Z = AC = 3+0
B X = BA = 1+0
B Y = BB = 2+3
B Z = BC = 3+6
C X = CA = 1+6
C Y = CB = 2+0
C Z = CC = 3+3
'''
roundtypes = [
["A X","4"],
["A Y","8"],
["A Z","3"],
["B X","1"],
["B Y","5"],
["B Z","9"],
["C X","7"],
["C Y","2"],
["C Z","6"]
]



#get the numeric values for each round
dinnums = din
for r in roundtypes:
  dinnums = dinnums.replace(r[0],r[1])

#convert from string to int
dinnums = dinnums.split("\n")
dinnums = [int(e) for e in dinnums if len(e)==1]

#total score
totalscore = sum(dinnums)

print(totalscore)


#pt 2 - new meaning - x=lose, y=draw, z=win
'''
new round type rules:
A X = AC = 3+0
A Y = AA = 1+3
A Z = AB = 2+6
B X = BA = 1+0
B Y = BB = 2+3
B Z = BC = 3+6
C X = CB = 2+0
C Y = CC = 3+3
C Z = CA = 1+6
'''

roundtypes = [
["A X","3"],
["A Y","4"],
["A Z","8"],
["B X","1"],
["B Y","5"],
["B Z","9"],
["C X","2"],
["C Y","6"],
["C Z","7"]
]


#get the numeric values for each round
dinnums = din
for r in roundtypes:
  dinnums = dinnums.replace(r[0],r[1])

#convert from string to int
dinnums = dinnums.split("\n")
dinnums = [int(e) for e in dinnums if len(e)==1]
#total score
totalscore = sum(dinnums)

print(totalscore)
