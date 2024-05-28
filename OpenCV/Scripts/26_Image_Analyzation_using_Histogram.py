'''
Image Analyzation using Histogram

- Histogram is a graphical representation of the distribution of numerical data.
- It is a kind of bar graph.
- It gives a rough idea about the distribution of pixel intensities in an image.
- X-axis represents the pixel intensities and Y-axis represents the frequency of that pixel intensity.
- It is used to analyze the contrast, brightness, intensity distribution, etc. of an image.
- It is used to analyze the quality of an image.
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

''' For black image  '''
# image = np.zeros((512, 512), np.uint8)

# # cv.rectangle(<image>, <start_point>, <end_point>, <color>, <thickness>)
# cv.rectangle(image, (0, 100), (256, 256), (255), -1)
# cv.rectangle(image, (0, 50), (50, 100), (127), -1)

# # calcHist(<images>, <channels>, <mask>, <histSize>, <ranges>)
# hist = cv.calcHist([image], [0], None, [256], [0, 256])

# plt.plot(hist)
# plt.show()

# cv.imshow('Black Image', image)


''' For colored image '''
# image = cv.imread('./Images/thor.jpg')
# image = cv.resize(image, (512, 512))

# b, g, r = cv.split(image)

# # hist(<images>, <channels>, <mask>, <histSize>, <ranges>)
# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])
# plt.show()

''' Grayscale image '''
# image = cv.imread('./Images/thor.jpg')
# image = cv.resize(image, (512, 512))
# img2gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# hist = cv.calcHist([img2gray], [0], None, [256], [0, 256])
# plt.plot(hist)
# plt.show()

''' Histogram Equalization: It is used to enhance the contrast of an image. '''
# image = cv.imread('./Images/thor.jpg')

# img2gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# equ = cv.equalizeHist(img2gray)

# res = np.hstack((img2gray, equ))
# cv.imshow('Equalized Image', res)

# hist = cv.calcHist([equ], [0], None, [256], [0, 256])
# plt.plot(hist)
# plt.show()

''' CLAHE (Contrast Limited Adaptive Histogram Equalization) 
- It is created to improve the contrast of an image.
- It is used to enhance the contrast of an image.
- It is used to improve the quality of an image and remove the noise.
'''
image = cv.imread('./Images/thor.jpg')
img2gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# createCLAHE(<clipLimit>, <tileGridSize>)
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img2gray)

cv.imshow('CLAHE Image', cl1)

hist = cv.calcHist([cl1], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
