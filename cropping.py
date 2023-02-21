#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image


# In[2]:


im = Image.open(r"D:\hari images\merry.jpg")


# In[3]:


left = 155


# In[4]:


top = 65


# In[5]:


right = 360


# In[6]:


bottom = 270


# In[7]:


im1 = im.crop((left, top, right, bottom))


# In[10]:


im1.show()


# In[ ]:




