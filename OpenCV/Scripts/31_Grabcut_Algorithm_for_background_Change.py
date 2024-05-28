'''
- Grabcut Algorithm helps to cut the foreground object from the image and change the background of the image.
- It is an interactive tool that requires the user to provide a rectangle around the foreground object. It works like a ractangle portion mark on the image and are outise the rectangle is treated as the background, and it removes the background from the image.
- Gaussian Mixture Model (GMM) is used to model the background and foreground.

function:

1) cv.grabCut(<image>, <mask>, <rect>, <bgdModel>, <fgdModel>, <iterCount>, <mode>)

    - mask: It is a mask image where we specify which areas are background, foreground, etc. It is a 2D array with the same size as the image. The possible values of the mask are cv.GC_BGD, cv.GC_FGD, cv.GC_PR_BGD, cv.GC_PR_FGD, or simply pass 0, 1, 2, 3 to the mask.
    - rect: It is the coordinates of a rectangle which includes the foreground object in the format (x, y, width, height).
    - bgdModel: It is the array of the same size as the image. It is used to store the background model.
    - fgdModel: It is the array of the same size as the image. It is used to store the foreground model.
    - iterCount: Number of iterations the algorithm should run.
    - mode: It should be cv.GC_INIT_WITH_RECT or cv.GC_INIT_WITH_MASK or combined which decides whether we are drawing rectangle or final touchup strokes.
'''
import cv2 as cv
import numpy as np

image = cv.imread('./Images/car.jpg')
image = cv.resize(image, (800, 800))

mask = np.zeros(image.shape[:2], np.uint8)
background_Model = np.zeros((1, 65), np.float64)
foreground_Model = np.zeros((1, 65), np.float64)

# Part want to keep in the image
rect = (134, 150, 660, 730)  # (x, y, width, height)
cv.grabCut(image, mask, rect, background_Model,
           foreground_Model, 5, cv.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
image = image * mask2[:, :, np.newaxis]


cv.imshow('Original Image', image)
cv.waitKey(0)
cv.destroyAllWindows()
