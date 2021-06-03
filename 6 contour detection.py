import cv2 as cv
import numpy as np

img = cv.imread('Chandler.jpg')
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#first way
blur = cv.GaussianBlur(grey,(7,7),cv.BORDER_DEFAULT)
canny = cv.Canny(blur,125,175)
contours, hiearchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))


#second way threshold value
ret,threshold = cv.threshold(grey,125,175,cv.THRESH_BINARY)
contours2, hiearchies2 = cv.findContours(threshold,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours2))


# draw ontours on image
blank = np.zeros(img.shape,dtype='uint8')
cv.drawContours(blank,contours2,-1,(0,0,255),1)
cv.imshow('blank comntours drwan',blank)
cv.waitKey(0)