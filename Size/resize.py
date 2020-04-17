import cv2

#이미지를 불러온다.
image = cv2.imread("astronaut.png", cv2.IMREAD_COLOR)

#현재 이미지의 크기를 알기 위해 image.shape을 사용한다.
print("current image shape = {0}".format(image.shape))

#원본에서 1/3으로 줄인 이미지를 resize해야 한다.
#resize의 형식은 cv2.resize(원본 이미지, 결과 이미지의 크기, 가로비, 세로비, interpolation속성)
#결과 이미지의 크기는 따로 지정하지 않으면 (0,0)으로 입력한다.
#interpolation 속성중에 이미지를 확대시 INTER_LINEAR 기법을 사용한다. 반면 축소시 INTER_AREA기법을 사용한다.
resize_image = cv2.resize(image, dsize=(0, 0), fx=0.33, fy=0.33,
                            interpolation=cv2.INTER_AREA)

#변환된 이미지를 imwrite 사용해서 저장한다.
cv2.imwrite("astronaut_resize.png", resize_image)
#원본 이미지를 콘솔창으로 보여준다.
cv2.imshow("image", image)
#변형된 이미지를 콘솔창으로 보여준다.
cv2.imshow("resize_image", resize_image)

#입력이 따로 있을때까지 무한대기한다.
cv2.waitKey(0)
#화면에 나타난 윈도우를 종료한다.
cv2.destoryAllWindows()
