#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
from PIL import ImageFilter
import os


# In[14]:


def main():
    inPath ="D:\hari images" 
    outPath ="D:\hari2"
    
    for imagePath in os.listdir(inPath):
        inputPath = os.path.join(inPath, imagePath)
        img = Image.open(inputPath)
        fulloutPath = os.path.join(outPath, 'invert_'+imagePath)
        img.rotate(90).save(fulloutPath)
        print(fulloutPath)
        


# In[15]:


if __name__ == '__main__':
    main()


# In[19]:


from PIL import Image
import os


# In[20]:


os.getcwd()


# In[21]:


image1 = Image.open("car.webp")
image1


# In[22]:


image1.show()


# In[23]:


image1.save("pic.jpg")


# In[24]:


os.listdir()


# In[45]:


for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        print(fn, "&", fext)


# In[27]:


for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        print(fn, "&", fext)


# In[44]:


for f in os.listdir("."):
    if f.endswith(".jpg"):
        print(f)


# In[30]:


for f in os.listdir("."):
    if f.endswith(".jpg"):
        print(f)


# In[31]:


os.mkdir('NewExtnsn')


# In[32]:


for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.save("NewExtnsn/{}.pdf".format(fn))


# In[33]:


os.makedirs('resize//small')
os.makedirs('resize//tiny')


# In[34]:


size_small = (600,600) # small images of 600 X 600 pixels
size_tiny = (200,200)  # tiny images of 200 X 200 pixels
for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.thumbnail(size_small)
        i.save("resize/small/{}_small{}".format(fn, fext))
        i.thumbnail(size_tiny)
        i.save("resize/tiny/{}_tiny{}".format(fn, fext))


# In[36]:


image2 = Image.open("merry.jpg")
image2 = image2.convert(mode='L')
image2


# In[37]:


os.mkdir('b&w')


# In[38]:


for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        im = i.convert(mode = 'L')
        im.save("b&w/{}_bw.{}".format(fn, fext))


# In[51]:


image3 = Image.open("sea.jfif")
image3.rotate(55).save("image3.jpg")
Image3 = Image.open("image3.jpg")


# In[52]:


Image3


# In[41]:


os.mkdir('rotate')


# In[42]:


for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, text = os.path.splitext(f)
        im = i.rotate(90)
        im.save("rotate/{}_rot.{}".format(fn, fext))


# In[ ]:




