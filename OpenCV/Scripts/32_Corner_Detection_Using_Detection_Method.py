'''
Corner Detection Using Detection Method

1) Harris Corner Detection:
    - It is a corner detection algorithm that checks for a corner in the image.
    - It is a mathematical method that checks the intensity variation in the image.
    - It is used to detect the corners in the image.
    - It returns an array where each row is a vector that contains the parameters (x, y) of the detected corner.

    - cv.cornerHarris(<image>, <blockSize>, <ksize>, <k>)
        - blockSize: It is the size of the neighborhood considered for corner detection.
        - ksize: Aperture parameter of the Sobel derivative used.
        - k: Harris detector free parameter in the equation.


2) Shi-Tomasi Corner Detection:
    - It is a corner detection algorithm that is an improvement over the Harris Corner Detection algorithm.
    - It is used to detect the corners in the image.
    - It returns an array where each row is a vector that contains the parameters (x, y) of the detected corner.

    - cv.goodFeaturesToTrack(<image>, <maxCorners>, <qualityLevel>, <minDistance>)
        - maxCorners: Maximum number of corners to return.
        - qualityLevel: Parameter characterizing the minimal accepted quality of image corners.
        - minDistance: Minimum possible Euclidean distance between the returned corners.


3) FAST (Features from Accelerated Segment Test) Corner Detection:
    - It is a corner detection algorithm that is used to detect the corners in the image.
    - It returns an array where each row is a vector that contains the parameters (x, y) of the detected corner.

    - cv.FastFeatureDetector_create(<threshold>)
        - threshold: Threshold on difference between intensity of the central pixel and pixels of a circle around this pixel.


4) BRIEF (Binary Robust Independent Elementary Features) Corner Detection:
    - It is a corner detection algorithm that is used to detect the corners in the image.
    - It returns an array where each row is a vector that contains the parameters (x, y) of the detected corner.

    - cv.xfeatures2d.BriefDescriptorExtractor_create()
'''

import cv2 as cv
import numpy as np

image = cv.imread('./Images/shapes.png')
image = cv.resize(image, (512, 512))
cv.imshow('Original Image', image)


image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# Convert the image to float32 because cv.cornerHarris() function requires float32 datatype
image_gray = np.float32(image_gray)

# Harris Corner Detection
corner = cv.cornerHarris(image_gray, 2, 3, 0.04)
image[corner > 0.01 * corner.max()] = [0, 0, 255]
cv.imshow('Harris Corner Detection', image)

# Shi-Tomasi Corner Detection
corner = cv.goodFeaturesToTrack(image_gray, 25, 0.01, 10)
corner = np.int0(corner)
for i in corner:
    x, y = i.ravel()
    cv.circle(image, (x, y), 3, (0, 255, 0), -1)

cv.imshow('Shi-Tomasi Corner Detection', image)

cv.waitKey(0)
cv.destroyAllWindows()
