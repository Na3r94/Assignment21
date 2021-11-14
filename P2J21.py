import cv2

img = cv2.imread('1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

img = 255 - img

cv2.imshow('Result', img)
cv2.waitKey()