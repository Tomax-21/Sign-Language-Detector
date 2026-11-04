import os
import cv2


DATA_DIR = "./data"
IMAGES_PER_LETTER = 100


def init_letter_dir(letter):
    if not os.path.exists(os.path.join(DATA_DIR, letter)):
        os.makedirs(os.path.join(DATA_DIR, letter))

def save_image(letter):
    init_letter_dir(letter=letter)
    


QUIT, STOP, SET_LETTER, NOTHING = "quit", "stop", "set_letter", "nothing"
def key_handler(key):
    if key == 27:
        return QUIT, None
    if key == 8:
        return STOP, None
    if ord("a") <= key <= ord("z"):
        letter = chr(key).upper()

        return SET_LETTER, letter
    return NOTHING, None


def draw_overlay(frame, last_key_pressed):
    display = frame.copy()  # on dessine sur une copie : les images sauvegardées restent propres
    
    cv2.putText(display, f"Key pressed (suppr to cancel) : {last_key_pressed if last_key_pressed!= "" else "None"} => images for key are saving", (10,30), cv2.FONT_HERSHEY_PLAIN, 1.2, (0,0,0),1, cv2.LINE_AA)

    return display

def collect_data(cap:cv2.VideoCapture):
    last_key_pressed = ""
    
    while True:
        ret, frame = cap.read()
        if not ret: 
            break
        
        cv2.imshow("frame", draw_overlay(frame, last_key_pressed))

        action, letter = key_handler(cv2.waitKey(30))
        if action == QUIT:
            break
        elif action == STOP:
            last_key_pressed = None
        elif action == SET_LETTER:
            last_key_pressed = letter

       
            
        #close with the cross
        if cv2.getWindowProperty("frame", cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()


def main():
    os.makedirs(DATA_DIR, exist_ok=True)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Can't open the webcam")

    try:
        collect_data(cap)
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()