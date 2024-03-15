import numpy as np
import cv2


Sorce = cv2.VideoCapture('facevideo.mp4');

ret, img = Sorce.read()
print(ret)
cv2.imshow('Img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
