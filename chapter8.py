import cv2
import numpy as np
from utils import stackImages


# colour + shape detection
def getContours(img, img_out):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        cv2.drawContours(img_out, cnt, -1, (255, 0, 0), 3)

        arc_length = cv2.arcLength(cnt, True)
        approx_poly = cv2.approxPolyDP(cnt, 0.02 * arc_length, True)
        obj_cor = len(approx_poly)
        x, y, w, h = cv2.boundingRect(approx_poly)

        if obj_cor == 3:
            obj_type = "Tri"
        elif obj_cor == 4:
            asp_ratio = w/float(h)
            if 0.95 < asp_ratio < 1.05:
                obj_type = "Sqr"
            else:
                obj_type = "Rec"
        else:
            obj_type = "Cir"

        cv2.rectangle(img_out, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img_out, obj_type, (x + w // 2 - 10, y + h // 2), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 0), 2)


path = 'resources/shapes.png'
img = cv2.imread(path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 1)
img_canny = cv2.Canny(img_blur, 50, 50)
img_blank = np.zeros_like(img)

img_contours = img.copy()
getContours(img_canny, img_contours)

img_stack = stackImages(0.75, [[img, img_gray, img_blur], [img_canny, img_contours, img_blank]])

cv2.imshow("Stacked", img_stack)
cv2.waitKey(0)
