import cv2 as cv
import numpy as np

img = cv.imread('0914.png')
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
print(kernel)

erosion = cv.erode(img, kernel, anchor=(-1, -1), iterations=1)

difference = img-erosion

result = np.hstack([img,difference])
cv.imshow('Result', result)
cv.waitKey(0)
cv.destroyAllWindows()