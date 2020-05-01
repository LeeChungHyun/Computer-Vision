import cv2 as cv
import numpy as np


def color_rect():

    # Color rectangle 생성
	#opencv 파이썬에서는 특이하게 RGB가 아닌 BGR로 배치된다.

	g = np.zeros((256, 256, 3), np.uint8)
	
	red = g[0,0,255]
	green = g[0,255,0]
	blue = g[255,0,0]
	#r = np.uint8([[[0,0,255]]])
	for i in range(256):
    		for j in range(256):
    				
		g[i, :, :] = (0, i, 255-i)
		g[i, :, :] = (i, 0, 255-i)
	return g

g = color_rect()
#dst = cv.add(g, 100)

cv.imshow('Org', g)

cv.waitKey(0)
cv.destroyAllWindows()
