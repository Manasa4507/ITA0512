import cv2

img = cv2.imread("tree.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edge = cv2.Canny(gray,100,200)

cv2.imshow("Original", img)
cv2.imshow("Edges", edge)

cv2.waitKey(0)
cv2.destroyAllWindows()
