'''
- Backgroud substraction is a technique to extract the foreground from the background.
- Technically, it is a process of detecting moving objects in a video and then removing from the static background.

1) BackgroundSubtractorMOG2:
    - It is a Gaussian Mixture-based Background/Foreground Segmentation Algorithm.
    - It is more effective in detecting moving objects in a video.
    - It is faster than the BackgroundSubtractorKNN.

2) BackgroundSubtractorKNN:
    - It is a K-nearest Neighbour-based Background/Foreground Segmentation Algorithm.
    - It is more accurate than MOG2 but slower.
    - It is more effective in handling shadows and detecting moving objects in a video.
'''

import cv2 as cv
import numpy as np

# Load the video
cap = cv.VideoCapture('./Images/test2.mp4')

mog2 = cv.createBackgroundSubtractorMOG2()
knn = cv.createBackgroundSubtractorKNN()


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    fgmask = mog2.apply(frame)
    # fgmask = knn.apply(frame)

    cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fgmask)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
