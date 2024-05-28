# Morphological Transformations: Morphological Transformations are some simple oprations based on the image shape. It is normally performed on binary images. It needs two inputs, one is our original image, second one is called structuring element or kernel which decides the nature of operation. Two basic morphological operators are Erosion and Dilation. Then its variant forms like Opening, Closing, Gradient etc also comes into play. We will see them one-by-one with help of following image:

# # Erosion: The basic idea of erosion is just like soil erosion only, it erodes away the boundaries of foreground object (Always try to keep foreground in white). So what it does? The kernel slides through the image (as in 2D convolution). A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).

# # Dilation: It is just opposite of erosion. Here, a pixel element is '1' if atleast one pixel under the kernel is '1'. So it increases the white region in the image or size of foreground object increases. Normally, in cases like noise removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. So we dilate it. Since noise is gone, they won't come back, but our object area increases. It is also useful in joining broken parts of an object.

# # Opening: Opening is just another name of erosion followed by dilation. It is useful in removing noise, as we explained above. Here we use the function, cv.morphologyEx()

# # Closing: Closing is reverse of Opening, Dilation followed by Erosion. It is useful in closing small holes inside the foreground objects, or small black points on the object.

# # Morphological Gradient: It is the difference between dilation and erosion of an image.

# # Top Hat: It is the difference between input image and Opening of the image. Below example is done for a 9x9 kernel.

# # Black Hat: It is the difference between the closing of the input image and input image.

# # Structuring Element: It is used to define the neighborhood for the operation. It is just a mask image with 1's representing the neighbor pixels to be considered while performing the operation.

# # Kernel: Kernel is a convolution matrix used for performing image processing tasks like blurring, sharpening, edge detection, etc. The kernel is applied to every pixel in the image. The most common type of kernel is the Gaussian kernel, which is used for Gaussian blurring and Gaussian smoothing.

# # Kernel Size: Kernel size is the area over which the kernel is applied. The kern

# # Kernel Shape: Kernel shape is the shape of the kernel. The most common kernel shapes are square and rectangular.

# # Kernel Type: Kernel type is the type of kernel used. The most common kernel types are Gaussian kernels and box kernels.

# # Kernel Values: Kernel values are the values of the kernel matrix. The most common kernel values are 1/9, 1/16, 1/25, etc.

# # Kernel Normalization: Kernel normalization is the process of dividing the kernel values by the sum of the kernel values. This ensures that the sum of the kernel values is equal to 1.

# # Kernel Center: Kernel center is the center of the kernel. The kernel center is the pixel that is being processed.

# # Kernel Anchor: Kernel anchor is the anchor point of the kernel. The kernel anchor is the pixel that is being processed.

# # Kernel Border: Kernel border is the border of the kernel. The kernel border is the border of the kernel.

# # Kernel Border Type: Kernel border type is the type of border used for the kernel. The most common border types are zero border, replicate border, and reflect border.

# # Kernel Border Value: Kernel border value is the value of the border used for the kernel. The most common border values are zero, one, and minus one.

# # Kernel Border Size: Kernel border size is the size of the border used for the kernel. The most common border sizes are one, two, and three.

# # Kernel Border Normalization: Kernel border normalization is the process of dividing the kernel border values by the sum of the kernel border values. This ensures that the sum of the kernel border values is equal to 1.

# # Kernel Border Center: Kernel border center is the center of the kernel border. The kernel border center is the pixel that is being processed.

# # Kernel Border Anchor: Kernel border anchor is the anchor point of the kernel border. The kernel border anchor is the pixel that is being processed.

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("./Images/smarties.png", cv.IMREAD_GRAYSCALE)

# In the morphological transformation, it is mandatory to have black background and white foreground
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

# kernel: It slides over the image to perform the operation ,to remove small black doughts on ball of mask image
kernel = np.ones((2, 2), np.uint8)  # It creates 4*4 ractangle

# dilation: It is used to increase the size of the object in the image. Here, it is used to remove small black doughts on ball of mask image. As 4*4 ractangle is appiled on that dought, we can change iteration accordingly
dilation = cv.dilate(mask, kernel, iterations=3)

# Erosion: It is used to decrease the size of the object in the image. Here, it is used to remove small white doughts on ball of mask image. As 4*4 ractangle is appiled on that dought, we can change iteration accordingly
erosion = cv.erode(mask, kernel, iterations=2)

# Opening
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)

# Closing
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

# Morphological Gradient
mg = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel)

# Top Hat
th = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel)

# There are a lot of other methods are avilable

titles = ["Image", "Mask", "Dilation", "Erosion",
          "Opening", "Closing", "MG", "Top Hat"]
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(len(images)):
    plt.subplot(3, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv.destroyAllWindows()
