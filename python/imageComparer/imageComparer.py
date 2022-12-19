import numpy as np
import cv2
from matplotlib import pyplot as plt

imset= input("image set: ")


imgL = cv2.imread(imset+'L.png',2)
imgR = cv2.imread(imset+'R.png',2)

#retL, imgL = (cv2.VideoCapture(0)).receive()
#retR, imgR = (cv2.VideoCapture(1)).receive()

minDisp = 0
maxDisp = 16

#https://docs.opencv.org/master/d2/d85/classcv_1_1StereoSGBM.html
stereo = cv2.StereoSGBM_create(
  minDisparity = minDisp,
  numDisparities = maxDisp-minDisp,
  blockSize = 32,
  #P1 = 0,
  #P2 = 10,
  #disp12MaxDiff = 10,
  #preFilterCap = 10,
  #uniquenessRatio = 10,
  #speckleWindowSize = 100,
  #speckleRange = 15,
  #mode = False
)

disp = stereo.compute(imgL, imgR)

cv2.imshow('disp', (disp-minDisp)/(maxDisp-minDisp)) #scale greyness then display
#plt.imshow(disp, 'gray') #title, file to display
#plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()