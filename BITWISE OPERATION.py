#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


img1 = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(img1, (100, 100), (250, 250), 255, -1)
cv2.imshow("pic.jpg", img1)


# In[3]:


img2 = np.zeros((300, 300), dtype="uint8")
cv2.circle(img2, (150, 150), 90, 255, -1)
cv2.imshow("car.webp", img2)
 


# In[4]:


rect_and_circle = cv2.bitwise_and(img1,img2)
cv2.imshow("AND operation",rect_and_circle)
 


# In[5]:


rect_or_circle = cv2.bitwise_or(img1,img2)
cv2.imshow("OR operation",rect_or_circle)


# In[6]:


rect_xor_circle = cv2.bitwise_xor(img1,img2)
cv2.imshow("XOR Operation",rect_xor_circle)


# In[7]:


rect_xor_circle2 = cv2.bitwise_xor(img1,img2)
cv2.imshow("XOR Operation",rect_xor_circle2)


# In[8]:


rect_xor_circle2 = cv2.bitwise_xor(img1,img2)
cv2.imshow("NOT Operation",rect_xor_circle)


# In[9]:


cv2.waitKey(0)
cv2.destroyAllWindows()

