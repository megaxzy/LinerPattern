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

img = Image.open("img/central_park_copy.png")
img_g=ImageEnhance.Color(img).enhance(0.0)
img_g.save('img/central_park_copy_g.png')