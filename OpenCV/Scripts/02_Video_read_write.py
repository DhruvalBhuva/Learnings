import cv2
import datetime

'''=>  Read video and open it '''

# '''

# for local video
cap = cv2.VideoCapture("./Images/video.mp4",)

# for camera
# cap = cv2.VideoCapture(0)

# print("video", cap)

while True:
    # read() returen ret  as True if frame is avilable
    ret, frame = cap.read()

    if ret == True:
        # print("Frame", frame)

        # Int value for cv2.CAP_PROP_FRAME_WIDTH is 3
        # print("Width: ", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # Int value for cv2.CAP_PROP_FRAME_HEIGHT is 4
        # print("Height: ", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # for More properties: https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d

        # Set height and width: it will set value as per camera resolution
        # cap.set(3, 200)
        # cap.set(4, 200)
        # print("Width: ", cap.get(3))
        # print("Height: ", cap.get(4))

        # Writing on the video
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Width:" + str(cap.get(3)) + ", Height:" + str(cap.get(4))
        dateTime = str(datetime.datetime.now())
        frame = cv2.putText(frame, dateTime, (10, 50), font,
                            1, (0, 255, 255), 2, cv2.LINE_AA)

        # frame = cap.resize(frame, (700, 450))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frameFlip = cv2.flip(frame, -1)

        cv2.imshow("ColorFrame", frame)
        # cv2.imshow("Gray Frame", gray)

    else:
        print("Error")
        break

    # waitKey(1) will display a frame for 1 ms, 25 will display for 25 ms, 0 will display frame until we close it
    # lesser the value of waitKey, faster the video will play.
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
# '''

''' 
# => Open video camera, record that video and save it 
 
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)   #Here parameter 0 is a path of any video use for webcam
print("checking..",cap.isOpened())

#it is 4 byte code which is use to specify the video codec
#Various codec -- DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
outputPath = "output.avi"
fps=20.0
height,weight=640,480

#It contain 4 parameter , name, codec,fps,resolution, isColor flag
outputObj = cv2.VideoWriter(outputPath,fourcc,fps,(height,weight),0)

while cap.isOpened():
    ret, frame = cap.read()
    
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame = cv2.flip(frame,0)
        outputObj.write(gray)
        
        cv2.imshow("Gray Frame", gray)
        cv2.imshow("Color Frame:", frame)
        
        if cv2.waitKey(25) == ord("q"):
            break
    else:
        break
    
# Release everything if job is finished
cap.release()
outputObj.release()
cv2.destroyAllWindows()
'''
