import cv2 as cv
img = cv.imread('Chandler.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
haar_cascade = cv.CascadeClassifier('Haar_detect.xml')
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=20)
print(len(faces_rect))
for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('detected face',img)
cv.waitKey(0)