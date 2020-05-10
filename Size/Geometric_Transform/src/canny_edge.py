import numpy as np
import cv2 as cv

img = cv.imread('me.jpg')
#현재 이미지의 크기를 알기 위해 image.shape을 사용한다.
print("current image shape = {0}".format(img.shape))

cv.imshow("Original", img)
gray = cv.imread('me.jpg', cv.IMREAD_GRAYSCALE)
#가우시안 blur(이미지, 커널크기)
blur1 = cv.GaussianBlur(gray, (1, 1), 0)
blur3 = cv.GaussianBlur(gray, (3, 3), 0)
blur5 = cv.GaussianBlur(gray, (5, 5), 0)
blur7 = cv.GaussianBlur(gray, (7, 7), 0)

edges1 = cv.Canny(blur1, 50, 100)
edges3 = cv.Canny(blur3, 50, 100)
edges5 = cv.Canny(blur5, 50, 100)
edges7 = cv.Canny(blur7, 50, 100)

cv.imshow("Edge1", edges1)
cv.imshow("Edge3", edges3)
cv.imshow("Edge5", edges5)
cv.imshow("Edge7", edges7)

cv.waitKey(0)
cv.destroyAllWindows()
