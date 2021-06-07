import numpy as np
import cv2 as cv
people = ['chandler','monica']

haar_cascade = cv.CascadeClassifier('Haar_detect.xml')
face_reogniser =  cv.face.LBPHFaceRecognizer_create()
face_reogniser.read('face_trained.yml')

img = cv.imread('chandlerl2.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

faces_rect = haar_cascade.detectMultiScale(gray,1.1,4)
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+h]
    label,confidence = face_reogniser.predict(faces_roi)
    print(f"label = {people[label]} with a confidence of  {confidence}")
    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=3)
cv.imshow('detect',img)
cv.waitKey(0)