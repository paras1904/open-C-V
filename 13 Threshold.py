import cv2 as cv

img = cv.imread('Chandler.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# simple thresholding
threshold, thresh = cv.threshold(gray,100,255,cv.THRESH_BINARY)
cv.imshow('threshold',thresh)
threshold, thresh_inv = cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)
cv.imshow('inverse threshold',thresh_inv)

#adaptive threshold
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('adaptive',adaptive_thresh)

cv.waitKey(0)