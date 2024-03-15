import cv2

img = cv2.imread('gray_image.png',0)
cv2.imshow("Img",img)


ret,thresh=cv2.threshold(img,80,255,cv2.THRESH_BINARY)
print(ret)
cv2.imshow("After Threshold",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
