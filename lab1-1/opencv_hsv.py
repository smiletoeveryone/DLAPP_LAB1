#!/usr/bin/python
# coding:utf-8

import cv2
import numpy as np

image = cv2.imread("penquin.jpg")
# cv2.imwrite("origin.jpg", image)
# newimg_1 = cv2.imread("origin.jpg")
newimg_1a = cv2.resize(image, (600, 400))

img_hsv=cv2.cvtColor(newimg_1a,cv2.COLOR_BGR2HSV)
# cv2.imwrite("hsv_demo.jpg", img_hsv)
# newimg_2 = cv2.imread("hsv_demo.jpg")
# newimg_hsv = cv2.resize(newimg_2, (1200, 800))
h,s,v = cv2.split(img_hsv)
hsv_split = np.concatenate((h, s, v), axis=1)
cv2.imshow("Split HSV",hsv_split)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
imghstack = np.hstack((newimg_1a, newimg_hsv))
cv2.namedWindow("imghstack")
cv2.imshow("imghstack",imghstack)

if(cv2.waitKey(0)==27):
    cv2.destroyAllWindows()
'''