import cv2 as cv

img = cv.imread('Chandler.jpg')
cv.imread(',chandler',img)

def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA )
capture = cv.VideoCapture('Iron_Man.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Iron_man.mp4',frame)

    frame_resized = rescaleFrame(frame,scale=.2)
    cv.imshow('Iron_man_small',frame_resized)
    if cv.waitKey(20) & 0xff == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
