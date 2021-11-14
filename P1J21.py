import cv2
import numpy as np
height = 800
width = 800
img = np.zeros((height, width))

for i in range(20):
    for j in range(20):
        if j % 2 == 0:
            if i % 2 == 0:
                img[i*40:(i+1)*40, j*40:(j+1)*40] = 1
            else:
                img[i*40:(i+1)*40, j*40:(j+1)*40] = 0
        else:
             if i % 2 == 1:
                 img[i*40:(i+1)*40, j*40:(j+1)*40] = 1
             else:
                 img[i*40:(i+1)*40, j*40:(j+1)*40] = 0

cv2.imshow('Result', img)
cv2.waitKey()