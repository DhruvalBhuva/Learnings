import cv2

img = cv2.imread("messi.jpg")
img2 = cv2.imread("opencv-logo.png")

print(img.shape)  # return a tuple of number of rows, columns, channels
print(img.size)  # return total number of pixels
print(img.dtype)  # return image data type

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

# choose object within Images and store it in variable
ball = img[280:340, 330:390]  # [Left top cor, right bottom cor]
img[273:333, 100:160] = ball

# Add() method Calculate the pre-element sum of two arrays or an array and a scalar.
# Need array of same size therefore required resizing
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
dst = cv2.add(img, img2)

# addWeight() method calculate the weighted sum of the two arrays.
# addWeight(<scr1>,<alpha>,<scr2>,<beta>,<gamma>)
# Formula used dst(I) = saturate(scr1*alpha+scr2*beta+gamma)
dst = cv2.addWeighted(img, .9, img2, .1, 0)  # aplha + beta = 1

cv2.imshow("Lena", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
