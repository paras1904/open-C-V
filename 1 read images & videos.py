import cv2 as cv
img = cv.imread('Chandler.jpg')
print(img.shape)
cv.imshow('chandler',img)
cv.waitKey(0)

capture = cv.VideoCapture('Iron_Man.mp4')
while True:
    isTrue, frame = capture.read()

    cv.imshow('Iron_Man.mp4',frame)
    if cv.waitKey(20) & 0xff == ord('d'):
        break
capture.release()
cv.destroyAllWindows()