import pictures
import matplotlib.pyplot as plt


#t=3
img=pictures.picture_grey('img/sky_g.jpg')
#img=pictures.picture_grey('img/beach_wood_g.png')
#img=pictures.picture_grey('img/central_park_copy_g.png')
img.show_img()
img.denoising_grey()
img.show_img_after_denoising()
img.show_img_noise_model()
'''
img.calculate_r_c_grey()
img.calculate_enery_grey()
print(img.r)
print(img.c)
print(img.e)
img.overlap_grey()
print(img.L)
plt.imshow(img.L)
plt.show()
'''
