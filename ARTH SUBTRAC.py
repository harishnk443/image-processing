#!/usr/bin/env python
# coding: utf-8

# In[1]:


import  cv2


# In[2]:


import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


first_img = cv2.imread("D://hari images//car.webp")


# In[4]:


second_img = cv2.imread("D://hari images//merry.jpg")


# In[5]:


print(first_img.shape)


# In[6]:


print(second_img.shape)


# In[7]:


dim =(680, 340)
resized_second_img = cv2.resize(second_img, dim, interpolation = cv2.INTER_AREA)
print("shape after resizing", resized_second_img.shape)


# In[8]:


subtracted = cv2.subtract(first_img, resized_second_img)


# In[9]:


cv2.imshow("first_img", first_img)
cv2.waitKey(0)
cv2.imshow("second_img", resized_second_img)
cv2.waitKey(0)
cv2.imshow("subtracted image", subtracted)
cv2.waitKey(0)


# In[10]:


cv2.destroyAllWindows


# In[11]:


import  cv2


# In[12]:


import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[13]:


first_img = cv2.imread("D://hari images//car.webp")


# In[14]:


second_img = cv2.imread("D://hari images//merry.jpg")


# In[15]:


print(first_img.shape)


# In[16]:


print(second_img.shape)


# In[17]:


dim =(680, 340)
resized_second_img = cv2.resize(second_img, dim, interpolation = cv2.INTER_AREA)
print("shape after resizing", resized_second_img.shape)


# In[18]:


multiplication = cv2.multiple(first_img, resized_second_img)


# In[ ]:




