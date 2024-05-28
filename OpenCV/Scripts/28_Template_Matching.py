'''
Template Matching is a technique in computer vision used to find a sub-image in a larger image.
- It is a mothod for searching and finding the location of a template image in a larger image.
- It simply slides the template image over the input image and compares the template and patch of input image under the template image.
- It returns a grayscale image, where each pixel denotes how much does the neighbourhood of that pixel match with the template.
- It is used in object detection, image registration, etc.
- cv.matchTemplate(<input_image>, <template_image>, <method>)
- cv.minMaxLoc(<image>)
'''

import cv2 as cv
import numpy as np

image = cv.imread('./Images/avengers.jpg')
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Load the template image
template = cv.imread('./Images/temp.jpg', 0)

w, h = template.shape[::-1]

# Apply template matching
# There are many methods for template matching:
# - cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR, cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED
res = cv.matchTemplate(image_gray, template, cv.TM_CCOEFF_NORMED)
# cv.imshow('Result', res)

# Set a threshold
threshold = 0.9
# threshold = cv.minMaxLoc(res)[1] - 0.1

# Find the location of the template
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)


cv.imshow('Original Image', cv.resize(image, (512, 512)))

cv.waitKey(0)
cv.destroyAllWindows()
