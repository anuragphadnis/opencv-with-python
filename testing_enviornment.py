
# import opencv and numpy for testing environment setup
import cv2
import numpy
#read image
img=cv2.imread("res/streak1.jpg")
#open a window and name it
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
#load img in Window
cv2.imshow("Image", img)
#define the window timeout time use 0 for infinite
cv2.waitKey(0)
#to save img that is read and to change its format
cv2.imwrite("streak_output.png",img)
