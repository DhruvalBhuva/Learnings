# # =>Image Gradients: An image Gradients is a directional change in the intensity or color in an image

# Image Gradients Methods
# 1. Laplacian Derivatives:
#   Laplacian Derivatives is a 2nd order derivative method used to find areas of rapid change in an image

# 2. Sobel Derivatives
#   Sobel Derivatives is a joint Gausian smoothing plus differentiation operation, so it is more resistant to noise

# 3. Scharr Derivatives
#   Scharr Derivatives is a joint Gausian smoothing plus differentiation operation, so it is more resistant to noise

# 4. Canny Edge Detection
#   Canny Edge Detection is a multi-stage algorithm to detect a wide range of edges in images

# 5. Image Pyramids
#   Image Pyramids is a type of multi-scale signal representation in which a signal or an image is subject to repeated smoothing and subsampling

# 6. Contours in OpenCV
#   OpenCV has a function to find contours in an image

# 7. Histograms in OpenCV
#   Histograms is a graph or plot, which gives you an overall idea about the intensity distribution of an image

# 8. Image Transforms in OpenCV
#   Image Transforms in OpenCV is a transformation of an image, which is used to enhance the contrast of an image

# # =>Edge Detection: Edge detection is an image processing technique for finding the boundaries of objects within images

# Edge Detection Methods:
# 1. Canny Edge Detection
#   Canny Edge Detection is a multi-stage algorithm to detect a wide range of edges in images
#   It composed of 5 steps:
#       1. Noise Reduction: To smooth the image
#       2. Gradient Detection: To find edges
#       3. Non-maximum Suppression: To get rid of spurious response to edge detection
#       4. Double Threshold: To determine potential edges
#       5. Edge Tracking by Hysteresis: To finalize the detection of edges by suppressing all the other edges that are weak and not connected to strong edges

# 2. Sobel Edge Detection
#   Sobel Edge Detection is a joint Gausian smoothing plus differentiation operation, so it is more resistant to noise

# 3. Laplacian Edge Detection
#   Laplacian Edge Detection is a 2nd order derivative method used to find areas of rapid change in an image

# 4. Hough Line Detection
#   Hough Line Detection is a popular technique to detect any shape, if you can represent that shape in mathematical form

# 5. Hough Circle Detection
#   Hough Circle Detection is a popular technique to detect any shape, if you can represent that shape in mathematical form


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# img = cv.imread("messi.jpg",cv.IMREAD_GRAYSCALE)
img = cv.imread("./Images/sudoku.png", cv.IMREAD_GRAYSCALE)

# Laplacian Derivatives
# CV_64F: 64-bit floating point number
lap = cv.Laplacian(img, cv.CV_64F, ksize=1)
# laplacian can have negative values, so we take absolute value
lap = np.uint8(np.absolute(lap))

# Sobel Derivatives:
# 1: x-direction, 0: y-direction, 5th arguement can provide ksize
sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)  # 1: x-direction, 0: y-direction

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv.bitwise_or(sobelX, sobelY)

# Canny Edge Detection
canny = cv.Canny(img, 100, 200)  # 100: minVal, 200: maxVal

titles = ["Image", "Laplacian", "sobelX", "sobelY", "sobelCombined", "canny"]
images = [img, lap, sobelX, sobelY, sobelCombined, canny]

for i in range(len(images)):
    plt.subplot(3, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv.destroyAllWindows()
