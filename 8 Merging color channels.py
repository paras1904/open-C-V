import cv2 as cv
import numpy as np

img = cv.imread('Chandler.jpg')
cv.imshow('img',img)
b,g,r = cv.split(img)
cv.imshow('b',b)
cv.imshow('g',g)
cv.imshow('r',r)
print(img.shape,b.shape,g.shape,r.shape)
merg = cv.merge([b,g,r])
cv.imshow('merg',merg)

blank = np.zeros(img.shape[:2],dtype='uint8')
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)


cv.waitKey(0)