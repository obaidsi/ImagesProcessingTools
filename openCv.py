# -*- coding: utf-8 -*-
"""
Spyder Editor, Basics of OpenCv

@author: Obaid
"""
import cv2 # read Color in BGR 
from matplotlib import pyplot as plt

img  = cv2.imread("C:/Users/MSSB2/Desktop/Image_Processing/Img_Projects/webb_Img/aa.jpg", 1)
plt.imshow(img)

resized_img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
plt.imshow(resized_img)