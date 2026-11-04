import os
import cv2
import time

import utils



def init_letter_dir(letter):
    path = os.path.join(utils.DATA_DIR, letter)
    os.makedirs(path, exist_ok=True)
    return path

def next_index(letter):
    path = init_letter_dir(letter)
    indexes = []
    for filename in os.listdir(path):
        name, extension = os.path.splitext(filename)
        if extension == ".jpg" and name.isdigit():
            indexes.append(int(name))

    return max(indexes) + 1 if indexes else 0



def count_images(letter):
    path = os.path.join(utils.DATA_DIR, letter)
    if not os.path.isdir(path):
        return 0
    return len([f for f in os.listdir(path) if f.endswith(".jpg")])



def save_image(letter, frame):
    path = init_letter_dir(letter)
    index = next_index(letter)
    cv2.imwrite(os.path.join(path, f"{index}.jpg"), frame)

    


def key_handler(key):
    if key == 27:
        return utils.QUIT, None
    if key == 8:
        return utils.STOP, None
    if ord("a") <= key <= ord("z"):
        letter = chr(key).upper()

        return utils.SET_LETTER, letter
    return utils.NOTHING, None


def draw_overlay(frame, last_key_pressed):
    display = frame.copy()  # on dessine sur une copie : les images sauvegardées restent propres

    key = "" if not last_key_pressed else last_key_pressed
    
    cv2.putText(display, f"Key pressed (suppr to cancel) : {key if key!= "" else "None"} => ({count_images(key)}/{IMAGES_PER_LETTER})", (10,30), cv2.FONT_HERSHEY_PLAIN, 1.2, (0,0,0),1, cv2.LINE_AA)

    return display

def collect_data(cap:cv2.VideoCapture):
    last_key_pressed = None
    last_save_time = 0

    
    while True:
        ret, frame = cap.read()
        if not ret: 
            break

        if last_key_pressed:
            if count_images(last_key_pressed) >= utils.IMAGES_PER_LETTER:
                print(f"Lettre {last_key_pressed} terminée ({utils.IMAGES_PER_LETTER} images)")
                last_key_pressed = None

            elif time.time() - last_save_time >= utils.SAVE_INTERVAL:
                save_image(last_key_pressed, frame)
                last_save_time = time.time()


                
        
        cv2.imshow("frame", draw_overlay(frame, last_key_pressed))

        action, letter = key_handler(cv2.waitKey(30))
        if action == utils.QUIT:
            break
        elif action == utils.STOP:
            last_key_pressed = None
        elif action == utils.SET_LETTER:
            last_key_pressed = letter

       
            
        #close with the cross
        if cv2.getWindowProperty("frame", cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()


def main():
    os.makedirs(utils.DATA_DIR, exist_ok=True)

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