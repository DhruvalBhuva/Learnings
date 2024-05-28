import cv2
import numpy as np

# Make Black Image
img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)

# Make white Image
# img2 = 255 * np.zeros((250, 500, 3), np.uint8)
# img2.fill(255)  # It makes image white, by default is 0 which is for black

img2 = np.zeros((250, 500, 3), np.uint8)
img2 = cv2.rectangle(img2, (250, 0), (500, 500), (255, 255, 255), -1)

bitAnd = cv2.bitwise_and(img1, img2)
bitor = cv2.bitwise_or(img1, img2)
bitxor = cv2.bitwise_xor(img1, img2)
bitnot1 = cv2.bitwise_not(img1)
bitnot2 = cv2.bitwise_not(img2)

cv2.imshow("Black Image", img1)
cv2.imshow("Mix Image", img2)

cv2.imshow("And Image", bitAnd)
cv2.imshow("or Image", bitor)
cv2.imshow("xor Image", bitxor)
cv2.imshow("not Image", bitnot)

cv2.waitKey(0)
cv2.destroyAllWindows()
