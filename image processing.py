#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
from PIL import Image
image=cv2.imread('car.webp',0)
cv2.imshow("TO DISPLAY IMAGE",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


cv2.imwrite('D:\image processing\car.webp',image)


# In[ ]:


cv2.waitKey(0)


# In[ ]:


cv2.destroyAllWindows()


# In[ ]:


import matplotlib.pyplot as plt
image=plt.imread('car.webp')
plt.imshow(image)
plt.show()


# In[ ]:


image.size


# In[ ]:


new_image=cv2.rotate(image,cv2.ROTATE_180)
cv2.imshow('Display image',new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


print(image.shape)


# In[ ]:


width, height = image.size
left = 4
top = height / 5
right = 154
bottom = 3 * height / 5


# In[ ]:


im = image.crop((left, top, right, bottom))
newsize = (300, 300)
im = im1.resize(newsize)
im.show()


# In[ ]:


im.size

