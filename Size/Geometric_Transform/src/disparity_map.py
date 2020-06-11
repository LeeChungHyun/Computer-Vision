import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgL = cv.imread('test1.jpg', cv.IMREAD_GRAYSCALE)
imgR = cv.imread('test2.jpg', cv.IMREAD_GRAYSCALE)

stereo = cv.StereoSGBM_create(minDisparity=16, blockSize=15)
disparity = stereo.compute(imgL, imgR)

# Normalize the image for representation
min = disparity.min()
max = disparity.max()
disparity = np.uint8(6400 * (disparity - min) / (max - min))

cv.imshow('Result', np.vstack((imgL, imgR, disparity)))
cv.waitKey(0)
cv.destroyAllWindows()
