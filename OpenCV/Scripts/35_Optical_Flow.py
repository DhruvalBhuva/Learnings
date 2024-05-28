'''
Optical Flow is the pattern of apparent motion of image objects between two consecutive frames caused by the movement of object or camera. It is 2D vector field where each vector is a displacement vector showing the movement of points from first frame to second. It works on several assumptions:

1. The pixel intensities of an object do not change between consecutive frames.
2. Neighbouring pixels have similar motion.

There are two types of Optical Flow techniques:

1. Sparse Optical Flow: It tracks only a few points in the image.
2. Dense Optical Flow: It tracks all the points in the image.

cv.calcOpticalFlowPyrLK(prevImg, nextImg, prevPts, nextPts, status, err) -> nextPts, status, err
    - prevImg: Previous frame.
    - nextImg: Next frame.
    - prevPts: Points to track.
    - nextPts: Output points.
    - status: Output status vector.
    - err: Output vector.

    - nextPts: Output points.
    - status: Output status vector.
    - err: Output vector.

cv.calcOpticalFlowFarneback(prev, next, flow, pyr_scale, levels, winsize, iterations, poly_n, poly_sigma, flags) -> flow
    - prev: Previous frame.
    - next: Next frame.
    - flow: Output flow.
    - pyr_scale: Parameter specifying the image scale.
    - levels: Number of pyramid layers.
    - winsize: Window size.
    - iterations: Number of iterations.
    - poly_n: Polynomial size.
    - poly_sigma: Standard deviation.
    - flags: Operation flags.

    - flow: Output flow.

cv.DualTVL1OpticalFlow_create() -> retval
    - retval: It returns the Dual TV L1 Optical Flow object.
'''

import cv2 as cv
import numpy as np

# Load the video
cap = cv.VideoCapture('./Images/test2.mp4')

''' Sparse Optical Flow'''

# # Parameters for ShiTomasi corner detection
# feature_params = dict(maxCorners=100, qualityLevel=0.3,
#                       minDistance=7, blockSize=7)

# # Parameters for Lucas-Kanade optical flow
# lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(
#     cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

# color = np.random.randint(0, 255, (100, 3))

# # Take the first frame and find corners in it
# ret, old_frame = cap.read()
# old_frame = cv.resize(old_frame, (700, 600))
# old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
# p0 = cv.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

# mask = np.zeros_like(old_frame)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     frame = cv.resize(frame, (700, 600))
#     frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#     # Calculate optical flow
#     p1, st, err = cv.calcOpticalFlowPyrLK(
#         old_gray, frame_gray, p0, None, **lk_params)

#     # Select good points
#     good_new = p1[st == 1]
#     good_old = p0[st == 1]

#     # Draw the tracks
#     for i, (new, old) in enumerate(zip(good_new, good_old)):
#         a, b = new.ravel()
#         c, d = old.ravel()
#         mask = cv.line(mask, (int(a), int(b)),
#                        (int(c), int(d)), color[i].tolist(), 2)
#         frame = cv.circle(frame, (int(a), int(b)), 5, color[i].tolist(), -1)

#     img = cv.add(frame, mask)

#     cv.imshow('frame', img)

#     k = cv.waitKey(30) & 0xff
#     if k == 27:
#         break

#     # Now update the previous frame and previous points
#     old_gray = frame_gray.copy()
#     p0 = good_new.reshape(-1, 1, 2)

''' Gunner Farneback Dense Optical Flow '''

# Take the first frame
ret, frame1 = cap.read()
frame1 = cv.resize(frame1, (700, 600))
prvs = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[..., 1] = 255


while True:
    ret, frame2 = cap.read()
    if not ret:
        break

    frame2 = cv.resize(frame2, (700, 600))
    next = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)

    # Calculate the dense optical flow
    flow = cv.calcOpticalFlowFarneback(
        prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    # Compute the magnitude and angle of the 2D vectors
    mag, ang = cv.cartToPolar(flow[..., 0], flow[..., 1])

    # Set the hue according to the angle
    hsv[..., 0] = ang*180/np.pi/2

    # Set the value according to the magnitude
    hsv[..., 2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)

    # Convert HSV to BGR
    bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

    img = cv.add(frame2, bgr)

    cv.imshow('frame2', img)

    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

    prvs = next


cap.release()
cv.destroyAllWindows()
