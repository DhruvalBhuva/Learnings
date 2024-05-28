'''
Contours are the boundaries of a shape with same intensity. It is useful for shape analysis and object detection and recognition.
 - It can be explained as a curve joining all the continuous points (along the boundary), having same color or intensity.
 - For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.
 - In OpenCV, finding contours is like finding white object from black background. So remember, object to be found should be white and background should be black.

cv.findContours(image, mode, method)
'''

import cv2 as cv
import numpy as np

img = cv.imread("./Images/logo.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Thresholding
_, mask = cv.threshold(gray, 70, 255, cv.THRESH_BINARY_INV)

# Find Contours
contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(f"Contours: {contours}")
print(f"Number of Contours: {len(contours)}")

# Draw Contours
# cv.drawContours(image, contours, contour_index, color, thickness)
# contour_index: -1 for all contours
# color: (B, G, R)
# thickness: -1 for fill the contour

draw = cv.drawContours(img, contours, -1, (0, 255, 0), 3)


cv.imshow("Original Image", img)
cv.imshow("Gray Image", gray)
cv.imshow("Mask Image", mask)
cv.imshow("Contours", draw)


cv.waitKey(0)
cv.destroyAllWindows()
