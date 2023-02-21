#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
from PIL import ImageDraw
 
# Open an Image
img = Image.open('car2.png')
 
# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)
 
# Add Text to an image
I1.text((30, 20), "nice ", fill=(300, 200, 100))
 
# Display edited image
img.show()
 
# Save the edited image
img.save("car2.png")


# In[7]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


def generate_empty_image():

    return np.ones(shape=(512,512,3), dtype=np.int16)


# In[9]:


sample_img = generate_empty_image()
plt.imshow(sample_img)


# In[10]:


img = generate_empty_image()
cv2.putText(img=img, text='Hi', org=(150, 250), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(0, 255, 0),thickness=3)

plt.imshow(img)


# In[11]:


img1 = generate_empty_image()

text = "How\nAre\nYou"

y_start = 150

y_increment = 100

for i, line in enumerate(text.split('\n')):
y = y_start + i*y_increment
cv2.putText(img=img1, text=line, org=(150, y), fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX, fontScale=4, color=(255,255,0), 
thickness=3)

plt.imshow(img1)


# In[12]:


import cv2


# In[13]:


path = r'taj.png'


# In[14]:


image = cv2.imread(path)


# In[15]:


window_name = 'Image'


# In[16]:


font = cv2.FONT_HERSHEY_SIMPLEX


# In[17]:


org = (50, 50)


# In[18]:


fontScale = 1


# In[19]:


color = (255, 0, 0)


# In[20]:


thickness = 2


# In[21]:


image = cv2.putText(image, 'OpenCV', org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)


# In[22]:


cv2.imshow(window_name, image) 

