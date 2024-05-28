import cv2
import numpy as np

img = cv2.imread("lena.jpg ")


def chnageColor(x):
    print(x)


cv2.namedWindow("Image")  # create window for Image

# createTrackbar(<Trackbar name>,<window name>,<initial value>,<final count>,<onChange>)
cv2.createTrackbar("CP", "Image", 10, 50, chnageColor)

switch = '0: Color\n 1 : Gray'
cv2.createTrackbar(switch, "Image", 0, 1, chnageColor)

while 1:

    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # 27 is ascii for esc
        break

    s = cv2.getTrackbarPos(switch, "Image")

    if s == 0:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Image", img)

cv2.destroyAllWindows()
