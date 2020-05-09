import numpy as np
import cv2 as cv

img = cv.imread("me.jpg", cv.IMREAD_GRAYSCALE)
gray = cv.imread(img, cv.IMREAD_GRAYSCALE)

edges = cv.Canny(gray, 50, 100, 3)

cv.imshow("Edge", edges)
cv.waitKey(0)
cv.destroyAllWindows()
