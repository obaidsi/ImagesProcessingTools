# -*- coding: utf-8 -*-
"""
Spyder Editor
Skimage Basics
"""
from skimage import io, color
from skimage.transform import rescale, resize, downscale_local_mean
from matplotlib import pyplot as plt
from skimage.util import random_noise
from skimage.filters import gaussian, sobel

# When as_gray=True skimage convert the image values to float 0 o 1
img = io.imread("C:/Users/MSSB2/Desktop/Image_Processing/Img_Projects/webb_Img/STScI-01G7DEE0V21GETVXYVT795AAV8.png", as_gray=True)
io.imshow(img)
img_rescaled = rescale(img, 0.25, anti_aliasing=(True))
io.imshow(img_rescaled)

img_resized = resize(img, (200, 200), anti_aliasing=(True))
plt.imshow(img_resized)

img_downscale = downscale_local_mean(img, (4, 3))
plt.imshow(img_downscale)

noisy_img = random_noise(img)
plt.imshow(noisy_img, cmap='gray')

filtered_img = gaussian(noisy_img)
plt.imshow(filtered_img, cmap='gray')

sobel_img = sobel(img)
plt.imshow(sobel_img, cmap='gray')
