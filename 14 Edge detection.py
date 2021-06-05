import cv2 as cv
import numpy as np

img = cv.imread('Chandler.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# laplacian
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('lap',lap)

#sobel
soblex = cv.Sobel(gray,cv.CV_64F,1,0)
sobley = cv.Sobel(gray,cv.CV_64F,0,1)
cobined = cv.bitwise_or(sobley,soblex)
cv.imshow('x & y',cobined)
cv.waitKey(0)