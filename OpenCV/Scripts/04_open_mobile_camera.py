import cv2, pafy

#'''
#connect your laptop and android device with same network either wifi or hotspot
# add this IP into browser to open on lptop
cameraIP = "https://192.168.0.15:8080/video"

#Here parameter 0 is a path of any video use for webcam

cap = cv2.VideoCapture(cameraIP)
#cap.open()

print("Cam check:", cap.isOpened())

#it is 4 byte code which is use to specify the video codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")

#It contain 4 parameter , name, codec,fps,resolution
outputObj = cv2.VideoWriter("Cam_video.mp4", fourcc, 20.0, (680, 400))

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        frame = cv2.resize(frame, (700, 600))
        outputObj.write(frame)
        
        cv2.imshow('Colorframe',frame)
        
        if cv2.waitKey(1) == ord("q"):
            break
    else:
        break

cap.release()
outputObj.release()
cv2.destroyAllWindows()
#'''

'''
# Capture video from youtube
youtubeURL = "https://www.youtube.com/watch?v=SLD9xzJ4oeU"

data = pafy.new(youtubeURL)
data = data.getbest(preftype="mp4")

cap = cv2.VideoCapture(data.url, cv2.CAP_DSHOW)

print("Cam check:", cap.isOpened())


while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        frame = cv2.resize(frame, (700, 600))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('Colorframe', frame)
        cv2.imshow("Gray Frame", gray)

        if cv2.waitKey(1) == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

'''