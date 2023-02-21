#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2
im=cv2.imread("car.webp")
grey=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
cv2.imshow('im',grey)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[11]:


hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
cv2.imshow('im',hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[12]:


lab=cv2.cvtColor(im,cv2.COLOR_BGR2LAB)
cv2.imshow('im',lab)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[13]:


hls=cv2.cvtColor(im,cv2.COLOR_BGR2HLS)
cv2.imshow('im',hls)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[10]:


yuv=cv2.cvtColor(im,cv2.COLOR_BGR2YUV)
cv2.imshow('im',yuv)
cv2.waitKey(0)
cv2.destroyAllWindows()

