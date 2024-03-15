import numpy as np
import cv2

sorce = cv2.VideoCapture('facevideo.mp4')


while(True):
    ret, img = sorce.read()
    cv2.rectangle(img,(20,20),(100,100),(0,255,0),1)
    print(ret)
    if(ret == False):
        break

    cv2.imshow('IMG',img)
    key = cv2.waitKeyEx(1)

    if(key==27):
        break

cv2.destroyAllWindows()

#cv2.waitKey() is a keyboard binding function. Its argument is the time in milliseconds.
#The function waits for specified milliseconds for any keyboard event. If you press any key in that time, the program continues.
# If 0 is passed, it waits indefinitely for a key stroke. It can also be set to detect specific key strokes like, if key a is pressed etc which we will discuss below.
