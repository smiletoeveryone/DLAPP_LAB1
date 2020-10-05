#!/usr/bin/python
# coding:utf-8

import cv2
import numpy as np

img = cv2.imread('penquin.jpg')

img1 = np.power(img/float(np.max(img)), 1/1.5)
img2 = np.power(img/float(np.max(img)), 1.5)
newimg_1 = cv2.resize(img, (600, 400))
newimg_2 = cv2.resize(img1, (600, 400))
newimg_3 = cv2.resize(img2, (600, 400))

imghstack = np.hstack((newimg_3, newimg_2, newimg_1))

cv2.namedWindow("imghstack")
cv2.imshow("imghstack",imghstack)

if(cv2.waitKey(0)==27):
    cv2.destroyAllWindows()
