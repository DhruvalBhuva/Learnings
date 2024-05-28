import cv2
import numpy as np

def chnageColor(x):
    print(x)


blackImg = np.zeros((250, 500, 3), np.uint8)
cv2.namedWindow("Image")  # create window for Image

# createTrackbar(<Trackbar name>,<window name>,<initial value>,<final count>,<onChange>)
cv2.createTrackbar("R", "Image", 0, 255, chnageColor)
cv2.createTrackbar("B", "Image", 0, 255, chnageColor)
cv2.createTrackbar("G", "Image", 0, 255, chnageColor)

switch = '0: OFF\n 1 : ON'
cv2.createTrackbar(switch, "Image", 0, 1, chnageColor)

while 1:
    cv2.imshow("Image", blackImg)  # load Image in above created "Image" window
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # 27 is ascii for esc
        break

    b = cv2.getTrackbarPos("B", "Image")  # (<TrackbarName>,<Image window name>)
    g = cv2.getTrackbarPos("G", "Image")
    r = cv2.getTrackbarPos("R", "Image")
    s = cv2.getTrackbarPos(switch, "Image")

    if s == 0:
        blackImg[:] = 0
    else:
        blackImg[:] = [b, g, r]

cv2.destroyAllWindows()
