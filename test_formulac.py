import urllib.request
import os
import random
import numpy as np
import cv2
import imageio
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance


'''
#转换成灰度图像
img = Image.open("img/beach_wood_copy.png")
img_g=ImageEnhance.Color(img).enhance(0.0)
img_g.save('img/beach_wood_copy_g.png')
'''
img=imageio.imread('sky.jpg')
img_g=imageio.imread('sky_g.jpg')

plt.imshow(img)
plt.show()
plt.imshow(img_g)
plt.show()
'''
print(img[0][0]) #123.3 / 370
print(img_g[0][0]) #121 / 363

print(img[0][1])  #122.3  / 367
print(img_g[0][1])  #120 / 360

print(img[0][2])  #120.6  / 362
print(img_g[0][2])  #119 / 357

print(img[0][3])  #119.6  / 359
print(img_g[0][3])  #117 / 351
'''

m=img_g.shape[0]
n=img_g.shape[1]
r=[0 for i in range(m)] #row
c=[0 for j in range(n)] #column

print("m:",m," n",n)


for i in range(0,m):
    for j in range(0,n):
        r[i]+=img_g[i][j][0]
for i in range(0,m):
    for j in range(0,n):
        c[j]+=img_g[i][j][0]

for i in range(0,m):
    r[i]= r[i]/n
for j in range(0,n):
    c[j]=c[j]/m

for i in range(0,m):
    print("i=",i,":",r[i])
for j in range(0,n):
    print("j=",j,":",c[j])



