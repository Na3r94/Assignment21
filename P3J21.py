import cv2

img = cv2.imread('3.jpg')
img_final = cv2.imread('3.jpg')

img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img_final = cv2.cvtColor(img_final, cv2.COLOR_RGB2GRAY)

rows,cols = img.shape

for i in range(rows):
    for j in range(cols):
        img_final[i, j] = img[rows - i-1, cols - j-1]


cv2.imshow('Result', img_final)
cv2.waitKey()