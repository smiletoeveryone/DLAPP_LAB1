#!/usr/bin/python
# coding:utf-8

import cv2
import numpy as np

image = cv2.imread('penquin.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray_demo.jpg", gray)
gray_demo = cv2.imread("gray_demo.jpg")

eq = cv2.equalizeHist(gray)
cv2.imwrite("eq_processed.jpg", eq)
eq_new_1 = cv2.imread("eq_processed.jpg")
newimg_1 = cv2.resize(image, (600, 400))
newimg_2 = cv2.resize(gray_demo, (600, 400))
newimg_3 = cv2.resize(eq_new_1, (600, 400))
imghstack = np.hstack((newimg_1, newimg_2, newimg_3))
cv2.namedWindow("imghstack")
cv2.imshow("imghstack",imghstack)


if(cv2.waitKey(0)==27):
    cv2.destroyAllWindows()

