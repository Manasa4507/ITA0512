import cv2

# Read image
img = cv2.imread(r"C:\Users\mamid\Downloads\flowerrr.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply threshold
_, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours
cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

# Display result
cv2.imshow("Defect Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
