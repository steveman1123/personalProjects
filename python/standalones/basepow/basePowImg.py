'''
the purpose of this is to generate an image from 1's digits of different powers being even or odd in different bases

#black=odd, white=even

'''

import numpy as np
from PIL import Image

n = 10 #power
w = 1600 #number of numbers to go to
h = 1600 #number of bases to check

pixel = np.zeros((h,w))

for b in range(1,h):
  for x in range(w):
    pixel[b,x] = (pow(x,n)%b)
    #pixel[b,x] = int(b*x)

#print(np.max(pixel))
pixel = (255*pixel/float(np.max(pixel))).astype(np.uint8) #scale to 255 as max
#print(pixel)
print(n)

Image.fromarray(pixel).save('pow'+str(n)+'a.bmp')
