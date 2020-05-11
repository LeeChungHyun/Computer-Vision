import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def eqHist():
    img = cv.imread('lena512.tif')
    gray = cv.imread('lena512.tif', cv.IMREAD_GRAYSCALE)

    scaled = cv.addWeighted(gray, 0.6, 0, 0, +50)
    hist_item = cv.calcHist([scaled], [0], None, [256], [0, 256])
  
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    # cdf의 값이 0인 경우는 mask처리를 하여 계산에서 제외
    # mask처리가 되면 Numpy 계산에서 제외가 됨
    # 아래는 cdf array에서 값이 0인 부분을 mask처리함
    cdf = hist.cumsum()
    cdf_m = np.ma.masked_equal(cdf, 0)
    #History Equalization 공식
    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    # Mask처리를 했던 부분을 다시 0으로 변환
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    equ = cdf[scaled]
    hist_item2 = cv.calcHist([equ], [0], None, [256], [0, 256])

    color = ('b', 'g', 'r')
    for col in enumerate(color):
        plt.plot(hist_item, color='r')
        plt.plot(hist_item2, color='g')
        plt.xlim([0, 256])
    plt.show()

    cv.imshow("Origin", img)
    cv.imshow("Gray2", scaled)
    cv.imshow("Equalized2", equ)

    cv.waitKey(0)
    cv.destroyAllWindows()

eqHist()
