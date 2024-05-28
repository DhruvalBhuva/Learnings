'''
Hough Transformation ia a popular technique to detect any shape, if you can represent that shape in mathematical form. It can detect the shape even if it is broken or distorted a little bit. We will see how it works for a line.
function: 
1) cv.HoughLines(<image>, <rho>, <theta>, <threshold>)
    - rho: Distance resolution of the accumulator in pixels.
    - theta: Angle resolution of the accumulator in radians.
    - threshold: Accumulator threshold parameter. Only those lines are returned that get enough votes (> threshold).

    - We represent a line and lines are expressed for Hough Transformation as coordinates (rho, theta). -> y = mx + c and in polar coordinates as (rho, theta) -> x * cos(theta) + y * sin(theta) = rho

    - We represent a line in mathematical form as:
        rho = x * cos(theta) + y * sin(theta)

    - It returns an array where each row is a vector that contains the parameters (rho, theta) of the detected line.


2) cv.HoughLinesP(<image>, <rho>, <theta>, <threshold>, <minLineLength>, <maxLineGap>)

    - rho: Distance resolution of the accumulator in pixels.
    - theta: Angle resolution of the accumulator in radians.
    - threshold: Accumulator threshold parameter. Only those lines are returned that get enough votes (> threshold).
    - minLineLength: Minimum line length. Line segments shorter than that are rejected.
    - maxLineGap: Maximum allowed gap between points on the same line to link them.

    - It is a probabilistic Hough Line Transform. It is an optimization of Hough Line Transform. It doesn't take all the points into consideration, instead, it takes only a random subset of points and that is sufficient for line detection.

    - It returns the start and end points of the line segment, unlike HoughLines which returns the line parameters.

    - It is more efficient than Hough Line Transform.
'''


import cv2 as cv
import numpy as np
image = cv.imread('./Images/chess.jpg')
# image = cv.imread('./Images/square.png')
image = cv.resize(image, (512, 512))
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

edges = cv.Canny(image_gray, 50, 150)

''' Hough Line Transformation
line = cv.HoughLines(edges, 1, np.pi/180, 200)
for rho, theta in line[:, 0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho

    # Here 1000 is a random number, you can choose any number. This number is used to draw the line from the center of the image to the edge of the image.
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))

    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
'''

# ''' # Hough Line Transformation Probabilistic
line = cv.HoughLinesP(edges, 1, np.pi/180, 100,
                      minLineLength=100, maxLineGap=10)
for x1, y1, x2, y2 in line[:, 0]:
    cv.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# '''

cv.imshow('Edges', edges)
cv.imshow('Original Image', image)
cv.waitKey(0)
cv.destroyAllWindows()
