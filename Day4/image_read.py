import numpy as np
import cv2

cap = cv2.VideoCapture(2)

while(True):
	ret, frame = cap.read()
	frame = cv2.line(frame,(200,130),(200,300),(0,255,255),30)
	frame = cv2.line(frame,(100,100),(300,100),(0,0,255),10)
	frame = cv2.line(frame,(110,110),(290,110),(0,0,255),10)
	frame = cv2.line(frame,(110,120),(290,120),(0,0,255),10)
	frame = cv2.line(frame,(120,130),(280,130),(0,0,255),10)
	cv2.imshow('frame',frame)
	if cv2.waitKey(1)& 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows
