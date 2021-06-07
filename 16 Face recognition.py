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
            img_path = os.path.join(path,img)
            img_Array = cv.imread(img_path)
            gray = cv.cvtColor(img_Array,cv.COLOR_BGR2GRAY)
            face_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
            for (x,y,w,h) in face_rect:
                faces_roi = gray[y:y+h,x:x+h]
                features.append(faces_roi)
                labels.append(label)
create_train()
# print(len(features),len(labels))

faces_recog = cv.face.LBPHFaceRecognizer_create()

#train
features = np.array(features,dtype='object')
labels = np.array(labels)
faces_recog.train(features,labels)
faces_recog.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)
