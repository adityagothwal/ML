import cv2
import random

#now starting cam
cap = cv2.VideoCapture(0)

while	cap.isOpened():
	print("Camera is Working")
	status,frame=cap.read()
	bwing=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.rectangle(frame,(100,100),(200,200),(0,255,0),2)
	font=cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(frame, 'classroom', (100,100),font,2,(255,0,0), 5)
	cv2.imshow("camera1", frame)
	x=random.random()
	y=str(x)[2:6]
	cv2.imwrite('adhoc'+y+'.jpg',frame)
	cv2.imshow("camera2", bwing)
	if cv2.waitKey(1) & 0xFF == ord('q') :
		break
cv2.destroyAllWindows()
cap.release()
 