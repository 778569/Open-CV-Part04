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
print flags

```
# Image Thresholding

* Here, the matter is straight forward. If pixel value is greater than a threshold value, it is assigned one value (may be white), else it is assigned another value (may be black).
* The function used is cv2.threshold.
* First argument is the source image, which should be a grayscale image.
* Second argument is the threshold value which is used to classify the pixel values.
* Third argument is the maxVal which represents the value to be given if pixel value is more than (sometimes less than) the threshold value.
* OpenCV provides different styles of thresholding and it is decided by the fourth parameter of the function.

Different types are:


```
cv2.THRESH_BINARY
cv2.THRESH_BINARY_INV
cv2.THRESH_TRUNCV
cv2.THRESH_TOZEROV
cv2.THRESH_TOZERO_INV

```
