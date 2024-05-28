'''
Image Pyramids: Image Pyramids is a type of multi-scale signal representation in which a signal or an image is subject to repeated smoothing and subsampling
- Sometimes, we need to work with images of different resolutions. For example, when we are working with face recognition, we need to work with images of different sizes. 
- In such cases, we can use image pyramids to work with images of different resolutions.

Types of Image Pyramids:
1. Gaussian Pyramids: Used to downsample the image
 - It has multiple levels, and each level has a lower resolution than the previous level.
    - The top level of the pyramid is the original image.
    - The bottom level of the pyramid is the smallest image.
    - cv.pyrDown() function is used to downsample the image.
    - cv.pyrUp() function is used to upsample the image.

2. Laplacian Pyramids: Used to reconstruct the image from the downsampled image
'''

import cv2 as cv
import numpy as np

img = cv.imread("./Images/sudoku.png", cv.IMREAD_GRAYSCALE)
img = cv.resize(img, (500, 500))

# Gaussian Pyramid
layer = img.copy()
gaussian_pyramid = [layer]
for i in range(6):
    layer = cv.pyrDown(layer)
    gaussian_pyramid.append(layer)
    cv.imshow(str(i), layer)


cv.imshow("Original Image", img)

cv.waitKey(0)
cv.destroyAllWindows()
