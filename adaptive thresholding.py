#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


img = cv2.imread('car.webp', cv2.IMREAD_GRAYSCALE)
cv2.imshow('gray', img)


# In[3]:


blur = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('blur', blur)


# In[4]:


ret,th1 = cv2.threshold(blur,150,255,cv2.THRESH_BINARY)
cv2.imshow('car', th1)
cv2.imwrite('car.webp',th1)


# In[5]:


th2 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('Adaptive Mean', th2)
cv2.imwrite('merry.jpg',th2)


# In[7]:


th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('merry2', th3)
cv2.imwrite('merry2.jpg',th3)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




