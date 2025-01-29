import cv2

import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()

    if not success:
        break

    cv2.imshow("webcam", cv2.flip(image, 1))

    if cv2.waitKey(100) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows
