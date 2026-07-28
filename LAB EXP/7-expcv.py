import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(100)   # Slow motion

    if key == ord('f'):
        cv2.waitKey(10)      # Fast motion

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
