import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

face = cv.CascadeClassifier("./cascades/haarcascade_frontalface_default.xml")


def detect_face(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(frame_gray, 1.3, 4)

    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    return frame


while True:
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)

    cv.imshow('Webcam', detect_face(frame))

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
