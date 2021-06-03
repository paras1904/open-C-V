import cv2 as cv
import numpy as np
img = cv.imread('Chandler.jpg')

#translation
def trans(img,x,y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimensiion = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dimensiion)
translated = trans(img,100,100)
cv.imshow('translated',translated)

#rotation
def rotat(img,angle,rotPoint = None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotmat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimension = (width,height)
    return cv.warpAffine(img,rotmat,dimension)
rot = rotat(img,45)
cv.imshow('rotated',rot)

#resizing
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

# flip
flip = cv.flip(img,1)
cv.imshow('flip',flip)

#cropping
crop = img[200:400,400:500]
cv.imshow('crop',crop)
cv.waitKey(0)