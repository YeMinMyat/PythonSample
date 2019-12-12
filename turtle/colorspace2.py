# import cv2 as cv
# import numpy as np 
# cap = cv.VideoCapture(0)
# while(1):

# 	#Take each frame
# 	_, frame = cap.read()

# 	#Convert BGR to HSV
# 	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

# 	# define range of blue color on HSV
# 	lower_blue = np.array([110,50,50])
# 	upper_blue = np.array([130,255,255])

# 	#Threshold the HSV image to get only blue colors
# 	mask = cv.inRange(hsv, lower_blue, upper_blue)

# 	#Bitwise-AND mask and original image
# 	res = cv.bitwise_and(frame,frame, mask= mask)

# 	cv.imshow('frame',frame)
# 	cv.imshow('mask' ,mask)
# 	cv.imshow('res',res)
# 	k = cv.waitKey(5) & 0xFF
# 	if k == 27:
# 		break

# cv.destroyAllwindows()

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
while(1):

	#Take each frame
	_, frame = cap.read()

	#Convert BGR to HSV
	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

	# define range of blue color on HSV
	lower_red = np.array([160,20,70])
	upper_red = np.array([190,255,255])

	lower_green = np.array([41,68,55])
	upper_green = np.array([122,224,185])

	#Threshold the HSV image to get only blue colors
	mask_red = cv.inRange(hsv, lower_red, upper_red)
	mask_green = cv.inRange(hsv, lower_green, upper_green)

	mask = cv.bitwise_or(mask_red, mask_green)

	#Birwise-AND mask and original image
	res = cv.bitwise_and(frame, frame, mask= mask)

	cv.imshow('frame',frame)
	cv.imshow('mask' ,mask)
	cv.imshow('res' ,res)
	k = cv.waitKey(5) & 0xFF
	if k == 27:
		break
cv.destroyAllwindows()


