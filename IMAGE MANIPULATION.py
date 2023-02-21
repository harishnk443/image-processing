#!/usr/bin/env python
# coding: utf-8

# In[7]:


from PIL import Image
from PIL import ImageFilter
import matplotlib.pyplot as plt
my_image = Image.open('pic.jpg')
sharp = my_image.filter(ImageFilter.SHARPEN)
sharp.save('D:image_sharpen.jpg')
sharp.show()
plt.imshow(sharp)
plt.show()


# In[10]:


import matplotlib.pyplot as plt
img = Image.open('pic.jpg')
plt.imshow(img)
plt.show()
flip = img.transpose(Image.FLIP_LEFT_RIGHT)
flip.save('D:/image_flip.jpg')
plt.imshow(flip)
plt.show()


# In[8]:


from PIL import Image
import matplotlib.pyplot as plt
im = Image.open('taj.png')
width, height = im.size
im1 = im.crop((280,100,800,600))
im1.show()
plt.imshow(im1)
plt.show()


# In[ ]:




