import cv2

img = cv2.imread(r"C:\Users\mamid\Downloads\flowerrr.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image", img)
cv2.imshow("Gray Image", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
