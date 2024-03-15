import numpy as np
import cv2

img = cv2.imread("flower.jpg")

cv2.rectangle(img,(50,50),(200,200),(0,225,225),2)

# print(img[100,100])
# img[100:200,100:105] = [255,255,255]

# print(img.shape)
# cv2.imshow('Live',img)
cv2.imshow('IMG',img)

cv2.imwrite('Flower02')
cv2.waitKey(10000)
cv2.destroyAllWindows()
