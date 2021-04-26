import cv2
import numpy as np

# openCV convention on coordinates
# y grows down
# x grows to the right
# (0,0) is in the top left corner
# (w,h) is the bottom right corner

img = cv2.imread("Resources/lambo.PNG")

# get the shape of the image
print(img.shape)

# resize
img_resize = cv2.resize(img, (300, 200))

# crop - height is the first coordinate, then width
img_cropped = img[0:200, 200:500]

cv2.imshow("Image", img_cropped)
cv2.waitKey(0)