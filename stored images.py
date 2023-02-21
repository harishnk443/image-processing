#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from os import listdir
folder_dir = "D:/hari images"
for images in os.listdir(folder_dir):
    if (images.endswith(".jfif") or images.endswith(".png")or images.endswith(".jpg") or images.endswith(".webp")):
        print(images)


# In[2]:


# importing the library
import os
 
# giving directory name
dirname = 'D:/hari images'
 
# giving file extension
ext = ('.exe', 'jpg')
 
# iterating over all files
for files in os.listdir(dirname):
    if files.endswith(ext):
        print(files)  # printing file name of desired extension
    else:
        continue


# In[3]:


import cv2
import os
import glob
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
 
img_dir = "D:/hari images"  
data_path = os.path.join(img_dir,'*')
files = glob.glob(data_path)
data = []
for f1 in files:
    img = cv2.imread(f1)
    data.append(img)
    plt.figure()
    plt.imshow(img)


# In[4]:


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


# In[5]:


from PIL import Image
from PIL import ImageFilter
import os

def main():
# path of the folder containing the raw images
inPath ="D:\\background"

# path of the folder that will contain the modified image
outPath ="D:\\test"

for imagePath in os.listdir(inPath):
# imagePath contains name of the image
inputPath = os.path.join(inPath, imagePath)

# inputPath contains the full directory name
img = Image.open(inputPath)

fullOutPath = os.path.join(outPath, 'invert_'+imagePath)
# fullOutPath contains the path of the output
# image that needs to be generated
img.rotate(90).save(fullOutPath)

print(fullOutPath)

# Driver Function
if __name__ == '__main__':
main()


# In[6]:


def show_image_contour(image, contours):
    plt.figure()
    for n, contour in enumerate(contours):
        plt.plot(contour[:, 1], contour[:, 0], linewidth=3)
        plt.imshow(image, interpolation='nearest', cmap='gray_r')
        plt.title('contours')
        plt.axis('off')


# In[7]:


from skimage import measure, data
horse_image = data.horse()
contours = measure.find_contours(horse_image, level=0.8)
show_image_contour(horse_image, contours)


# In[9]:


import cv2
import matplotlib.pyplot as plt
def show_image_contour(image, contours):
    from skimage.segmentation import slic
    from skimage.color import label2rgb
    face_image = plt.imread('cat.png')
    segments = slic(face_image, n_segments=400)
    segmented_image = label2rgb(segments, face_image, kind='avg')
plot_comparison(face_image, segmented_image, 'segmented image, 400 superpixels' )

