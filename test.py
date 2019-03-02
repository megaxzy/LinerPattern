import urllib.request
import os
import random
import numpy as np
from PIL import Image
import cv2
import imageio
import matplotlib.pyplot as plt
import denoising

img=imageio.imread('img/sky_g.jpg')
print(img[0][0])
#img=imageio.imread('img/beach_wood_g.png')

plt.imshow(img)
plt.show()


#img2=denoising.convolution_wave_filter_gray(img)

'''
imgGrey = cv2.imread('img/beach_wood.png', 0)
sp1 = img.shape
sp2 = imgGrey.shape
print(sp1)
print(sp2)
print(img)
print(imgGrey)
cv2.imwrite("img/beach_wood_g.png", imgGrey)
'''
'''
plt.imshow(img)
plt.show()
length = img.shape[0]
width = img.shape[1]
a=1
for i in range(1, length - 1):
    for j in range(1, width - 1):

        img[i][j][0] = nine_matrix(img,i,j,0)
        img[i][j][1] = nine_matrix(img,i,j,0)
        img[i][j][2] = nine_matrix(img,i,j,0)

        a=a+img[i][j][0]
'''