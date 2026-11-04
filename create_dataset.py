import cv2
import os
import mediapipe as mp
import matplotlib.pyplot as plt

import utils




for dir in os.listdir(utils.DATA_DIR):
    for img_path in os.listdir(os.path.join(utils.DATA_DIR, dir)):

        image = cv2.imread(os.path.join(utils.DATA_DIR, dir, img_path))
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        plt.figure()
        plt.imshow(img_rgb)

plt.show()
