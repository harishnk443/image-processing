#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
from PIL import Image
img=cv2.imread('car.webp')
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


img2=Image.open('car.webp')
width=img2.width
height=img2.height
print("height:",height)
print("width:",width)


# In[ ]:


images=cv2.imread("car.webp",0)
print("no of channels is:"+str(img.ndim))
print("no of channels is:",img.shape)
cv2.imshow('images',images)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


import matplotlib.image as image
img1=image.imread('car.webp')
print("array")
print(img1)


# In[ ]:


from PIL import Image
filepath = "car.webp"
im = Image.open(filepath)
new_im = im.resize((400,400))
new_im


# In[ ]:


import cv2
img=cv2.imread("car.webp")
ret, bw_img=cv2.threshold(img , 127,225, cv2.THRESH_BINARY)
bw = cv2.threshold(img ,225, 127, cv2.THRESH_BINARY)
cv2.imshow("BINARY",bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


num1 = 15


# In[ ]:


num2 = 12


# In[ ]:


sum = num1 + num2


# In[ ]:


print("sum of {0} and {1} is {2}" .format(num1, num2, sum))

