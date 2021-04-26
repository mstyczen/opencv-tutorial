import numpy as np
import cv2
from utils import stackImages

path = 'resources/lambo.PNG'


def empty(_):
    pass


# use track bars for hue, sat and val
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
# 179 is max value for hue in OpenCV
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 19, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 110, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 240, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 153, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    img = cv2.imread(path)
    # convert to HSV space
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hue_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    hue_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    sat_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    sat_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    val_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    val_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    img_stack = stackImages(0.6, [[img, imgHSV], [mask, imgResult]])
    cv2.imshow("stack", img_stack)
    cv2.waitKey(1)
