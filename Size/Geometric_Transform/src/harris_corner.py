import cv2 as cv
import numpy as np

filename = 'camera.png'
img = cv.imread(filename)

gray = cv.imread('camera.png', cv.IMREAD_GRAYSCALE)
gray = np.float32(gray)
dst = cv.cornerHarris(gray, 2, 3, 0.04)
# Threshold for an optimal value, it may vary depending on the image.
img[dst > 0.01*dst.max()]=[0,255,0]
cv.imshow('dst', img)

cv.waitKey(0)
cv.destroyAllWindows()
