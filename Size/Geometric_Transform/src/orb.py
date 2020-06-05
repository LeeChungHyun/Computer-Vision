import numpy as np
import cv2 as cv

img1 = cv.imread('test1.jpg', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('test2.jpg', cv.IMREAD_GRAYSCALE)

resize_image1 = cv.resize(img1, dsize=(0, 0), fx=0.6, fy=0.6,
                          interpolation=cv.INTER_AREA)

resize_image2 = cv.resize(img2, dsize=(0, 0), fx=0.6, fy=0.6,
                          interpolation=cv.INTER_AREA)
# Initiate ORB detector
orb = cv.ORB_create()

# find the keypoints with ORB
kp1, des1 = orb.detectAndCompute(resize_image1, None)
kp2, des2 = orb.detectAndCompute(resize_image2, None)

# create BFMatcher object
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
# Match descriptors.
matches = bf.match(des1, des2)
# Sort them in the order of their distance.
matches = sorted(matches, key=lambda x: x.distance)
# Draw first 30 matches.
img3 = cv.drawMatches(resize_image1, kp1, resize_image2, kp2,
                      matches[:30], None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

cv.imshow('Image', img3)
cv.waitKey(0)
cv.destroyAllWindows()
