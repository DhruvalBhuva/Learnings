import cv2

# => Loads a color image. Any transparency of image will be neglected. It is the default flag.

# this function is used to read the image from location
img1 = cv2.imread('./Images/lena.jpg', -1)  # -1 for alpha channels
img2 = cv2.imread('./Images/lena.jpg', 0)  # 0 for gray images
img3 = cv2.imread('./Images/lena.jpg', 1)  # 1 for color images

img1 = cv2.resize(img1, (200, 400))  # width ,height
img2 = cv2.resize(img2, (200, 400))  # width ,height
img3 = cv2.resize(img3, (200, 400))  # width ,height


# It accept two parameters 1)- Name of screen ,2) -  Image
cv2.imshow("Alpha Image", img1)
cv2.imshow("Gray Image", img2)
cv2.imshow("Colored Image", img3)

# It shows Image in turms of matrix
print("Give image with color: \n", img1)

# here parameter inside waitkey handle the life duration of an image
cv2.waitKey(0)
cv2.destroyAllWindows()


# => Read User input image and save it

imgPath = input("Enter Image full path: ")
print("Your entered file path is:", imgPath)

img4 = cv2.imread(imgPath, 1)
img4 = cv2.resize(img4, (560, 700))
img4 = cv2.flip(img4, 0)  # it accept 3 parameters 0,-1,1

cv2.imshow("User Image", img4)

k = cv2.waitKey(0) & 0xFF
if k == ord("q"):
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite("", img4)
    cv2.destroyAllWindows()
