import os
import cv2


DATA_DIR = "./data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Cant open the webcam")


while True:
    ret, frame = cap.read()
    if not ret: 
        break
    
    cv2.imshow("frame", frame)

    key  = cv2.waitKey(30)
    if key ==27:
        break

cap.release()
cv2.destroyAllWindows()