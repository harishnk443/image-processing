#!/usr/bin/env python
# coding: utf-8

# In[3]:


#import necessary packages
import cv2
import imageio
import os
import glob
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)
 
#Set the path where images are stored
img_dir = "D:/hari images/" # Enter Directory of all images  
data_path = os.path.join(img_dir,'*')
files = glob.glob(data_path)
data = []
for f1 in files:
    img = plt.imread(f1)
    data.append(img)
    #image_resized=cv2.resize(img,(200,200))
    plt.figure()
    plt.title('Original Image')
    plt.imshow(img)
    #plt.show()
    #plt.imshow(image_resized)
    plt.show()
    #fig = plt.figure()
    #fig.set_size_inches(5, 5)
for f1 in files:
    img = plt.imread(f1)
    data.append(img)
    image_resized=cv2.resize(img,(200,200))
    plt.figure()
    plt.title('Resized Image')
    #plt.imshow(img)
    #plt.show()
    plt.imshow(image_resized)
    plt.show()


# In[ ]:




