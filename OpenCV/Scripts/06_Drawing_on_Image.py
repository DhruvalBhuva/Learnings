import cv2
import numpy as np

image = cv2.imread('lena.jpg', 1)

# create Image using numpy
image = np.zeros([512, 512, 3], np.uint8)  # it creates 512*512 image

# line(<imgOBJ>,tuple of starting Co-ordinate, tuple of ending Co-ordinate, clr in BGR format, thickness )
image = cv2.line(image, (0, 0), (255, 255), (0, 0, 255),
                 5)  # B = 255 means blue line on img
image = cv2.arrowedLine(image, (255, 255), (500, 500), (0, 255, 0), 5)

# rectangle(<imgOBJ>,Top Left vertex co,Lower right vertex co, thickness)
# image = cv2.rectangle(image, (384, 0), (510, 228), 5)
# thickness negative values fill rectangle
image = cv2.rectangle(image, (384, 0), (510, 228), (255, 0, 0), -1)

# circle(<imgOBJ, center, radius,clr, thickness>
image = cv2.circle(image, (447, 63), 63, (0, 255, 0), -1)

# putText( <imgObj>, Text, org point, fontScale, color, thickness)
image = cv2.putText(image, "OpenCV", (10, 500),
                    cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 10, cv2.LINE_AA)

cv2.imshow("Lena Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
