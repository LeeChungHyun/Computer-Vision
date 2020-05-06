import cv2 as cv
import numpy as np

def color_rect():
 
	g = np.zeros((256,256,3), np.uint8)
 
	for i in range(256):
    		g[i,:,:] = (0, i, 255-i)
        g[i, 255, :] = (255-i,i,i)
        for j in range(256):
              g[i,j,:] = (1-j/256)*src[i,0,:] + j/256*g[i,255,:]

	return g

g = color_rect()
cv.imshow('Org', g)
cv.waitKey(0)
cv.destroyAllWindows()
