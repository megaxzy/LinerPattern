import urllib.request
import os
import random
import numpy as np
from PIL import Image
import cv2
import imageio
import matplotlib.pyplot as plt





img_test=imageio.imread('img/beach_wood_copy.png')
m=img_test.shape[0]
n=img_test.shape[1]
print("hight,m,row number:",m)
print("width,n,column number:",n)
'''
遍历所有像素
for i in range(0,m):
    for j in range(0,n):
        print("i=",i,",j=",j,":",img_test[i,j,0]," ")
'''
'''
#建立数组 越往前越内
#4是7中的4；0是3中的0；1是2中的1
matrix = [[[0 for i in range(2)] for i in range(3)]for i in range(7)]
matrix[4][0][1]=565
print(matrix)
'''

L=[[[0 for k in range (3)] for j in range(n)]for i in range(m)] #m*n*k
r=[[0 for k in range(3)] for i in range(m)] #row
c=[[0 for k in range(3)] for j in range(n)] #column
for i in range(0,m):
    for j in range(0,n):
        for k in range(1,4):
            r[i][k-1]+=img_test[i][j][k-1]
for i in range(0,m):
    for j in range(0,n):
        for k in range(1,4):
            c[j][k-1]+=img_test[i][j][k-1]

for i in range(0,m):
    for k in range(1, 4):
        r[i][k-1]= r[i][k-1]/n
for j in range(0,n):
    for k in range(1, 4):
        c[j][k-1]=c[j][k-1]/m

'''
for i in range(0,m):
    for k in range(1, 4):
        print("r[",i,"][",k-1,"]:",r[i][k-1])
for j in range(0,n):
    for k in range(1, 4):
        print("c[",j,"][",k-1,"]:",c[j][k - 1])
'''
print()
r_R=np.array(r).astype('int64')
print(r_R)



x= np.linspace(0, m, m)
plt.plot(x, r_R, label='RGB')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()

'''
E=[[0 for k in range(3)] for i in range(2)] #Energy
for i in range(0,m):
    for k in range(1, 4):
        E[0][k-1]+=r[i][k-1]*r[i][k-1]
for j in range(0,n):
    for k in range(1, 4):
        E[1][k-1]+=c[j][k-1]*c[j][k-1]


print(E[0][0])
print(E[0][1])
print(E[0][2])
print(E[1][0])
print(E[1][1])
print(E[1][2])
'''
def r_c(img):
    m = img.shape[0]
    n = img.shape[1]
    print("hight,m,row number:", m)
    print("width,n,column number:", n)
    L = [[[0 for k in range(3)] for j in range(n)] for i in range(m)]  # m*n*k
    r = [[0 for k in range(3)] for i in range(m)]  # row
    c = [[0 for k in range(3)] for j in range(n)]  # column
    for i in range(0, m):
        for j in range(0, n):
            for k in range(0,3):
                r[i][k] += img[i][j][k]
    for i in range(0, m):
        for j in range(0, n):
            for k in range(0,3):
                c[j][k] += img[i][j][k]

    for i in range(0, m):
        for k in range(0, 3):
            r[i][k] = r[i][k] / n
    for j in range(0, n):
        for k in range(0, 3):
            c[j][k] = c[j][k] / m


def enery(m,n,r,c):
    E = [[0 for k in range(3)] for i in range(2)]  # Energy
    for i in range(0, m):
        for k in range(0,3):
            E[0][k] += r[i][k] * r[i][k]
    for j in range(0, n):
        for k in range(0, 3):
            E[1][k] += c[j][k] * c[j][k]

def enery_g(m,n,r,c):
    E = [[0 for k in range(3)] for i in range(2)]  # Energy
    for i in range(0, m):
        E[0][0] += r[i][0] * r[i][0]
    for j in range(0, n):
        E[1][0] += c[j][0] * c[j][0]