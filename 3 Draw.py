import cv2 as cv
import numpy as np

img = cv.imread('Chandler.jpg')
cv.imshow('chandler',img)

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)

# paint img certain colour
blank[:] = 255,0,0
cv.imshow('blue',blank)

blank[20:30,30:40] = 255,0,0
cv.imshow('sqr',blank)

# draw rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,255),thickness=2)
cv.imshow('rectangle',blank)

#draw circle
cv.circle(blank,(250,250),40,(0,0,255),thickness=2)
cv.imshow('circle',blank)

#draw line
cv.line(blank,(0,0),(250,250),(255,255,255),thickness=3)
cv.imshow('line',blank)

#write Text
cv.putText(blank,"HELLO",(255,255),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
cv.imshow('text',blank)
cv.waitKey(0)
