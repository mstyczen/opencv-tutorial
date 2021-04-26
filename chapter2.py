import cv2
import numpy as np

img = cv2.imread("resources/lena.png")

# standard convention for OpenCV is BGR, rather than RGB
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# second parameter is kernel size, third is sigma_X
blur_img = cv2.GaussianBlur(img_gray, (7, 7), 0)

# edge detector, the parameters are threshold values
img_canny = cv2.Canny(img, 150, 200)

# dilation - making edges thicker
kernel = np.ones((5, 5), np.uint8)
# more iterations = more thickness
img_dilation = cv2.dilate(img_canny, kernel, iterations=1)

# erosion - opposite of erosion
img_erosion = cv2.erode(img_dilation, kernel, iterations=1)

cv2.imshow("Gray image", img_gray)
cv2.imshow("Blurred image", blur_img)
cv2.imshow("Canny image", img_canny)
cv2.imshow("Dilated image", img_dilation)
cv2.imshow("Eroded image", img_erosion)
cv2.waitKey(0)

