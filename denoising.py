import math
import sys

def convolution_wave_filter( img ): #平均值 RGB
    length=img.shape[0]
    width=img.shape[1]
    for i in range(1,length-1):
        for j in range(1,width-1):
            for k in range(0,3):
                img[i][j][k]=nine_matrix(img,i,j,k)
    return img;

def convolution_wave_filter_gray( img ): #平均值 GRAY
    length=img.shape[0]
    width=img.shape[1]
    img_temp=img
    for i in range(1,length-1):
        for j in range(1,width-1):
            img[i][j] = D4_matrix(img,i,j,0)
    return img_temp;

def nine_matrix(img,i,j,k): #3*3取平均值
    sum=0
    sum+=int(img[i-1][j-1][k]) + int(img[i-1][j][k]) + int(img[i-1][j+1][k])
    sum+=int(img[i][j-1][k]) + int(img[i][j][k]) + int(img[i][j+1][k])
    sum+=int(img[i+1][j-1][k]) + int(img[i+1][j][k]) + int(img[i+1][j+1][k])
    average=round(sum/9)
    if average>255:
        average=255
    if average<0:
        average=0
    return average

def D4_matrix(img,i,j,k): #D4取平均值
    sum=0
    sum+=int(img[i][j-1][k]) + int(img[i][j+1][k]) + int(img[i-1][j][k])+int(img[i+1][j][k])
    average=round(sum/4)
    if average>255:
        average=255
    if average<0:
        average=0
    return average

def DB4(img,n):
    h0 = (1 + math.sqrt(3)) / (4 * math.sqrt(2))
    h1 = (3 + math.sqrt(3)) / (4 * math.sqrt(2))
    h2 = (3 - math.sqrt(3)) / (4 * math.sqrt(2))
    h3 = (1 - math.sqrt(3)) / (4 * math.sqrt(2))

    g0 = h3
    g1 = -h2
    g2 = h1
    g3 = -h0

    Ih0 = h2
    Ih1 = g2
    Ih2 = h0
    Ih3 = g0

    Ig0 = h3
    Ig1 = g3
    Ig2 = h1
    Ig3 = g1

    if n >= 4:
        half = n >> 1
        tmp = []
        j = 0
        i = 0
        while j < n - 3:
            tmp.insert(i, img[j] * h0 + img[j + 1] * h1 + img[j + 2] * h2 + img[j + 3] * h3)
            tmp.insert(i + half, img[j] * g0 + img[j + 1] * g1 + img[j + 2] * g2 + img[j + 3] * g3)
            i += 1
            j += 2
        tmp.insert(i, img[n - 2] * h0 + img[n - 1] * h1 + img[0] * h2 + img[1] * h3)
        tmp.insert(i + half, img[n - 2] * g0 + img[n - 1] * g1 + img[0] * g2 + img[1] * g3)

        for i in range(n):
            img[i] = tmp[i]
            print('a[%d]=:%4.2f' % (i, img[i]))

        return img


def iTransform(img, n):

    h0 = (1 + math.sqrt(3)) / (4 * math.sqrt(2))
    h1 = (3 + math.sqrt(3)) / (4 * math.sqrt(2))
    h2 = (3 - math.sqrt(3)) / (4 * math.sqrt(2))
    h3 = (1 - math.sqrt(3)) / (4 * math.sqrt(2))

    g0 = h3
    g1 = -h2
    g2 = h1
    g3 = -h0

    Ih0 = h2
    Ih1 = g2
    Ih2 = h0
    Ih3 = g0

    Ig0 = h3
    Ig1 = g3
    Ig2 = h1
    Ig3 = g1
    if n >= 4:
        i = 0
        j = 2
        half = n >> 1
        halfPls1 = half + 1
        tmp = []

        tmp.append(img[half - 1] * Ih0 + img[n - 1] * Ih1 + img[0] * Ih2 + img[half] * Ih3)
        tmp.append(img[half - 1] * Ig0 + img[n - 1] * Ig1 + img[0] * Ig2 + img[half] * Ig3)

        for i in range(half - 1):
            tmp.insert(j, img[i] * Ih0 + img[i + half] * Ih1 + img[i + 1] * Ih2 + img[i + halfPls1] * Ih3)
            j += 1
            tmp.insert(j, img[i] * Ig0 + img[i + half] * Ig1 + img[i + 1] * Ig2 + img[i + halfPls1] * Ig3)
            j += 1
        for i in range(n):
            img[i] = tmp[i]
            print('a[%d]=%4.2f' % (i, img[i]))
        return img


