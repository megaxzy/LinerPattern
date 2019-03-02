import imageio
import matplotlib.pyplot as plt
import denoising
import math

class picture_grey:
    num=0
    def __init__(self,str):  #初始化
        self.img = imageio.imread(str)
        #在图片中，如果是-1会自动化成255，同理-2变成254
        #self.img_after_denoising = imageio.imread(str)
        #self.img_noise_model = imageio.imread(str)
        self.m = self.img.shape[0] #m是高
        self.n = self.img.shape[1] #n是长
        picture.num+=1
        print("high,m,row number:", self.m)
        print("width,n,column number:", self.n)

    def show_img(self):
        plt.imshow(self.img)
        plt.show()

    def show_img_after_denoising(self):
        plt.imshow(self.img_after_denoising)
        plt.show()

    def show_img_noise_model(self):
        plt.imshow(self.img_noise_model)
        plt.show()

    def denoising_grey(self):
        #选择的合适去噪方法 TODO
        self.img_after_denoising =denoising.convolution_wave_filter_gray(self.img_after_denoising)
        #计算噪声总和
        sum=0
        #计算噪声模板
        for i in range(0, self.m):
            for j in range(0, self.n):
                self.img_noise_model[i][j][0] = (int(self.img[i][j][0])-int(self.img_after_denoising[i][j][0]))
                self.img_noise_model[i][j][1]=self.img_noise_model[i][j][2]=self.img_noise_model[i][j][0]
                sum+=self.img_noise_model[i][j][0]
                if(i<10 and j<10):
                    print(i," ",j,":",self.img_noise_model[i][j][0])
                    print("    ", int(self.img[i][j][0]))
                    print("    " , int(self.img_after_denoising[i][j][0]))
        #计算平均值
        w_average=sum/(self.m*self.n)
        print("average:",w_average)
        #减去平均值
        for i in range(0, self.m):
            for j in range(0, self.n):
                self.img_noise_model[i][j][0] -= w_average
                self.img_noise_model[i][j][1] = self.img_noise_model[i][j][2] = self.img_noise_model[i][j][0]
                if (i < 10 and j < 10):
                    print(i, " ", j, ":", self.img_noise_model[i][j][0])
                    print("    ", self.img[i][j][0])
                    print("    " , self.img_after_denoising[i][j][0])

    def calculate_r_c_grey(self): #计算r和c
        L = [[[0 for k in range(3)] for j in range(self.n)] for i in range(self.m)]  # m*n*k
        r = [[0 for k in range(3)] for i in range(self.m)]  # row
        c = [[0 for k in range(3)] for j in range(self.n)]  # column
        for i in range(1, self.m):
            for j in range(1, self.n-1): #假设边界不修改，则最外层不进行计算，减少时间
                r[i][0] += self.img_noise_model[i][j][0]
        for i in range(1, self.m):
            for j in range(1, self.n-1):
                c[j][0] += self.img_noise_model[i][j][0]
        for i in range(1, self.m-1):
            r[i][0] = r[i][0] / self.n
        for j in range(0, self.n-1):
            c[j][0] = c[j][0] / self.m
        self.r=r
        self.c=c


    def calculate_enery_grey(self):
        E = [[0 for k in range(3)] for i in range(2)]  # Energy
        for i in range(1, self.m-1):
            E[0][0] += self.r[i][0] * self.r[i][0]
        for j in range(1, self.n-1):
            E[1][0] += self.c[j][0] * self.c[j][0]
        E[0][0] = E[0][0] * self.n / self.m
        E[1][0] = E[1][0] * self.m / self.n
        self.e=E

    def overlap_grey(self):
        self.M=math.ceil(self.m/picture.w)
        self.N=math.ceil(self.n/picture.w)
        print("M",self.M)
        print("N", self.N)
        L = [[[0 for k in range(3)] for j in range(self.N)] for i in range(self.M)]  # m*n*k
        for i in range(0,self.M-1):  #这里可能需要改进 #TODO
            for j in range (0,self.N-1):
                L[i][j][0]=L[i][j][1]=L[i][j][2]=picture.lp(self,i,j)
                print("i",i,"j",j,"L",L[i][j])
        self.L=L

    def lp(self,x,y):#TODO
        sum=0.0
        q=int(x*picture.w)
        for i in range(q,q+picture.w):
            sum += self.r[i][0]
        h=int(y*picture.w)
        for j in range (h,h+picture.w):
            sum+=self.c[i][0]
        return sum

    def PSD_y_grey(self):
        yr = [[0 for k in range(3)] for i in range(picture.w)]
        for k in range(1,picture.w):
            for i in range(1,picture.w):
                if(i+k>picture.w):
                    yr[k]+=self.r[i][0]*self.r[i+k-picture.w][0]
                else:
                    yr[k] += self.r[i][0] * self.r[i + k][0]
        for k in range(1, picture.w):
            yr[k]= yr[k]/picture.w

        yc = [[0 for k in range(3)] for i in range(picture.w)]
        for k in range(1,picture.w):
            for i in range(1,picture.w):
                if(i+k>picture.w):
                    yc[k]+=self.c[i][0]*self.c[i+k-picture.w][0]
                else:
                    yc[k] += self.c[i][0] * self.c[i + k][0]
        for k in range(1, picture.w):
            yc[k]= yc[k]/picture.w

        self.yc=yc
        self.yr=yr

    def PSD_s_grey(self):
        sr=[[0 for k in range(3)] for i in range(picture.w)]


class picture:
    num=0
    w=50  #size
    def __init__(self,str):  #初始化
        self.img = imageio.imread(str)
        self.img_after_denoising = imageio.imread(str)
        self.img_noise_model = imageio.imread(str)
        self.m = self.img.shape[0] #m是高
        self.n = self.img.shape[1] #n是长
        picture.num+=1
        print("high,m,row number:", self.m)
        print("width,n,column number:", self.n)
        #print(self.img)

    def show_img(self):
        plt.imshow(self.img)
        plt.show()

    def show_img_after_denoising(self):
        plt.imshow(self.img_after_denoising)
        plt.show()

    def show_img_noise_model(self):
        plt.imshow(self.img_noise_model)
        plt.show()

    def denoising_RGB(self):
        self.img_after_denoising=denoising.convolution_wave_filter(self.img_after_denoising)
        self.img_after_denoising =denoising.convolution_wave_filter_gray(self.img_after_denoising)
        for i in range(0, self.m):
            for j in range(0, self.n):
                for k in range(0, 3):
                    self.img_noise_model[i][j][k] += (int(self.img[i][j][k])-int(self.img_after_denoising[i][j][k]))

    def denoising_grey(self):
        self.img_after_denoising =denoising.convolution_wave_filter_gray(self.img_after_denoising)
        for i in range(0, self.m):
            for j in range(0, self.n):
                self.img_noise_model[i][j][0] = (int(self.img[i][j][0])-int(self.img_after_denoising[i][j][0]))
                self.img_noise_model[i][j][1]=self.img_noise_model[i][j][2]=self.img_noise_model[i][j][0]

    def calculate_r_c_RGB(self): #计算r和c
        L = [[[0 for k in range(3)] for j in range(self.n)] for i in range(self.m)]  # m*n*k
        r = [[0 for k in range(3)] for i in range(self.m)]  # row
        c = [[0 for k in range(3)] for j in range(self.n)]  # column
        for i in range(1, self.m):
            for j in range(1, self.n-1): #假设边界不修改，则最外层不进行计算，减少时间
                for k in range(0, 3):
                    r[i][k] += (int(self.img[i][j][k])-int(self.img_after_denoising[i][j][k]))
        for i in range(1, self.m):
            for j in range(1, self.n-1):
                for k in range(0, 3):
                    c[j][k] += (int(self.img[i][j][k])-int(self.img_after_denoising[i][j][k]))
        for i in range(1, self.m-1):
            for k in range(1, 3):
                r[i][k] = r[i][k] / self.n
        for j in range(0, self.n-1):
            for k in range(0, 3):
                c[j][k] = c[j][k] / self.m
        self.r=r
        self.c=c

    def calculate_r_c_grey(self): #计算r和c
        L = [[[0 for k in range(3)] for j in range(self.n)] for i in range(self.m)]  # m*n*k
        r = [[0 for k in range(3)] for i in range(self.m)]  # row
        c = [[0 for k in range(3)] for j in range(self.n)]  # column
        for i in range(1, self.m):
            for j in range(1, self.n-1): #假设边界不修改，则最外层不进行计算，减少时间
                r[i][0] += self.img_noise_model[i][j][0]
        for i in range(1, self.m):
            for j in range(1, self.n-1):
                c[j][0] += self.img_noise_model[i][j][0]
        for i in range(1, self.m-1):
            r[i][0] = r[i][0] / self.n
        for j in range(0, self.n-1):
            c[j][0] = c[j][0] / self.m
        self.r=r
        self.c=c

    def calculate_enery_RGB(self):
        E = [[0 for k in range(3)] for i in range(2)]  # Energy
        for i in range(1, self.m-1):
            for k in range(0, 3):
                E[0][k] += self.r[i][k] * self.r[i][k]
        for j in range(1, self.n-1):
            for k in range(0, 3):
                E[1][k] += self.c[j][k] * self.c[j][k]
        for k in range(0,3):
            E[0][k] = E[0][k] * self.n / self.m
            E[1][k] = E[1][k] * self.m / self.n
        self.e = E

    def calculate_enery_grey(self):
        E = [[0 for k in range(3)] for i in range(2)]  # Energy
        for i in range(1, self.m-1):
            E[0][0] += self.r[i][0] * self.r[i][0]
        for j in range(1, self.n-1):
            E[1][0] += self.c[j][0] * self.c[j][0]
        E[0][0] = E[0][0] * self.n / self.m
        E[1][0] = E[1][0] * self.m / self.n
        self.e=E

    def overlap_grey(self):
        self.M=math.ceil(self.m/picture.w)
        self.N=math.ceil(self.n/picture.w)
        print("M",self.M)
        print("N", self.N)
        L = [[[0 for k in range(3)] for j in range(self.N)] for i in range(self.M)]  # m*n*k
        for i in range(0,self.M-1):  #这里可能需要改进 #TODO
            for j in range (0,self.N-1):
                L[i][j][0]=L[i][j][1]=L[i][j][2]=picture.lp(self,i,j)
                print("i",i,"j",j,"L",L[i][j])
        self.L=L

    def lp(self,x,y):#TODO
        sum=0.0
        q=int(x*picture.w)
        for i in range(q,q+picture.w):
            sum += self.r[i][0]
        h=int(y*picture.w)
        for j in range (h,h+picture.w):
            sum+=self.c[i][0]
        return sum

    def PSD_y_grey(self):
        yr = [[0 for k in range(3)] for i in range(picture.w)]
        for k in range(1,picture.w):
            for i in range(1,picture.w):
                if(i+k>picture.w):
                    yr[k]+=self.r[i][0]*self.r[i+k-picture.w][0]
                else:
                    yr[k] += self.r[i][0] * self.r[i + k][0]
        for k in range(1, picture.w):
            yr[k]= yr[k]/picture.w

        yc = [[0 for k in range(3)] for i in range(picture.w)]
        for k in range(1,picture.w):
            for i in range(1,picture.w):
                if(i+k>picture.w):
                    yc[k]+=self.c[i][0]*self.c[i+k-picture.w][0]
                else:
                    yc[k] += self.c[i][0] * self.c[i + k][0]
        for k in range(1, picture.w):
            yc[k]= yc[k]/picture.w

        self.yc=yc
        self.yr=yr

    def PSD_s_grey(self):
        sr=[[0 for k in range(3)] for i in range(picture.w)]


