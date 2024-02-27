import numpy as np
import cv2
import glob
import sys
import os

nline = 8
ncol = 8 

img = cv2.imread(glob.glob('/home/rossm/chessBoard.jpg')[0])

cv2.findChessboardCorners(img, patternSize[, corners[, flags]]) → retval, corners

## termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

## processing
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Find the chessboard corners
ret, corners = cv2.findChessboardCorners(gray, (nline, ncol), None)
corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)