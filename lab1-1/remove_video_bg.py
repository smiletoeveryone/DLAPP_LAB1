import cv2

cap=cv2.VideoCapture("data.mp4")
fps = cap.get(5)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# fourcc = cv2.VideoWriter_fourcc(*'MP4V')
_, frame = cap.read()
out = cv2.VideoWriter('data_output.avi', fourcc, fps, (frame.shape[1], frame.shape[0]), False)
j=0
while 1:
    _,frame=cap.read()
    if(j==0):
        bg=frame.copy().astype("float")
    if(j<30):
        cv2.accumulateWeighted(frame,bg,0.1)
        j=j+1
    diff=cv2.absdiff(frame,bg.astype("uint8"))
    diff=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    thre,diff=cv2.threshold(diff,25,255,cv2.THRESH_BINARY)
    out.write(diff)
    cv2.imshow("output",diff)
    if(cv2.waitKey(1) & 0XFF==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()

