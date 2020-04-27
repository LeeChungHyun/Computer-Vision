import cv2 as cv

image = cv.imread("astronaut.png", cv.IMREAD_GRAYSCALE)
#이미지를 grayscale로 불러온다.
image_gray = cv.imread("astronaut.png", cv.IMREAD_GRAYSCALE)

#현재 이미지의 크기를 알기 위해 image.shape을 사용한다.
#grayscale이라서 채널의 수가 0개임을 알수 있다. 또한 사이즈는 (512,512)임을 알 수 있다.
print("current image shape = {0}".format(image_gray.shape))

#현재 이미지의 밝기가 100보다 작으면 100, 그 외에는 현재값으로 만든다.
#이미지의 크기가 (512, 512)이고 for문 안에 if문으로 해결했다.
for i in range(0, 512):
    for j in range(0, 512):
        if image_gray[i,j] < 100:
            image_gray[i, j] = 100
            continue
        image_gray[i,j]
        
#grayscale된 이미지를 imwrite 사용해서 저장한다.
cv.imwrite("Before brightness.png", image)

#grayscale된 이미지를 brightness처리를 한 다음 imwrite 사용해서 저장한다.
cv.imwrite("After brightness.png", image_gray)

cv.imshow("Before brightness", image)
cv.imshow("After brightness", image_gray)

cv.waitKey(0)

cv.destroyAllWindows()
