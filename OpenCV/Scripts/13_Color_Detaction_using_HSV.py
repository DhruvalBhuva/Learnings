import cv2
import numpy as np

frame = cv2.imread('./Images/smarties.png')

while True:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerHue = np.array([110, 50, 50])
    upperHue = np.array([130, 255, 255])

    # Masking the image to get only the required color
    mask = cv2.inRange(hsv, lowerHue, upperHue)

    # Bitwise AND operation to get the colored image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break


cv2.destroyAllWindows()
