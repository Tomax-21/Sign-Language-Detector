import os
import cv2


DATA_DIR = "./data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Cant open the webcam")


last_key_pressed = ""

while True:
    ret, frame = cap.read()
    cv2.putText(frame, f"Key pressed (suppr to cancel) : {last_key_pressed if last_key_pressed!= "" else "None"} => images for key are saving", (10,30), cv2.FONT_HERSHEY_PLAIN, 1.2, (0,0,0),1, cv2.LINE_AA)
    if not ret: 
        break
    
    cv2.imshow("frame", frame)

    key  = cv2.waitKey(30)
    if key ==27:
        break
    elif key != -1:
        if key == 8: #delete
            last_key_pressed = ""

        #a = 97, z = 122
        if key >= 97 and key <= 122:
            last_key_pressed = chr(key)


    #close with the cross
    if cv2.getWindowProperty("frame", cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()