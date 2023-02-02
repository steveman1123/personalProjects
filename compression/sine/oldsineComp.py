from numpy.fft import fft,ifft
import numpy as np
from matplotlib import pyplot as plt
from math import atan

#a = np.array([1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0])
#a = np.array([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0])

#data = input("data: ")
data = open("./rndFile.dat").read()[:400]

print()

print("data")
print(data)

ascii = [ord(c) for c in data]
print("ascii")
print(ascii)
#isolate the first number (100's digit)
#ascii = [int(c/100) for c in ascii]
#convert numbers to complex
a=[]
#for i in range(0,len(ascii)-1,2):
#  a.append(ascii[i]+complex(str(ascii[i+1])+"j"))

for i in range(0,len(ascii)-3,4):
  a.append(ascii[i]+ascii[i+1]/1000+complex(str(ascii[i+2]+ascii[i+3]/1000)+"j"))
#plt.plot(ascii)
#plt.show()


#try doing a single sine wave per number
#current question: how can we determine the frequencies based on nodes (+ to - or - to + crossovers)







'''
#try using fourier transforms

maxRound = 3

#get the fft and ifft (ifft for check)
ft = np.round(fft(a),maxRound)
print("ft")
for i,e in enumerate(ft):
  print(i,e,((e.real**2+e.imag**2)**0.5,atan(e.imag/e.real)))

ift = np.round(ifft(ft),maxRound)

print()
print("a")
print(a)
print("ift")
print(ift)

#ift = [round(e.real)+complex(str(round(e.imag))+"j") for e in ift]
#print("ift rounded")
#print(ift)

print()
print("ift==a")
print((ift==a))
'''