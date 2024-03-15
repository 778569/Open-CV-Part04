# Open-CV-Part04
GitHub repository containing various image processing algorithms implemented using OpenCV library, facilitating tasks like object detection, image enhancement, and more. Explore, contribute, and utilize powerful computer vision techniques.

# How computer read image

![image](https://github.com/778569/Open-CV-Part04/assets/52319671/a90aa0e1-ffd3-4c9e-97c0-af686b68ddf0)

# Point Operations (Pixelwise Operations)

## Color Conversion

There are more than 150 color-space conversion methods available in OpenCV. But we will look into only two which are most widely used ones, BGR \leftrightarrow Gray and BGR \leftrightarrow HSV.

For color conversion, we use the function cv2.cvtColor(input_image, flag) where flag determines the type of conversion.

For BGR \rightarrow Gray conversion we use the flags cv2.COLOR_BGR2GRAY. Similarly for BGR \rightarrow HSV, we use the flag cv2.COLOR_BGR2HSV. To get other flags, just run following commands in your Python terminal :

```
import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print flags ```
