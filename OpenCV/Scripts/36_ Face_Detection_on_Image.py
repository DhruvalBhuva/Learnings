''' Face detection using Haar cascades 
    - Haar cascades is a machine learning-based approach.
    - It is used to detect the objects in an image.
    - It is more effective than the traditional image processing techniques.
    
    - cv.CascadeClassifier.detectMultiScale(image, scaleFactor, minNeighbors) -> objects
        - image: Input image.
        - scaleFactor: Parameter specifying how much the image size is reduced at each image scale.
        - minNeighbors: Parameter specifying how many neighbors each candidate rectangle should have to retain it.
        
        - objects: It returns the detected objects.

    - cv.CascadeClassifier.load(filename) -> retval
        - filename: Name of the file from which the classifier is loaded.
        
        - retval: It returns the CascadeClassifier object.
'''

import cv2 as cv
import numpy as np

# Load the image
img = cv.imread('./Images/a.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

face = cv.CascadeClassifier("./cascades/haarcascade_frontalface_default.xml")
eye = cv.CascadeClassifier("./cascades/haarcascade_eye.xml")

faces = face.detectMultiScale(img_gray, 4, 4)


for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Eyes detection
    roi_gray = img_gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    eyes = eye.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

cv.imshow('Face Detection', img)

cv.waitKey(0)
cv.destroyAllWindows()
