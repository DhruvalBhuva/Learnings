'''
Object Tracking and Detection
1. Object Tracking using MeanShift
    - MeanShift is a method to track the objects in a video.
    - It is based on the density estimation technique.
    - It is used to track the objects in a video.

    - cv.meanShift(probImage, window, criteria) -> retval, window
        - probImage: Back projection of the object histogram.
        - window: Initial search window.
        - criteria: Stop criteria for the algorithm.

        - retval: It returns the number of iterations the algorithm took to converge.
        - window: It returns the coordinates of the object.

2. Object Tracking using CamShift
    - CamShift is an extension of MeanShift.
    - It is used to track the objects in a video.
    - It is more effective than MeanShift.

    - cv.CamShift(probImage, window, criteria) -> retval, window
        - probImage: Back projection of the object histogram.
        - window: Initial search window.
        - criteria: Stop criteria for the algorithm.

        - retval: It returns the rotated rectangle structure.
        - window: It returns the coordinates of the object.

3. Object Detection using Haar Cascades
    - Haar Cascades is a machine learning-based approach.
    - It is used to detect the objects in an image.
    - It is more effective than the traditional image processing techniques.

    - cv.CascadeClassifier.detectMultiScale(image, scaleFactor, minNeighbors) -> objects
        - image: Input image.
        - scaleFactor: Parameter specifying how much the image size is reduced at each image scale.
        - minNeighbors: Parameter specifying how many neighbors each candidate rectangle should have to retain it.

        - objects: It returns the detected objects.
'''

import cv2 as cv
import numpy as np

# Load the video
cap = cv.VideoCapture('./Images/test2.mp4')

# first frame
ret, frame = cap.read()

# Set the initial location of the window
x, y, w, h = 580, 30, 80, 150
track_window = (x, y, w, h)

# Set the region of interest
roi = frame[y:y+h, x:x+w]

# Convert the region of interest to HSV
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)),
                  np.array((180., 255., 255.)))

# Calculate the histogram
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])

# Normalize the histogram
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

# Set the termination criteria
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

''' Object Tracking using MeanShift '''
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break

#     hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

#     dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

#     # Apply the mean shift to get the new location
#     ret, track_window = cv.meanShift(dst, track_window, term_crit)

#     # Draw the rectangle on the image
#     x, y, w, h = track_window
#     img2 = cv.rectangle(frame, (x, y), (x+w, y+h), 255, 2)

#     cv.imshow('img2', img2)

#     if cv.waitKey(30) == ord('q'):
#         break


''' Object Tracking using CamShift '''

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    # Apply the cam shift to get the new location
    ret, track_window = cv.CamShift(dst, track_window, term_crit)

    # Draw the rotated rectangle on the image
    pts = cv.boxPoints(ret)
    pts = np.int0(pts)
    img2 = cv.polylines(frame, [pts], True, 255, 2)

    cv.imshow('img2', img2)

    if cv.waitKey(30) == ord('q'):
        break


cap.release()
cv.destroyAllWindows()
