# Standard imports
import cv2 as cv
import numpy as np

# Read image
image1 = cv.imread("images/test5.png")
im = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)  # Use COLOR_BGR2GRAY instead of IMREAD_GRAYSCALE

cv.namedWindow('GRAYSCALE', cv.WINDOW_NORMAL)           

cv.imshow("GRAYSCALE", im)

cv.waitKey(0)
