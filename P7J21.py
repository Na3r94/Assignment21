import cv2

img = cv2.imread('5.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

img = cv2.resize(img,(300,300))

rows, cols = img.shape
print(rows)
for i in range(rows):
    for j in range(cols):
        img[i, j]= 255
for i in range(40,200):
    for j in range(20,50):
        img[i,j] = 0

for i in range(40,200):
    for j in range(190,220):
        img[i, j] =0

for j in range(40):
    for i in range(40,200):
        img[i,i+j-20]= 0

cv2.imshow('Practice 7', img)
cv2.waitKey()