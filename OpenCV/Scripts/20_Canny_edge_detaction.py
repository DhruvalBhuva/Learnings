'''
Canny edge detection is a multi-step algorithm that can detect edges with noise supression.
It is composed of 5 steps:
    1. Noise Reduction: To smooth the image
    2. Gradient Detection: To find edges
    3. Non-maximum Suppression: To get rid of spurious response to edge detection
    4. Double Threshold: To determine potential edges
    5. Edge Tracking by Hysteresis: To finalize the detection of edges by suppressing all the other edges that are weak and not connected to strong edges
Canny Edge Detection: cv.Canny(<ImgObj>,<Thresold1>,<Thresold2>,<ApertureSize>,<L2gradient>)
'''

import cv2 as cv
import numpy as np

img = cv.imread("./Images/sudoku.png", cv.IMREAD_GRAYSCALE)
img = cv.resize(img, (500, 500))


def nothing(x):
    pass


cv.namedWindow("Canny Edge Detection", cv.WINDOW_NORMAL)
cv.createTrackbar("Thresold1", "Canny Edge Detection", 0, 255, nothing)
cv.createTrackbar("Thresold2", "Canny Edge Detection", 0, 255, nothing)

while True:
    th1 = cv.getTrackbarPos("Thresold1", "Canny Edge Detection")
    th2 = cv.getTrackbarPos("Thresold2", "Canny Edge Detection")

    canny = cv.Canny(img, th1, th2)

    cv.imshow("Canny Edge Detection", canny)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cv.waitKey(0)
cv.destroyAllWindows()
