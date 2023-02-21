#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2

img = cv2.imread('taj.png')
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# edge_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen_kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
img = cv2.filter2D(grayscale, -1, sharpen_kernel)

# Smooth out image
# blur = cv2.medianBlur(img, 3)
blur = cv2.GaussianBlur(img, (3,3), 0)

cv2.imshow('img',img)
cv2.imwrite('img.png',img)
cv2.imshow('blur',blur)
cv2.waitKey(0)


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


import cv2
import numpy as np
from skimage import io      # Only needed for web grabbing images; use cv2.imread(...) for local images

# Read images
frame = cv2.cvtColor(io.imread('crop.png'), cv2.COLOR_RGB2BGR)
image = cv2.cvtColor(io.imread('nature.jpg'), cv2.COLOR_RGB2BGR)

# Color threshold red frame; single color here, more sophisticated solution would be using cv2.inRange
mask = 255 * np.uint8(np.all(frame == [36, 28, 237], axis=2))

# Find inner contour of frame; get coordinates
contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = min(contours, key=cv2.contourArea)
(x, y, w, h) = cv2.boundingRect(cnt)

# Copy appropriately resized image to frame
frame[y:y+h, x:x+w] = cv2.resize(image, (w, h))

cv2.imshow('frame', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




