import cv2 as cv
import numpy as np

img = cv.imread('0907.png')
kernel = cv.getStructuringElement(cv.MORPH_CROSS, (3, 3))
print(kernel)

dilation = cv.dilate(img, kernel, anchor=(-1, -1), iterations=1)

result = np.hstack([img,dilation])
cv.imshow('Result', result)
cv.waitKey(0)
cv.destroyAllWindows()