import numpy as np
import cv2

cap = cv2.VideoCapture("data.mp4")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# point out how to encode videos
# I420-avi=>cv2.cv.CV_FOURCC('X','2','6','4');
# MP4=>cv2.cv.CV_FOURCC('M', 'J', 'P', 'G')
# The mp4 encoder in my computer do not work,so i just use X264
videoWriter = cv2.VideoWriter('output.avi', fourcc, fps, size)
# read one frame from the video
success, frame = cap.read()
while success:
    cv2.imshow("Output Video", frame)  # display this frame
    cv2.waitKey(int(fps))  # delay
    videoWriter.write(frame)  # write one frame into the output video
    success, frame = cap.read()  # get the next frame of the video
# some process after finish all the program
cv2.destroyAllWindows()     # close all the widows opened inside the program
cap.release        # release the video read/write handler
videoWriter.release
