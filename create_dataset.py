import cv2
import os
import mediapipe as mp
import matplotlib.pyplot as plt

import utils


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)



for dir in os.listdir(utils.DATA_DIR):
    for img_path in os.listdir(os.path.join(utils.DATA_DIR, dir)):

        image = cv2.imread(os.path.join(utils.DATA_DIR, dir, img_path))
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    img_rgb,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )
                
        plt.figure()
        plt.imshow(img_rgb)

plt.show()
