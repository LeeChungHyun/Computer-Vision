import cv2 as cv
import numpy as np

img = cv.imread('pattern.png', cv.IMREAD_GRAYSCALE)
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (15, 15))
print(kernel)

dilation = cv.dilate(img, kernel, anchor=(-1, -1), iterations=1)
erosion = cv.erode(img, kernel, anchor=(-1, -1), iterations = 1)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

result = np.hstack([img,erosion,dilation,closing,opening])
cv.imshow('Result', result)

cv.waitKey(0)
cv.destroyAllWindows()
