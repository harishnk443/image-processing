#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('merry2.jpg', -1)
cv2.imshow('merry2',img)

color = ('b','g','r')
for channel,col in enumerate(color):
    histr = cv2.calcHist([img],[channel],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.title('Histogram for color scale picture')
plt.show()

while True:
    k = cv2.waitKey(0) & 0xFF    
    if k == 27: break              
cv2.destroyAllWindows()


# In[ ]:




