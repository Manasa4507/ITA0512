import cv2

img = cv2.imread("house.jpg")

blur = cv2.GaussianBlur(img, (9,9), 0)

cv2.imshow("Original", img)
cv2.imshow("Blur", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
