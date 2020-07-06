# nabbed from: https://docs.opencv.org/3.1.0/dd/d53/tutorial_py_depthmap.html 

import numpy as np
import cv2
import time
 
imset = input("image set: ")

imgL = cv2.imread(imset+'L.png',0)
imgR = cv2.imread(imset+'R.png',0)

cv2.imshow('left',imgL)
cv2.imshow('right',imgR)


stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR) 
cv2.imshow('test',disparity/(disparity.max()-disparity.min()))
cv2.waitKey(0)
cv2.destroyAllWindows()
