import cv2 
import numpy as np 

cap = cv2.VideoCapture('data.mp4') 


while (cap.isOpened()): 
	# Capture frame-by-frame 
	ret, frame = cap.read() 
	frame = cv2.resize(frame, (540, 380), fx = 0, fy = 0, 
						interpolation = cv2.INTER_CUBIC) 

	# Display the resulting frame 
	cv2.imshow('Frame', frame) 

	# using cv2.Gaussianblur() method to blur the video 

	# (5, 5) is the kernel size for blurring. 
	gaussianblur = cv2.GaussianBlur(frame, (5, 5), 0) 
	cv2.imshow('gblur', gaussianblur) 

	if cv2.waitKey(25) & 0xFF == ord('q'): 
		break

cap.release() 
cv2.destroyAllWindows() 

