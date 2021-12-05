'''
import numpy as np
import os,sys
#import Image
jpgfile = np.image.open("dna.jpg")

print(jpgfile.bits, jpgfile.size, jpgfile.format)
'''


import skimage.color
from skimage.color import rgb2grey
from skimage import data, io, filters
from skimage.filters import gaussian

image = data.imread('F:\\Docs\\Misc\\Tech\\MyPrograms\\nucTest\\duck.jpg')
grey = rgb2grey(image)
hpf = gaussian(grey, sigma=0.4)

io.imshow(image)
io.show()

io.imshow(grey)
io.show()

io.imshow(hpf)
io.show()