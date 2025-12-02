import os,sys
import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
from skimage.transform import resize
from mpl_toolkits import mplot3d
from matplotlib import pyplot
from stl import mesh


def rgb2gray(rgb):
    """Convert rgb image to grayscale image in range 0-1
    >>> gray = factorial(rgbimg)
    """
    print("converting rgb to greyscale")
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


def scaleim(im, width_mm=40):
    """Scale image to 0.1 pixel width
    For example the following:

    >>> im_scaled = scaleim(im, width_mm = 100)

    Will make an image with 1000 pixels wide.
    The height will be scale proportionally
    """

    ydim = im.shape[0]
    xdim = im.shape[1]

    scale = (width_mm*10/xdim)
    newshape = (int(ydim*scale), int(xdim*scale), 3)
    im = resize(im, newshape)
    return im


def jpg2stl(im='', width='', h=3.0, d=0.5, show=True):
  """Function to convert filename to stl with width = width
  :width: - Required parameter.  Width
  """
  print("converting jpg to stl")
  
  depth = h
  offset = d

  if type(im) == str:
    filename = im
    print(f"Reading {filename}")
    im = img.imread(filename)
  else:
    raise ValueError(f"Invalid image name {filename}")

  if width == '':
    width = im.shape[1]

  print("scaling image")
  im = scaleim(im, width_mm=width)
  im = im/np.max(im)

  # Convert to grayscale
  print("converting to greyscale")
  if len(im.shape) == 3:
    gray = rgb2gray(im)
  else:
    gray = im

  # Invert threshold for z matrix
  ngray = 1 - np.double(gray)

  # scale z matrix to desired max depth and add base height
  z_middle = ngray * depth + offset

  # add border of zeros to help with back
  z = np.zeros([z_middle.shape[0]+2, z_middle.shape[1]+2])
  z[1:-1, 1:-1] = z_middle

  x1 = np.linspace(1, z.shape[1]/10, z.shape[1])
  y1 = np.linspace(1, z.shape[0]/10, z.shape[0])

  x, y = np.meshgrid(x1, y1)

  #option to fil horizontally to have 3d surface on exterior (not flipping will have 3d surface on interior)
  #x = np.fliplr(x)

  return x, y, z


def makeCylinder(x, y, z):
  '''Convert flat point cloud to Cylinder'''
  print("converting flat point cloud to cylinder")
  newx = x.copy()
  newz = z.copy()
  radius = (np.max(x)-np.min(x))/(2*np.pi)
  print(f"Cylinder Radius {radius}mm")
  for r in range(0, x.shape[0]):
    for c in range(0, x.shape[1]):
      t = (c/(x.shape[1]-10))*2*np.pi
      rad = radius + z[r, c]
      newx[r, c] = rad*np.cos(t)
      newz[r, c] = rad*np.sin(t)
  return newx, y.copy(), newz

# Construct polygons from grid data


def makemesh(x, y, z):
  '''Convert point cloud grid to mesh'''
  print("converting pointcloud to mesh")
  count = 0
  points = []
  triangles = []
  for i in range(z.shape[0]-1):
    for j in range(z.shape[1]-1):
      # Triangle 1
      points.append([x[i][j], y[i][j], z[i][j]])
      points.append([x[i][j+1], y[i][j+1], z[i][j+1]])
      points.append([x[i+1][j], y[i+1][j], z[i+1][j]])

      triangles.append([count, count+1, count+2])

      # Triangle 2
      points.append([x[i][j+1], y[i][j+1], z[i][j+1]])
      points.append([x[i+1][j+1], y[i+1][j+1], z[i+1][j+1]])
      points.append([x[i+1][j], y[i+1][j], z[i+1][j]])

      triangles.append([count+3, count+4, count+5])

      count += 6

  # BACK
  for j in range(x.shape[1]-1):
    bot = x.shape[0]-1

    # Back Triangle 1
    points.append([x[bot][j], y[bot][j], z[bot][j]])
    points.append([x[0][j+1], y[0][j+1], z[0][j+1]])
    points.append([x[0][j],   y[0][j],   z[0][j]])

    triangles.append([count, count+1, count+2])

    # Triangle 2
    points.append([x[bot][j], y[bot][j], z[bot][j]])
    points.append([x[bot][j+1], y[bot][j+1], z[bot][j+1]])
    points.append([x[0][j+1], y[0][j+1], z[0][j+1]])

    triangles.append([count+3, count+4, count+5])

    count += 6

  # Create the mesh
  model = mesh.Mesh(np.zeros(len(triangles), dtype=mesh.Mesh.dtype))
  for i, f in enumerate(triangles):
    for j in range(3):
      model.vectors[i][j] = points[f[j]]

  return model


def showstl(x, y, z):
  print("displaying pointcloud")
  '''
  ======================
  3D surface (color map)
  ======================

  Demonstrates plotting a 3D surface colored with the coolwarm color map.
  The surface is made opaque by using antialiased=False.

  Also demonstrates using the LinearLocator and custom formatting for the
  z axis tick labels.
  '''

  from mpl_toolkits.mplot3d import Axes3D
  import matplotlib.pyplot as plt
  from matplotlib import cm
  from matplotlib.ticker import LinearLocator, FormatStrFormatter
  import numpy as np

  fig = plt.figure()
  ax = fig.add_subplot(projection='3d')

  # Plot the surface.
  surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                         linewidth=0, antialiased=False)

  # plt.axis('equal')
