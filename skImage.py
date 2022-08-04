# -*- coding: utf-8 -*-
"""
Spyder Editor
Skimage Basics
"""
from skimage import io
from matplotlib import pyplot as plt
import os

imgPathList = os.listdir('C:/Users/MSSB2/Desktop/Image_Processing')
imgList = []
for path in imgPathList:
    a = io.imread('C:/Users/MSSB2/Desktop/Image_Processing/'+path)
    imgList.append(a)
    
plt.imshow(imgList[0])
