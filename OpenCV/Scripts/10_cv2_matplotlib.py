import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("./Images/lena.jpg", -1)
cv.imshow("Cv2 Image", img)

# Matplot uses RGB formate so need to transalate it
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img)

plt.xticks([]), plt.yticks([])  # To hide X,Y axis

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
