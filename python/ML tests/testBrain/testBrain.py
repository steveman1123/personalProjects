#This is a test to make a brain/neural network
from random import randint
from time import sleep
import numpy

nodeNum = int(input("Number of Nodes: "))
iCons = int(input("Number of Initial Connections: "))
itNum = int(input("Number of Iterations: "))

conns = numpy.zeros(nodeNum*nodeNum, int)

#give initial random connections
for i in range(0,iCons):
    nodeA = randint(0,nodeNum-1)
    nodeB = randint(0,nodeNum-1)
    conns[nodeA*nodeNum+nodeB] += 1

for itCount in range(0,itNum):
    print(itCount, "   ", conns)
    nodeA = randint(0,nodeNum-1)
    obc = 0 #obc = out bound connections
    for i in range(0, nodeNum-1):
        obc += conns[nodeA*nodeNum+i]
        
    #cue arbetrary rules here:
    if obc % 2: #odd
        obn = 0 # obn = out bound connections per node
        for i in range(0,nodeNum-1): #all node connections for nodeA
            obn = conns[nodeA*nodeNum+i] 
            for j in range(0,obn): #
                if randint(0,1):
                    conns[nodeA*nodeNum+i]+=1
    else: #even
        nodeB = randint(0,nodeNum-1)
        conns[nodeA*nodeNum+nodeB]+=1
    #sleep(2)


