import numpy as np
import cv2

img = cv2.imread('flower.jpg')
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)

cv2.imshow("IMG1",img)
cv2.imshow('IMG2',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
