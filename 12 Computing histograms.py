import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('Chandler.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# histogram for gray
gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])
plt.figure()
plt.title("HISTOGRAM")
plt.xlabel("BINS")
plt.ylabel('# of pixels ')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
# cv.waitKey(0)