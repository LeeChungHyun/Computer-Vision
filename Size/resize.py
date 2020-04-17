import cv2

image = cv2.imread("astronaut.png", cv2.IMREAD_COLOR)

print("current image shape = {0}".format(image.shape))

resize_image = cv2.resize(image, dsize=(0, 0), fx=0.33, fy=0.33,
                            interpolation=cv2.INTER_AREA)

cv2.imwrite("astronaut_resize.png", resize_image)
cv2.imshow("image", image)
cv2.imshow("resize_image", resize_image)


cv2.waitKey(0)
cv2.destoryAllWindows()
