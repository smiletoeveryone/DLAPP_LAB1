#!/usr/bin/python
# coding:utf-8

import cv2
import numpy as np

def NN_interpolation(img,dstH,dstW): #dstH, dstW for the size of new pic
    scrH,scrW,_=img.shape
    retimg=np.zeros((dstH,dstW,3),dtype=np.uint8)
    for i in range(dstH-1):
        for j in range(dstW-1): #calculate new coordinates
            scrx=round(i*(scrH/dstH)) #scrH, scrW for the size of original pic
            scry=round(j*(scrW/dstW))
            retimg[i,j]=img[scrx,scry]
    return retimg


img = cv2.imread("penquin.jpg")
zoom = NN_interpolation(img,img.shape[0]*2,img.shape[1]*2)
newimg_1 = cv2.resize(img, (1200, 800))
newimg_2 = cv2.resize(zoom, (1200, 800))
cv2.imwrite("origin.jpg", newimg_1)
cv2.imwrite("zoom.jpg", newimg_2)
newimg_1a = cv2.imread("origin.jpg")
newimg_2a = cv2.imread("zoom.jpg")

imghstack = np.hstack((newimg_2a, newimg_1a))
cv2.namedWindow("imghstack")
cv2.imshow("imghstack",imghstack)

if(cv2.waitKey(0)==27):
    cv2.destroyAllWindows()
