#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cv2
from matplotlib import pyplot as plt

image = cv2.imread('data.png')
img1 = cv2.resize(image, (500, 500), interpolation=cv2.INTER_NEAREST)
img2 = cv2.resize(image, (400, 400), interpolation=cv2.INTER_LINEAR)
img3 = cv2.resize(image, (300, 300), interpolation=cv2.INTER_AREA)
img4 = cv2.resize(image, (200, 200), interpolation=cv2.INTER_CUBIC)
img5 = cv2.resize(image, (400, 400), interpolation=cv2.INTER_LANCZOS4)

img0_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img3_rgb = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
img4_rgb = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)
img5_rgb = cv2.cvtColor(img5, cv2.COLOR_BGR2RGB)

titles = ['Original Image', 'INTER_NEAREST', 'INTER_LINEAR', 'INTER_AREA', 'INTER_CUBIC', 'INTER_LANCZOS4']
images = [img0_rgb, img1_rgb, img2_rgb, img3_rgb, img4_rgb, img5_rgb]
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
