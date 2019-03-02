import urllib.request
import os
import random
import numpy as np
from PIL import Image
import cv2
import imageio
import matplotlib.pyplot as plt


print("Hello World");
for letter in range(0,3):
    print("for: 循环",letter,"次");



img1 = Image.open("sky_g.jpg")
#img1.show()
print(img1.format) #JPG
print(img1.mode) #RGB
print(img1.size) #宽度 高度
img1_1 = Image.eval(img1, lambda i: i/2)
#img1_1.show()
# PIL.Image.eval(image, *args)函数对图像的每个像素进行执行函数。
# lambda表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。eg: add = lambda x, y : x+y  add(1,2)  # 结果为3




print("\n")
img = cv2.imread("sky_g.jpg",1) #1是强调G
print('Type of the image : ', type(img))
print('Shape of the image : {}'.format(img.shape))#高度 宽度 元素通道数
print('Image Hight {}'.format(img.shape[0]))
print('Image Width {}'.format(img.shape[1]))
print('Dimension of Image {}'.format(img.ndim))

#cv2.imshow("imshow",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


print('Value of only R channel {}'.format(img[ 100, 50, 0]))
print('Value of only G channel {}'.format(img[ 100, 50, 1]))
print('Value of only B channel {}'.format(img[ 100, 50, 2]))

'''
plt.title('R channel')
plt.ylabel('Height {}'.format(img.shape[0]))
plt.xlabel('Width {}'.format(img.shape[1]))
plt.imshow(img[:, :,2])#这表示所有
'''

img= imageio.imread('sky_g.jpg')
img[50:90 , 80:180 , 0] = 255 # full intensity to those pixel's R channel
plt.figure( figsize = (10,10))
plt.imshow(img)
plt.show()


img= imageio.imread('sky.jpg')
for i in range(0,100):
    for j in range (0,100):
        if (i+j)%3==0:
            img[i:i+1,j:j+1,0]=255
        if (i+j)%3==1:
            img[i:i+1,j:j+1,1]=255
        if (i+j)%3==2:
            img[i:i+1,j:j+1,2]=255
plt.imshow(img)
plt.show()


img_test=imageio.imread('sky.jpg')

def printme( str ):
   print(str);
   return;