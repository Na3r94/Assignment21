import cv2

img = cv2.imread('5.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

img = cv2.resize(img, (300, 255))

rows, cols = img.shape

for i in range(rows):
    for j in range(cols):
        img[i, j] = 255 - i

cv2.imshow('Practice 6', img)
cv2.waitKey()