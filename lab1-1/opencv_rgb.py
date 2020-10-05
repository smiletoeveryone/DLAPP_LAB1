#!/usr/bin/python
# coding:utf-8

import cv2
import numpy as np

image = cv2.imread("penquin.jpg")
# newimg = cv2.resize(image, (600, 400))
cv2.imwrite("origin.jpg", image)
image_1 = cv2.imread("origin.jpg")
image_1a = cv2.resize(image_1, (600, 400))

(B,G,R) = cv2.split(image)
cv2.imwrite("blue.jpg", B)
cv2.imwrite("green.jpg", G)
cv2.imwrite("red.jpg", R)
newimg_1 = cv2.imread("blue.jpg")
newimg_2 = cv2.imread("green.jpg")
newimg_3 = cv2.imread("blue.jpg")
newimg_1a = cv2.resize(newimg_1, (600, 400))
newimg_2a = cv2.resize(newimg_2, (600, 400))
newimg_3a = cv2.resize(newimg_3, (600, 400))

imghstack = np.hstack((image_1a, newimg_3a, newimg_2a, newimg_1a))
cv2.namedWindow("imghstack")
cv2.imshow("imghstack",imghstack)

if(cv2.waitKey(0)==27):
    cv2.destroyAllWindows()
