# ROI (Region of interest): Taking Specific part of image.

import cv2 as cv
import numpy as np

img1 = cv.imread("./Images/hero1.jpg")
img2 = cv.imread("./Images/strom_breaker.JPG")

img1 = cv.resize(img1, (1024, 650))
# Parent Image size must me either same or greater than image to be pasted
img2 = cv.resize(img2, (600, 650))

# Want to paste img2 on img1
row, col, channel = img2.shape

# ROI: Region of Interest
roi = img1[0:row, 0:col]

# Convert img2 to gray scale
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

# Thresholding: here value is try and error method. here for 50 we can get proper mask
_, mask = cv.threshold(img2gray, 50, 255, cv.THRESH_BINARY)

# Inverse mask
mask_inv = cv.bitwise_not(mask)

# Black out the area of logo in ROI
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)

# Take only region of logo from logo image
img2_fg = cv.bitwise_and(img2, img2, mask=mask)

# Put logo in ROI and modify the main image
dst = cv.add(img1_bg, img2_fg)

img1[0:row, 0:col] = dst


# cv.imshow("1=> Img1 Original", img1)
# cv.imshow("2=> Img2 Original", img2)
# cv.imshow("3=> ROI", roi)
# cv.imshow("4=> Img2 Gray", img2gray)
# cv.imshow("5=> Mask", mask)
# cv.imshow("6=> Mask Inverse", mask_inv)
# cv.imshow("7=> Img1 Background", img1_bg)
# cv.imshow("8=> Img2 Foreground", img2_fg)
cv.imshow("9=> Final Image", img1)

cv.waitKey(0)
cv.destroyAllWindows()
