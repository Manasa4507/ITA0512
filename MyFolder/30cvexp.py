import cv2

# Read image
img = cv2.imread(r"C:\Users\mamid\Downloads\flowerrr.jpg")

# Increase brightness
bright = cv2.convertScaleAbs(img, alpha=1, beta=50)

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("Bright Image", bright)

cv2.waitKey(0)
cv2.destroyAllWindows()
