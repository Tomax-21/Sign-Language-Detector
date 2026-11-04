import os
import cv2


DATA_DIR = "./data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Cant open the webcam")





def key_handler(key):
    if key ==27:
        return
    
    elif key == 8: #delete
        return ""
    
    if key >= 97 and key <= 122:  #a = 97, z = 122
        return chr(key)


def collect_data():
    last_key_pressed = ""

    while True:
        ret, frame = cap.read()
        if not ret: 
            break
        
        cv2.putText(frame, f"Key pressed (suppr to cancel) : {last_key_pressed if last_key_pressed!= "" else "None"} => images for key are saving", (10,30), cv2.FONT_HERSHEY_PLAIN, 1.2, (0,0,0),1, cv2.LINE_AA)
        cv2.imshow("frame", frame)

        key  = cv2.waitKey(30)
        if not key_handler(key):
            break
       
            
        #close with the cross
        if cv2.getWindowProperty("frame", cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()


collect_data()