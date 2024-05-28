import cv2 as cv
import numpy as np

img = cv.imread('./Images/hand.jpg')
img = cv.resize(img, (600, 700))
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Removing noise from the image
blur = cv.medianBlur(imgGray, 11)

# Thresholding the image
_, thresh = cv.threshold(blur, 240, 255, cv.THRESH_BINARY_INV)

# Finding contours
contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(f'Number of contours: {len(contours)}')

# Drawing contours
# cv.drawContours(img, contours, -1, (0, 255, 0), 3)

for contour in contours:
    epsilon = 0.0001 * cv.arcLength(contour, True)
    approx = cv.approxPolyDP(contour, epsilon, True)

    hull = cv.convexHull(contour)

    cv.drawContours(img, [approx], -1, (0, 255, 0), 3)
    cv.drawContours(img, [hull], -1, (0, 0, 255), 3)

'''
Convexity Defects: Convexity defects are the points where the contour is not convex.
    - cv.convexityDefects() function is used to find the convexity defects in the contour.

hull = cv.convexHull(contour, returnPoints=False)
defects = cv.convexityDefects(contour, hull)

for defect in defects:
    start, end, far, _ = defect[0]
    start_point = tuple(contour[start][0])
    end_point = tuple(contour[end][0])
    far_point = tuple(contour[far][0])

    cv.circle(img, far_point, 5, (255, 0, 0), -1)
    cv.line(img, start_point, end_point, (0, 255, 0), 3)
'''

'''
Finding extreme points in the contour
leftmost = tuple(contour[contour[:, :, 0].argmin()][0])
rightmost = tuple(contour[contour[:, :, 0].argmax()][0])
topmost = tuple(contour[contour[:, :, 1].argmin()][0])
bottommost = tuple(contour[contour[:, :, 1].argmax()][0])

cv.circle(img, leftmost, 5, (255, 0, 0), -1)
cv.circle(img, rightmost, 5, (255, 0, 0), -1)
cv.circle(img, topmost, 5, (255, 0, 0), -1)
cv.circle(img, bottommost, 5, (255, 0, 0), -1)

cv.putText(img, 'Leftmost', leftmost, cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
cv.putText(img, 'Rightmost', rightmost, cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
cv.putText(img, 'Topmost', topmost, cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
cv.putText(img, 'Bottommost', bottommost, cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

'''

cv.imshow('Original Image', img)
# cv.imshow('Gray Image', imgGray)
cv.imshow('Threshold Image', thresh)


cv.waitKey(0)
cv.destroyAllWindows()
