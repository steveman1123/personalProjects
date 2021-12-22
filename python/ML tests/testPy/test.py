'''
Simple and fast image transforms to mimic:
 - brightness
 - contrast
 - erosion
 - dilation
'''

import cv2
from pylab import array, uint8

# Image data
image = cv2.imread('duck.jpg',0) # load as 1-channel 8bit grayscale
maxIntensity = 255.0 # depends on dtype of image data

# Parameters for manipulating image data
phi = 1
theta = 2

# Increase intensity such that
# dark pixels become much brighter,
# bright pixels become slightly bright
newImage0 = (maxIntensity/phi)*(image/(maxIntensity/theta))**0.5
newImage0 = array(newImage0,dtype=uint8)


# Decrease intensity such that
# dark pixels become much darker,
# bright pixels become slightly dark

newImage1 = array((maxIntensity/phi)*(image/(maxIntensity/theta))**1.5,dtype=uint8)

cv2.imshow('original',image)
cv2.imshow('increase brightness',newImage0)
cv2.imshow('decrease brightness',newImage1)

# any key to close windows
closeWindow = -1
while closeWindow<0:
    closeWindow = cv2.waitKey(1)
cv2.destroyAllWindows()