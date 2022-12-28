#pt 1 - max sum of calories carried by an elf

with open("./day01in.txt",'r') as f:
  d = f.read()
  f.close()

elflist = d.split("\n\n")
print(len(elflist),"elves")

#get each calories held per elf
elfcals = [e.split("\n") for e in elflist]
elfcals = [[int(e) for e in f if len(e)>0] for f in elfcals]

#get total cals held per elf
totalcals = [sum(e) for e in elfcals]

#get most cals held by an elf
maxcals = max(totalcals)

print(maxcals)


#pt 2 - find the sum of the top 3 total cals

top3 = sum(sorted(totalcals)[-3:])

print(top3)
