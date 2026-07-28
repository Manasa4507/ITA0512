import cv2
import numpy as np

img = cv2.imread("image.jpg")

rows, cols = img.shape[:2]

M = np.float32([[1, 0, 100],
                [0, 1, 50]])

move = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("Original", img)
cv2.imshow("Moved", move)

cv2.waitKey(0)
cv2.destroyAllWindows()
