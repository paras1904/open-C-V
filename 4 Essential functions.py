import cv2 as cv
img = cv.imread('Chandler.jpg')

# convert to gray
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
cv.waitKey(0)

#blur
blur = cv.GaussianBlur(img,(11,11),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

# Edge cascade
canny = cv.Canny(img,125,175)
cv.imshow('edge',canny)

# Dialating image
canny = cv.Canny(img,125,175)
dilated = cv.dilate(canny,(7,7),iterations=5)
cv.imshow('dilated',dilated)

# Eroding = dilated + edge
canny = cv.Canny(img,125,175)
dilated = cv.dilate(canny,(7,7),iterations=5)
erode = cv.erode(dilated,(3,3),iterations=2)
cv.imshow('erode',erode)

# Resize
resizes = cv.resize(img,(400,400),interpolation=cv.INTER_AREA)
cv.imshow('resize',resizes)

#cropd
crop = img[50:200,200:400]
cv.imshow('crop',crop)
cv.waitKey(0)





