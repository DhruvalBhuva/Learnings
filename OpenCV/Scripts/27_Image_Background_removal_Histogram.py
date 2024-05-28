import cv2 as cv
import numpy as np

image = cv.imread('./Images/green.jpg')
image = cv.resize(image, (512, 512))

hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

# ROI of background
roi = cv.imread('./Images/g.jpg')
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

# Histogram ROI
roi_hist = cv.calcHist([hsv_roi], [0, 1], None, [
                       180, 256], [0, 180, 0, 256], 1)
mask = cv.calcBackProject([hsv_image], [0, 1], roi_hist, [0, 180, 0, 256], 1)

# Filtering remove noise
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
mask = cv.filter2D(mask, -1, kernel)
_, mask = cv.threshold(mask, 100, 255, cv.THRESH_BINARY)

mask = cv.merge((mask, mask, mask))
result = cv.bitwise_or(image, mask)


cv.imshow('Original Image', image)
cv.imshow('Result', result)

cv.waitKey(0)
cv.destroyAllWindows()
