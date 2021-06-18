#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

# python image library
from PIL import Image

pic = Image.open('/Users/junpark/Downloads/Computer-Vision-with-Python/DATA/00-puppy.jpg')

# to diplay image using matplotlib
# plt.imshow(pic)
# plt.show()

# type of image
print(type(pic))
# convert it into array
pic_arr = np.asarray(pic)
print(type(pic_arr))
# check the shapre with channel
print(np.shape(pic_arr))

# plt.imshow(pic_arr)
# plt.show()

pic_red = pic_arr.copy()
# change get the red channel value only
print(pic_red[:,:,0])
# gray scale
plt.imshow(pic_red[:,:,0], cmap='gray')
plt.show()

# display red channel only
pic_red[:,:,1] = 0
pic_red[:,:,2] = 0
plt.imshow(pic_red)
plt.show()

# Challenge
# isolate the blue channel
pic_blue = pic.copy()
print(np.shape(pic_blue))
