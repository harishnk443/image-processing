#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import cv2
  
# Open the image.
img = cv2.imread('cat.png')
  
# Load the mask.
mask = cv2.imread('black.png', 0)
  
# Inpaint.
dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)
  
# Write the output.
cv2.imwrite('cat_inpainted.png', dst)

cv2.imshow('cat_inpainted.png', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




