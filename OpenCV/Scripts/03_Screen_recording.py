import cv2
import numpy as np
import pyautogui as pag
# '''

# Create resolution => It messure recording screen resolution
rs = pag.size()

# File in which want to store recording
outputPath = input("Enter output path: ")

# Fix the frame rate
fps = 21.0

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter(outputPath, fourcc, fps, rs)

# create recording module
cv2.namedWindow("Live_Recording", cv2.WINDOW_NORMAL)

# Resize the window
# cv2.resizeWindow("Live Recording", (600, 400))

while True:
    img = pag.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    output.write(frame)

    cv2.imshow("Recording..", frame)

    if cv2.waitKey(25) == ord("q"):
        break

output.release()
cv2.destroyAllWindows()
# '''


'''
# Break the video into Images and store it in a folder
import cv2

# Path of video
videoPath = "output.avi"

# Create object of VideoCapture
cap = cv2.VideoCapture(videoPath)
ret, frame = cap.read()

count = 0

while ret:
    cv2.imwrite("Frames/frameN%d.jpg" % count, frame)
    cap.set(cv2.CAP_PROP_POS_MSEC, (count * 100))
    ret, frame = cap.read()

    count += 1

    if cv2.waitKey(25) == ord("q"):
        break
        cv2.destroyAllWindows()

cap.release()
cv2.destroyAllWindows()
'''
