#!/usr/bin/python
# coding:utf-8

import cv2
import numpy as np

image = cv2.imread("penquin.jpg")
cv2.imwrite("origin.jpg", image)
newimg_1 = cv2.imread("origin.jpg")
newimg_1a = cv2.resize(image, (1200, 800))

img_hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imwrite("hsv_demo.jpg", img_hsv)
newimg_2 = cv2.imread("hsv_demo.jpg")
newimg_hsv = cv2.resize(newimg_2, (1200, 800))

imghstack = np.hstack((newimg_1a, newimg_hsv))
cv2.namedWindow("imghstack")
cv2.imshow("imghstack",imghstack)

if(cv2.waitKey(0)==27):
    cv2.destroyAllWindows()
