#live capture webcam feeds, apply filters, view disparity


import numpy as np
import cv2

#index of your camera
vidStreamL = cv2.VideoCapture(1)
vidStreamR = cv2.VideoCapture(2)

print("Cameras Enabled\nPress Space to Stop\n")

minDisp = 0 #original: 0
maxDisp = 16 #original: 16

# see imgcomp3.py
stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)

while(True):
  #get image from cameras
  retL, imgL = vidStreamL.read()
  retR, imgR = vidStreamR.read()

  #convert to greyscale
  grayL = cv2.cvtColor(imgL,cv2.COLOR_BGR2GRAY)
  grayR = cv2.cvtColor(imgR,cv2.COLOR_BGR2GRAY)

  disp = stereo.compute(grayL, grayR) #compute disparity  
  
  cv2.imshow('left',imgL)
  cv2.imshow('right',imgR)
  cv2.imshow('disp',disp/(disp.max()-disp.min()))


  k = cv2.waitKey(1) & 0xFF #get key and mask so it continues without stopping
  if(k == 32): #if space
    break

