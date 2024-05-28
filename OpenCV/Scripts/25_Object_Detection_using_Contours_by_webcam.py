import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0, cv.CAP_DSHOW)


def nothing(x):
    pass


cv.namedWindow('Colorbars')
cv.createTrackbar('Threshold', 'Colorbars', 0, 255, nothing)

cv.createTrackbar('lowH', 'Colorbars', 0, 255, nothing)
cv.createTrackbar('lowS', 'Colorbars', 0, 255, nothing)
cv.createTrackbar('lowV', 'Colorbars', 0, 255, nothing)

cv.createTrackbar('UpH', 'Colorbars', 0, 255, nothing)
cv.createTrackbar('UpS', 'Colorbars', 255, 255, nothing)
cv.createTrackbar('UpV', 'Colorbars', 255, 255, nothing)


while True:
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lowH = cv.getTrackbarPos('lowH', 'Colorbars')
    UpH = cv.getTrackbarPos('UpH', 'Colorbars')
    lowS = cv.getTrackbarPos('lowS', 'Colorbars')
    UpS = cv.getTrackbarPos('UpS', 'Colorbars')
    lowV = cv.getTrackbarPos('lowV', 'Colorbars')
    UpV = cv.getTrackbarPos('UpV', 'Colorbars')

    lower_bound = np.array([lowH, lowS, lowV])
    upper_bound = np.array([UpH, UpS, UpV])

    mask = cv.inRange(hsv, lower_bound, upper_bound)

    filtered = cv.bitwise_and(frame, frame, mask=mask)
    # cv.imshow('Filtered', filtered)

    # converting to background black and foreground white
    mask = cv.bitwise_not(mask)

    # thresholding the mask
    threadshold = cv.getTrackbarPos('Threshold', 'Colorbars')
    _, mask = cv.threshold(mask, threadshold, 255, cv.THRESH_BINARY)

    dilate = cv.dilate(mask, (1, 1), iterations=6)

    contours, _ = cv.findContours(
        dilate, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    print(f'Number of contours: {len(contours)}')

    # frame = cv.drawContours(frame, contours, -1, (0, 255, 0), 3)

    for contour in contours:
        epsilon = 0.0001 * cv.arcLength(contour, True)
        approx = cv.approxPolyDP(contour, epsilon, True)

        hull = cv.convexHull(approx)

        cv.drawContours(frame, [contour], -1, (0, 255, 0), 3)
        cv.drawContours(frame, [hull], -1, (0, 0, 255), 3)

    cv.imshow('Frame', frame)
    cv.imshow('Mask', mask)
    cv.imshow('Filtered', filtered)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
