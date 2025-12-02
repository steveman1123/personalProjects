#based on the code here: https://github.com/colbrydi/Lithophane

import os,sys
import lithophane as li

#get the image as a local image
if(len(sys.argv)==2):
  imagefile = sys.argv[-1]
elif(len(sys.argv)<2):
  imagefile = input("image file: ")
else:
  print("too many arguments provided, please only pass an image url to convert to lithophane")

#Generate xyz point cloud
width = 160 #Width in mm
x,y,z = li.jpg2stl(imagefile, width=width, h = 3, d = 0.5)

#convert flat to cylindrical
#x,y,z = li.makeCylinder(x,y,z)

#Generate stl model from pointcloud and save
model = li.makemesh(x,y,z);
meshfile = imagefile[:-4] + '_lithophane.stl'
print(f"saving mesh to {meshfile}")
model.save(meshfile)

print("done")
