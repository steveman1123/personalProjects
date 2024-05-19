n = 1000

threes = range(0,n,3)
fives = range(0,n,5)
print(len(threes),"threes")
print(len(fives),"fives")

only3s = [e for e in threes if e not in fives]
#only5s = [e for e in fives if e not in threes]



print("sum:")
print(sum(only3s)+sum(fives))
