n = 100

squares = [e**2 for e in range(0,n+1)]

sumofsq = sum(squares)

sqofsum = sum(range(0,n+1))**2

diff = sqofsum - sumofsq

print(diff)
