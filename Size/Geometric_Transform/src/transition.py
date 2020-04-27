import cv2 as cv
import numpy as np

#이미지를 grayscale로 불러온다.
image = cv.imread("astronaut.png", cv.IMREAD_GRAYSCALE)

#현재 이미지의 크기를 알기 위해 image.shape을 사용한다.
#grayscale이라서 채널의 수가 0개임을 알수 있다.
print("current image shape = {0}".format(image.shape))

#변환행렬 M은 2*3행렬이므로 행과 열이(t_x,t_y) 3행에 위치하도록 설정한다.
rows, cols = image.shape[:2]

#M은 변환행렬이다. [1,0,x축이동], [0,1,y축이동] 형태의 float32타입이다.
M = np.float32([[1,0,100],[0,1,100]])
#warpAffine함수를 사용하여 이미지의 위치를 변경시킨다.
dst = cv.warpAffine(image, M, (cols, rows))

#변환된 이미지를 imwrite 사용해서 저장한다.
cv.imwrite("astronaut_original.png", image)
#warpAffine된 이미지를 imwrite 사용해서 저장한다.
cv.imwrite("astronaut_result.png", dst)

#원본 이미지를 콘솔창으로 보여준다.
cv.imshow("original", image)
cv.imshow("Result", dst)

#입력이 따로 있을때까지 무한대기한다.
cv.waitKey(0)

#화면에 나타난 윈도우를 종료한다.
cv.destoryAllWindows()
