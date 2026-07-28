import cv2

img = cv2.imread("image.jpg")

big = cv2.resize(img, (600, 600))
small = cv2.resize(img, (200, 200))

cv2.imshow("Original", img)
cv2.imshow("Big", big)
cv2.imshow("Small", small)

cv2.waitKey(0)
cv2.destroyAllWindows()
