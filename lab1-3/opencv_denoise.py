#!/usr/bin/python
# coding:utf-8

import cv2
import numpy as np

image = cv2.imread ("penquin.jpg") 
newimg = cv2.resize(image, (1200, 800))
dst = cv2.fastNlMeansDenoisingColored (newimg, None , 15, 15, 7, 21)
gray = cv2.cvtColor(newimg, cv2.COLOR_BGR2GRAY) 
gret = cv2.fastNlMeansDenoising(gray, None, 15, 8, 25)
cv2.imwrite("penquin_demo.jpg", gret)

image_1 = cv2.imread("penquin_demo.jpg")
newimg_1 = cv2.resize(image_1, (1200, 800))
imghstack = np.hstack((newimg, newimg_1))
cv2.namedWindow("imghstack")
cv2.imshow("imghstack",imghstack)

if(cv2.waitKey(0)==27):
    cv2.destroyAllWindows()
