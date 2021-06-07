import cv2 as cv
import os
import numpy
import numpy as np

people = ['chandler','monica']
DIR = r"/home/paras/PycharmProjects/pythonprojects/A.I/Open CV/face_recog/"
haar_cascade = cv.CascadeClassifier('Haar_detect.xml')
# for i in os.listdir(DIR):
#     print(i,end=',')

features = []
labels = []


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            if img_array is None:
                continue

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y + h, x:x + w]
                features.append(faces_roi)
                labels.append(label)


create_train()
features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
# Train the Recognizer on the features list and the labels list
face_recognizer.train(features, labels)

# haar_cascade = face_recognizer()
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')
img = cv.imread('Chandler.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 20)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)
cv.waitKey(0)
