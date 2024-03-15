import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('threshold.jpg')
cv2.imshow('Original',img)
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('gray',gray)

ret, thresh =cv2.threshold(gray,60,225,cv2.THRESH_BINARY)
cv2.imshow('Thresh-60',thresh)


ret,thresh=cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
cv2.imshow('Thresh-100',thresh)


cv2.waitKey(0)
cv2.destroyAllWindows()
