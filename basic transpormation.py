#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


image = cv2.imread('calvinHobbes.jpeg')


# In[3]:


height, width = image.shape[:2] 
quarter_height, quarter_width = height/4, width/4


# In[4]:


T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]]) 
img_translation = cv2.warpAffine(image, T, (width, height)) 


# In[ ]:


cv2.imshow("Originalimage", image) 
cv2.imshow('Translation', img_translation)
cv2.imwrite('Translation.jpg', img_translation) 
cv2.waitKey() 


# In[ ]:


cv2.destroyAllWindows()


# In[ ]:


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('panda1.jpg')

blur = cv2.blur(img,(5,5))

plt.imshow(img),plt.title('Original')
plt.show()
cv2.imwrite('orig.png', img)
plt.xticks([]), plt.yticks([])
plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
cv2.imwrite('boxfil.png', blur)


# In[ ]:


import cv2
import numpy as np


# In[ ]:


img = cv2.imread('panda.jpg', 0)
(h,w) = img.shape[:2]
center = (w/2, h/2)
angle45 = 45
scale = 1.0


# In[ ]:


M = cv2.getRotationMatrix2D(center, angle45, scale)


# In[ ]:


abs_cos = abs(M[0,0]) 
abs_sin = abs(M[0,1])


# In[ ]:


bound_w = int(h * abs_sin + w * abs_cos)
bound_h = int(h * abs_cos + w * abs_sin)


# In[ ]:


M[0, 2] += bound_w/2 - center[0]
M[1, 2] += bound_h/2 - center[1]


# In[ ]:


rotated30 = cv2.warpAffine(img, M, (bound_w,bound_h))


# In[ ]:


scale_percent = 110
width = int(rotated30.shape[1] * scale_percent / 100)
height = int(rotated30.shape[0] * scale_percent / 100)
dim = (width, height)


# In[ ]:


scaled = cv2.resize(rotated30, dim, interpolation=cv2.INTER_NEAREST)
scaled1 = cv2.resize(rotated30, dim, interpolation=cv2.INTER_LINEAR)
scaled2 = cv2.resize(rotated30, dim, interpolation=cv2.INTER_CUBIC)


# In[ ]:


cv2.imshow("Nearest Neighbour", scaled)
cv2.imshow("Bilinear", scaled1)
cv2.imshow("Bicubic", scaled2)


# In[ ]:


cv2.imwrite("Nearest Neighbour.jpg", scaled)
cv2.imwrite("Bilinear.jpg", scaled1)
cv2.imwrite("Bicubic.jpg", scaled2)
cv2.waitKey(0)
cv2.destroyAllWindows() 

