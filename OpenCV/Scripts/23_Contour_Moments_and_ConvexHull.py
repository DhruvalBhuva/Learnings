'''
Moments: Moments are used to describe the shape of an object in an image.
    - cv.moments() function is used to calculate the moments of an image.
    - cv.contourArea() function is used to calculate the area of the contour.
    - cv.arcLength() function is used to calculate the perimeter of the contour.
    - cv.approxPolyDP() function is used to approximate the shape of the contour.

Convex Hull: Convex Hull is the smallest convex shape that encloses all the points in the shape.
'''

import cv2 as cv
import numpy as np

img = cv.imread('./Images/shapes.png')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Thresholding the image
_, thresh = cv.threshold(imgGray, 240, 255, cv.THRESH_BINARY)

# Finding contours
contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Drawing contours
# cv.drawContours(img, contours, -1, (0, 255, 0), 3)

for contour in contours:
    # Calculating the moments of the contour
    M = cv.moments(contour)

    # Calculating the area of the contour
    area = cv.contourArea(contour)

    # Calculating the perimeter of the contour
    perimeter = cv.arcLength(contour, True)

    # Approximating the shape of the contour
    epsilon = 0.01 * perimeter
    approx = cv.approxPolyDP(contour, epsilon, True)

    # Drawing the approximated shape
    cv.drawContours(img, [approx], -1, (0, 255, 0), 3)

    # Drawing the convex hull
    hull = cv.convexHull(contour)
    cv.drawContours(img, [hull], -1, (0, 0, 255), 3)

    # Calculating the area of the convex hull
    hull_area = cv.contourArea(hull)

    # Calculating the solidity of the shape
    solidity = area / hull_area

    # Drawing the centroid of the shape
    if M['m00'] != 0:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv.circle(img, (cx, cy), 5, (255, 0, 0), -1)

        # Drawing the text
        cv.putText(img, f'Area: {area}', (cx, cy + 20),
                   cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        # cv.putText(img, f'Perimeter: {perimeter}', (cx, cy + 40), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        # cv.putText(img, f'Solidity: {solidity}', (cx, cy + 60), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)


cv.imshow('Original Image', img)
cv.imshow('Gray Image', imgGray)
cv.imshow('Threshold Image', thresh)

cv.waitKey(0)
cv.destroyAllWindows()
