import cv2
import numpy as np


def nothing(x):
    pass


cap = cv2.VideoCapture(0);

cv2.namedWindow("Tracking")
cv2.createTrackbar("LowerHue", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LowerSaturation", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LowerValue", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UpperHue", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UpperSaturation", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UpperValue", "Tracking", 255, 255, nothing)

while True:
    # frame = cv2.imread('smarties.png')
    rat, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerHue = cv2.getTrackbarPos("LowerHue", "Tracking")
    lowerSaturation = cv2.getTrackbarPos("LowerSaturation", "Tracking")
    lowerValue = cv2.getTrackbarPos("LowerValue", "Tracking")

    upperHue = cv2.getTrackbarPos("UpperHue", "Tracking")
    upperSaturation = cv2.getTrackbarPos("UpperSaturation", "Tracking")
    upperValue = cv2.getTrackbarPos("UpperValue", "Tracking")

    lowerColor = np.array([lowerHue, lowerSaturation, lowerValue])
    upperColor = np.array([upperHue, upperSaturation, upperValue])

    mask = cv2.inRange(hsv, lowerColor, upperColor)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
