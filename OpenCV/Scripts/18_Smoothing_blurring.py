# Diffrent types of filter
#
# # 1. Averaging
# # => convolve the image with a normalized box filter. It simply takes the average of all the pixels under kernel area and replaces the central element with this average.
# # => This is done by the function cv.blur() or cv.boxFilter(). Check the docs for more details about the kernel. We should specify the width and height of kernel.
# # => A 3x3 normalized box filter would look like this:
# # => If you don't want to use a normalized box filter, use cv.boxFilter() and pass the argument normalize=False to the function.
# # => Here, the function cv.blur() takes the average of all the pixels under the kernel area and replaces the central element with this average. This is done by the function cv.blur() or cv.boxFilter(). Check the docs for more details about the kernel. We should specify the width and height of kernel.

# # 2. Gaussian Filtering
# # => In this approach, instead of a box filter consisting of equal filter coefficients, a Gaussian kernel is used. It is done with the function, cv.GaussianBlur(). We should specify the width and height of the kernel which should be positive and odd. We also should specify the standard deviation in the X and Y directions, sigmaX and sigmaY respectively. If only sigmaX is specified, sigmaY is taken as equal to sigmaX. If both are given as zeros, they are calculated from the kernel size. Gaussian filtering is highly effective in removing Gaussian noise from the image.
# # => If you want, you can create a Gaussian kernel with the function, cv.getGaussianKernel().
# # => If you want to create a Gaussian filter of a different size than (5,5), with different sigmaX and sigmaY, you can create the kernel and pass it to the cv.filter2D() function.
# # => Gaussian blurring is highly effective in removing Gaussian noise from the image.
# # => Kernel:

# # 3. Median Filtering
# # => Here, the function cv.medianBlur() computes the median of all the pixels under the kernel window and the central pixel is replaced with this median value. This is highly effective against salt-and-pepper noise in the images. Interesting thing is that, in the above filters, central element is a newly calculated value which may be a pixel value in the image or a new value. But in median blurring, central element is always replaced by some pixel value in the image. It reduces the noise effectively. Its kernel size should be a positive odd integer.
# # => In this, the central element in the kernel area is replaced with the median of all the pixels under the kernel. This is highly effective against salt-and-pepper noise in the images. Interesting thing is that, in the above filters, central element is a newly calculated value which may be a pixel value in the image or a new value. But in median blurring, central element is always replaced by some pixel value in the image. It reduces the noise effectively. Its kernel size should be a positive odd integer.

# # 4. Bilateral Filtering
# # => As we noted, the filters we presented earlier tend to blur edges. This is not the case for the bilateral filter, cv.bilateralFilter(), which was defined for, and is highly effective at noise removal while preserving edges. But the operation is slower compared to other filters. We already saw that a Gaussian filter takes the a neighbourhood around the pixel and find its Gaussian weighted average. This Gaussian filter is a function of space alone, that is, nearby pixels are considered while filtering. It doesn't consider whether pixels have almost same intensity. It doesn't consider whether pixel is an edge pixel or not. So it blurs the edges also, which we don't want to do.
# # => Bilateral filter also takes a Gaussian filter in space, but one more Gaussian filter which is a function of pixel difference. Gaussian function of space make sure only nearby pixels are considered for blurring while Gaussian function of intensity difference make sure only those pixels with similar intensity to central pixel is considered for blurring. So it preserves the edges since pixels at edges will have large intensity variation.
# # => We already saw that a Gaussian filter takes the a neighbourhood around the pixel and find its Gaussian weighted average. This Gaussian filter is a function of space alone, that is, nearby pixels are considered while filtering. It doesn't consider whether pixels have almost same intensity. It doesn't consider whether pixel is an edge pixel or not. So it blurs the edges also, which we don't want to do.

# #5. Homogeneous Filtering
# # => Homogeneous filter is the most simple filter. Each output pixel is the mean of its kernel neighbors. This is done by convolving the image with a normalized box filter. It simply takes the average of all the pixels under kernel area and replaces the central element with this average. This is done by the function cv.blur() or cv.boxFilter(). Check the docs for more details about the kernel. We should specify the width and height of kernel. A 3x3 normalized box filter would look like this:
# # => If you don't want to use a normalized box filter, use cv.boxFilter() and pass the argument normalize=False to the function.
# # => Here, the function cv.blur() takes the average of all the pixels under the kernel area and replaces the central element with this average. This is done by the function cv.blur() or cv.boxFilter(). Check the docs for more details about the kernel. We should specify the width and height of kernel.
# kernel = (1 / kernal weight * kernel height) * [Identity Matrix of weight * height size]


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# img = cv.imread("opencv-logo.png",1)
# img = cv.imread("Halftone_Gaussian_Blur.jpg",1)
# img = cv.imread("water.png")
img = cv.imread("./Images/lena.jpg")

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

homogeneous_Kernel = np.ones((5, 5), np.float32) / 25

# As in one dimentional signals, images also can be filtered with various low-pass filter(LPF), high-pass filter(HPF)
# etc. LPF helps in removing noises, blurring the images etc. HPF filters helps in finding edges in the images.
# OpenCV provides a function cv.filter2D() to convolve a kernel with an image.
dst = cv.filter2D(img, -1, homogeneous_Kernel)

# Averaging: It is done by convolving the image with a normalized box filter. It simply takes the average of all the pixels under kernel area and replaces the central element with this average.
blur = cv.blur(img, (5, 5))

# Gaussian Filtering: It used for removing high frequency noice
gBlur = cv.GaussianBlur(img, (5, 5), 0)

# Median Filtering: It used for removing salt and pepper noice.(Black and white both the noice)
mBlur = cv.medianBlur(img, 5)  # Kernal size must be odd, exepts 1

# Bilateral Filtering: It used for removing noise while keeping edges sharp
bBlur = cv.bilateralFilter(img, 9, 75, 75)

titles = ["Image", "2D Convolution", "Blue",
          "gaussian Blur", "Median Blur", "Bilateral Blur"]
images = [img, dst, blur, gBlur, mBlur, bBlur]

for i in range(len(images)):
    plt.subplot(3, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv.destroyAllWindows()
