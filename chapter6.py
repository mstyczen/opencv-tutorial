import cv2
import numpy as np

# joining images
img = cv2.imread('resources/lena.png')

# horizontal stack
hor = np.hstack((img,img))
cv2.imshow("h stack", hor)

# vertical stack
vert = np.vstack((img, img))
cv2.imshow("v stack", vert)

# if the images have different number of channels, the functions above will not work

cv2.waitKey(0)