import cv2
import os
import mediapipe as mp
import matplotlib.pyplot as plt
import pickle
import utils


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)


data = []
labels = [] # categories of each images


for letter in os.listdir(utils.DATA_DIR):
    for img_path in os.listdir(os.path.join(letter)):

        data_img = []

        image = cv2.imread(os.path.join(utils.DATA_DIR, dir, img_path))
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # pour chaque image, on extrait tous les landmarks

                #mp_drawing.draw_landmarks(img_rgb,hand_landmarks,mp_hands.HAND_CONNECTIONS,mp_drawing_styles.get_default_hand_landmarks_style(),mp_drawing_styles.get_default_hand_connections_style())
                for i in range(len(hand_landmarks.landmark)):
                    #hand_landmarks.landmark[i] = position of the landmark
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    data_img.append(x)
                    data_img.append(y)

            data.append(data_img)
            labels.append(letter)

f = open("data.pickle", "wb")
pickle.dump({"data": data, "label":labels}, f)
f.close()

