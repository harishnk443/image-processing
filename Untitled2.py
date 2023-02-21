#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')


# In[4]:


loaded_image = cv2.imread('img.png')
loaded_image = cv2.cvtColor(loaded_image,cv2.COLOR_BGR2RGB)


# In[11]:


gray_img = cv2.cvtColor(loaded_image,cv2.COLOR_BGR2RGB)
edged_image = cv2.Canny(gray_img, threshold1=30, threshold2=100)


# In[12]:


plt.figure(figsize=(20,20))
plt.subplot(1,3,1)
plt.imshow(loaded_image,cmap='gray')
plt.title('original Image')
plt.axis('off')
plt.subplot(1,3,2)
plt.imshow(gray_img,cmap='gray')
plt.axis('off')
plt.title('GrayScale')
plt.subplot(1,3,3)
plt.imshow(edged_image,cmap='gray')
plt.axis('off')
plt.title('Canny Edge Detected Image')
plt.show()


# In[16]:


import cv2
import numpy as np
from matplotlib import pyplot as plt
img0 = cv2.imread('img.png',)
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2RGB)
img = cv2.GaussianBlur(gray,(3,3),0)
laplacian = cv2.Laplacian(img,cv2.CV_64F)
soblex = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)


# In[19]:


plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(soblex,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobley,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()


# In[23]:


import cv2
import numpy as np
from matplotlib import pyplot as plt
img0 = cv2.imread('img.png',)
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2RGB)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,-0,1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
cv2.imshow('Original Image', img)
cv2.imshow('prewitt X', img_prewittx)
cv2.imshow('prewitt Y', img_prewitty)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:




