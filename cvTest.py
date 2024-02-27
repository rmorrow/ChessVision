import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

from IPython.display import Image

#%matplotlib inline

#image = cv2.imread("/home/rossm/checkerboard_18x18.png", 0)
image = cv2.imread("/home/rossm/chessComputerGame.jpg", 0)
#image = cv2.imread("/home/rossm/chessBoardZoom.jpg", cv2.IMREAD_ANYDEPTH)
#image = image.view(np.int32)
#cv2.imshow('Preview', image)
#plt.imshow(image)
#plt.show()
#cv2.waitKey(0)
print(image)

cb_img_copy = image.copy()

#for y in range(50,55):
	#for x in range(700, 818):
	#	cb_img_copy[x,y] = 200
		
		
#cv2.circle(cb_img_copy, (600, 200), 100, (0,0,255), thickness=5, lineType=cv2.LINE_AA)




#plt.imshow(cb_img_copy)
#plt.show()

#retval, image_thresh = cv2.threshold(image,150,255 ,cv2.THRESH_BINARY)
GRID = (7, 7)

#plt.figure(figsize=[18,5])
#plt.imshow(image_thresh)

found, corners = cv2.findChessboardCorners(
    image, GRID, cv2.CALIB_CB_ADAPTIVE_THRESH)

cv2.drawChessboardCorners(image, GRID, corners, found)
cv2.imshow('Chess Board Vision', image)
cv2.waitKey(0)

print("Image type is ", image.dtype)
print("Shape is" , image.shape)
print(image.max())


