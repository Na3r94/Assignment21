import cv2

img = cv2.imread('funny_lion.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

rows, cols = img.shape
print(img.shape)

for i in range(50):
    for j in range(150):
        if (i-j+100) >0 :
            img[j,100-j+i] = 0

cv2.imshow('Result', img)
cv2.waitKey()