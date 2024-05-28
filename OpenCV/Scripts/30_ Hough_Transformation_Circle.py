'''
Hough Transformation Circle Detection
1) cv.HoughCircles(<image>, <method>, <dp>, <minDist>, <param1>, <param2>[param1 > params2], <minRadius>, <maxRadius>)
    - method: Detection method. Currently, the only implemented method is cv.HOUGH_GRADIENT.
    - dp: Inverse ratio of the accumulator resolution to the image resolution.
    - minDist: Minimum distance between the centers of the detected circles.
    - param1: First method-specific parameter. In case of cv.HOUGH_GRADIENT, it is the higher threshold of the two passed to the Canny edge detector (the lower one is twice smaller).
    - param2: Second method-specific parameter. In case of cv.HOUGH_GRADIENT, it is the accumulator threshold for the circle centers at the detection stage.
    - minRadius: Minimum circle radius.
    - maxRadius: Maximum circle radius.
    - It returns an array where each row is a vector that contains the parameters (x, y, r) of the detected circle.


2) cv.circle(<image>, <center>, <radius>, <color>, <thickness>)
    - center: Center of the circle.
    - radius: Radius of the circle.
    - color: Color of the circle.
    - thickness: Thickness of the circle outline, if negative, the circle will be filled.
'''

import cv2 as cv
import numpy as np

''' Hough Transformation to detect circles in an image '''

# image = cv.imread('./Images/col_balls.jpg')
# image_copy = image.copy()

# image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# image_gray = cv.medianBlur(image_gray, 5)

# circles = cv.HoughCircles(image_gray, cv.HOUGH_GRADIENT,
#                           1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
# # print("Circles: ", circles)

# circles = np.uint16(np.around(circles))

# for (x, y, r) in circles[0, :]:
#     cv.circle(image_copy, (x, y), r, (0, 255, 0), 2)
#     cv.circle(image_copy, (x, y), 2, (0, 0, 255), 3)

# cv.imshow('Detected Circles', image_copy)

# cv.imshow('Original Image', image)


''' Hough Transformation to detect circles using webcam '''

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.medianBlur(frame_gray, 5)

    circles = cv.HoughCircles(frame_gray, cv.HOUGH_GRADIENT,
                              1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

    if circles is not None:
        circles = np.uint16(np.around(circles))

        for (x, y, r) in circles[0, :]:
            cv.circle(frame, (x, y), r, (0, 255, 0), 2)
            cv.circle(frame, (x, y), 2, (0, 0, 255), 3)

    cv.imshow('Detected Circles', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cv.waitKey(0)
cv.destroyAllWindows()
