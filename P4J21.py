import  cv2

img = cv2.imread('4.JPG')
img= cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

rows, cols = img.shape
print(img.shape)

# cv2.rectangle(img, (710, 340), (1050,850), (0,255,0), 5)
for i in range(rows):
    for j in range(cols):
        if 350 < i < 850 and 710 < j < 1050:
            img[i, j] = img[i, j]
        else:
            if img[i, j] < 150:
                img[i, j] = 0

cv2.imshow('Result', img)
cv2.waitKey()