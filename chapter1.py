import cv2

# img = cv2.imread("resources/lena.png")
# cv2.imshow("Output", img)
#
# cv2.waitKey(1000)

# cap = cv2.VideoCapture("resources/test_video.mp4")

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if not success or cv2.waitKey(1) & 0xFF == ord('q'):
        break

