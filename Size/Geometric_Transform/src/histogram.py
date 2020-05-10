import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('lena512.tif')
gray = cv.imread('lena512.tif', cv.IMREAD_GRAYSCALE)

# 밝기를 변형한 영상 생성
scaled = cv.addWeighted(gray, 0.6, 0, 0, +50)
# 평활화 수행
equ = cv.equalizeHist(scaled)
'''
calchist함수는 (이미지, 채널, 이미지 일부분에 대한 히스토그램(mask),
계산할 히스토 막대, 계산 범위 )으로 이루어진다. grayscale일 경우 채널=0이다.
'''
hist1 = cv.calcHist([scaled], [0], None, [256], [0, 256])
hist2 = cv.calcHist([equ], [0], None, [256], [0, 256])
#각 히스토그램을 그래프로 표현하고 출력하기
plt.plot(hist1, color = 'r')
plt.plot(hist2, color = 'g')
plt.show()

cv.imshow("Origin", img)
cv.imshow("Gray", scaled)
cv.imshow("Equalized", equ)

cv.waitKey(0)
cv.destroyAllWindows()
