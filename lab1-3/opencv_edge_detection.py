#!/usr/bin/python
# coding:utf-8

import cv2 
import numpy as np
# import matplotlib.pyplot as plt

image = cv2.imread("penquin.jpg") 
newimg = cv2.resize(image, (1200, 800))

#calculate the edges using Canny edge algorithm
edges = cv2.Canny(image, 100, 200)
cv2.imwrite("penquin_canny.jpg", edges)
newimg_1 = cv2.imread("penquin_canny.jpg")
newimg_resized = cv2.resize(newimg_1, (1200, 800))
imghstack = np.hstack((newimg, newimg_resized))
cv2.namedWindow("imghstack")
cv2.imshow("imghstack",imghstack)

if(cv2.waitKey(0)==27):
    cv2.destroyAllWindows()

