import cv2 as cv
img = cv.imread('Chandler.jpg')

#bgr to hsv
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)
cv.waitKey(0)

#bgr to labsudo apt-get install --reinstall libxcb-xinerama0
lab = cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow('lab',lab)
cv.waitKey(0)

#open cv know how to read BGR img but other library like matplotlib don't
import matplotlib.pyplot as plt
plt.imshow(img)
plt.show()

# bgr to rgb
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)
cv.waitKey(0)

#mix match
hsv1 = cv.cvtColor(img,cv.COLOR_BGR2HSV)
hsv2 = cv.cvtColor(hsv1,cv.COLOR_HSV2BGR)
cv.imshow('hsv to bgr',hsv2)
cv.waitKey(0)