#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt
import numpy as np
img1 = cv2.imread('merry.jpg', 0)
[m, n] = img1.shape
print('Image Shape:', m, n)
   
f = 4
img2 = np.zeros((m//f, n//f), dtype=np.int)
for i in range(0, m, f):
    for j in range(0, n, f):
        try:
 
            img2[i//f][j//f] = img1[i][j]
        except IndexError:
            pass
       
print('Down Sampled Image:')
plt.imshow(img2)


# In[2]:


img3 = np.zeros((m, n), dtype=np.int)
for i in range(0, m-1, f):
    for j in range(0, n-1, f):
        img3[i, j] = img2[i//f][j//f]
 
for i in range(1, m-(f-1), f):
    for j in range(0, n-(f-1)):
        img3[i:i+(f-1), j] = img3[i-1, j]
for i in range(0, m-1):
    for j in range(1, n-1, f):
        img3[i, j:j+(f-1)] = img3[i, j-1]
 
print('Up Sampled Image:')
plt.imshow(img3)


# In[5]:


from PIL import Image
import matplotlib.pyplot as plt
import pylab
import numpy as np
def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)

im = Image.open('merry.jpg')
pylab.figure(figsize=(20,30))
num_colors_list = [1 << n for n in range(8,0,-1)]
snr_list = []
i = 1
for num_colors in num_colors_list:
 im1 = im.convert('P', palette=Image.ADAPTIVE, colors=num_colors)
 pylab.subplot(4,2,i), pylab.imshow(im1), pylab.axis('off')
 snr_list.append(signaltonoise(im1, axis=None))
 pylab.title('Image with # colors = ' + str(num_colors) + ' SNR = ' +
 str(np.round(snr_list[i-1],3)), size=20)
 i += 1
pylab.subplots_adjust(wspace=0.2, hspace=0)
pylab.show()


# In[6]:


import cv2
import matplotlib.pyplot as plt
from PIL import Image
im = Image.open("merry.Jpg")
plt.imshow(im)
plt.show()
import cv2
import matplotlib.pyplot as plt
from PIL import Image
im = Image.open("merry.Jpg")
im = im.resize((im.width*5, im.height*5), Image.NEAREST)
plt.figure(figsize=(10,10))
plt.imshow(im)
plt.show()
im = Image.open("merry.Jpg")
im = im.resize((im.width//5, im.height//5))
plt.figure(figsize=(15,10))
plt.imshow(im)
plt.show()


# In[ ]:




