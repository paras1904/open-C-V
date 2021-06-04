import cv2 as cv
img = cv.imread('Chandler.jpg')
cv.imshow('normal',img)
#averaging blur method
avg = cv.blur(img,(7,7))
cv.imshow('average',avg)

#gaussion blur
gaus_blur = cv.GaussianBlur(img,(7,7),0)
cv.imshow('gaussion blur',gaus_blur)

# median blur
median = cv.medianBlur(img,11)
cv.imshow('median',median)


#bilateral bluring
bilateral = cv.bilateralFilter(img,40,35,45)
cv.imshow('bilateral',bilateral)
cv.waitKey(0)