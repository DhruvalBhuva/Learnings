# Image blending: It is the process of overlaying two images of the same size to form a new image.

# cv2.addWeighted() method is used to blend two images.
# Syntax: cv2.addWeighted(img1, alpha, img2, beta, gamma)
# img1: First image
# alpha: Weight of the first image elements to be applied to the final image
# img2: Second image
# beta: Weight of the second image elements to be applied to the final image
# gamma: Scalar added to each sum
# alpha + beta = 1

# cv2.add() method is used to add two images.
# Syntax: cv2.add(img1, img2)
# img1: First image
# img2: Second image

import cv2
import numpy as np

image1 = cv2.imread('./Images/lena.jpg')
image2 = cv2.imread('./Images/messi.jpg')

# Resize the images
image1 = cv2.resize(image1, (512, 512))
image2 = cv2.resize(image2, (512, 512))

# Adding the images
added_image = cv2.add(image1, image2)
cv2.imshow("Added Image", added_image)

# Blending the images
blended_image = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)
cv2.imshow("Blended Image", blended_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
