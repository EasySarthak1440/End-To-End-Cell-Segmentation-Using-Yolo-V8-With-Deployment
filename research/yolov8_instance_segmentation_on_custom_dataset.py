#!/usr/bin/env python
# coding: utf-8

# ## Before you start
# 
# Let's make sure that we have access to GPU. We can use `nvidia-smi` command to do that. In case of any problems navigate to `Edit` -> `Notebook settings` -> `Hardware accelerator`, set it to `GPU`, and then click `Save`.

# In[1]:


get_ipython().system('nvidia-smi')


# In[2]:


import os
HOME = os.getcwd()
print(HOME)


# ## Install YOLOv8
# 
# ⚠️ YOLOv8 is still under heavy development. Breaking changes are being introduced almost weekly. We strive to make our YOLOv8 notebooks work with the latest version of the library. Last tests took place on **12.02.2023** with version **YOLOv8.0.28**.
# 
# If you notice that our notebook behaves incorrectly - especially if you experience errors that prevent you from going through the tutorial - don't hesitate! Let us know and open an [issue](https://github.com/roboflow/notebooks/issues) on the Roboflow Notebooks repository.
# 
# YOLOv8 can be installed in two ways - from the source and via pip. This is because it is the first iteration of YOLO to have an official package.

# In[3]:


# Pip install method (recommended)

get_ipython().system('pip install ultralytics==8.0.28')

from IPython import display
display.clear_output()

import ultralytics
ultralytics.checks()


# In[4]:


# Git clone method (for development)

# %cd {HOME}
# !git clone github.com/ultralytics/ultralytics
# %cd {HOME}/ultralytics
# !pip install -qe ultralytics

# from IPython import display
# display.clear_output()

# import ultralytics
# ultralytics.checks()


# In[5]:


from ultralytics import YOLO

from IPython.display import display, Image


# ## CLI Basics

# If you want to train, validate or run inference on models and don't need to make any modifications to the code, using YOLO command line interface is the easiest way to get started. Read more about CLI in [Ultralytics YOLO Docs](https://v8docs.ultralytics.com/cli/).
# 
# ```
# yolo task=detect    mode=train    model=yolov8n.yaml      args...
#           classify       predict        yolov8n-cls.yaml  args...
#           segment        val            yolov8n-seg.yaml  args...
#                          export         yolov8n.pt        format=onnx  args...
# ```

# ## Inference with Pre-trained COCO Model

# ### 💻 CLI

# `yolo mode=predict` runs YOLOv8 inference on a variety of sources, downloading models automatically from the latest YOLOv8 release, and saving results to `runs/predict`.

# In[6]:


get_ipython().run_line_magic('cd', '{HOME}')
get_ipython().system("yolo task=segment mode=predict model=yolov8s-seg.pt conf=0.25 source='https://media.roboflow.com/notebooks/examples/dog.jpeg' save=true")


# In[7]:


get_ipython().run_line_magic('cd', '{HOME}')
Image(filename='runs/segment/predict/dog.jpeg', height=600)


# ### 🐍 Python SDK
# 
# The simplest way of simply using YOLOv8 directly in a Python environment.

# In[8]:


model = YOLO(f'{HOME}/yolov8s-seg.pt')
results = model.predict(source='https://media.roboflow.com/notebooks/examples/dog.jpeg', conf=0.25)


# In[9]:


results[0].boxes.xyxy


# In[10]:


results[0].boxes.conf


# In[11]:


results[0].boxes.cls


# In[12]:


results[0].masks.masks


# ## Roboflow Universe
# 
# Need data for your project? Before spending time on annotating, check out Roboflow Universe, a repository of more than 110,000 open-source datasets that you can use in your projects. You'll find datasets containing everything from annotated cracks in concrete to plant images with disease annotations.
# 
# 
# [![Roboflow Universe](https://ik.imagekit.io/roboflow/notebooks/template/uni-banner-frame.png?ik-sdk-version=javascript-1.4.3&updatedAt=1672878480290)](https://universe.roboflow.com/)
# 
# 

# In[13]:


from google.colab import drive
drive.mount('/content/drive')


# In[14]:


ROOT_PATH = "/content/drive/MyDrive/Yolov8-seg"


# In[15]:


get_ipython().system('pwd')


# In[16]:


get_ipython().run_line_magic('cd', '"/content/drive/MyDrive/Yolov8-seg"')


# In[17]:


get_ipython().system('pwd')


# In[18]:


get_ipython().system('ls')


# ## Custom Training

# In[19]:


get_ipython().system('yolo task=segment mode=train model=yolov8s-seg.pt data=data.yaml epochs=10 imgsz=640 save=true')


# In[20]:


get_ipython().system('ls runs/segment/train/')


# In[21]:


Image(filename=f'runs/segment/train/confusion_matrix.png', width=600)


# In[22]:


Image(filename=f'runs/segment/train/results.png', width=600)


# In[23]:


Image(filename=f'runs/segment/train/val_batch0_pred.jpg', width=600)


# ## Validate Custom Model

# In[24]:


get_ipython().system('yolo task=segment mode=val model=runs/segment/train/weights/best.pt data=data.yaml')


# ## Inference with Custom Model

# In[25]:


get_ipython().system('yolo task=segment mode=predict model=runs/segment/train/weights/best.pt conf=0.25 source=cell_data/test/images save=true')


# In[26]:


import glob
from IPython.display import Image, display

for image_path in glob.glob(f'runs/segment/predict/*.jpg')[:3]:
      display(Image(filename=image_path, height=600))
      print("\n")


# ## 🏆 Congratulations
# 
# 
# ### Convert data formats
# 
# Roboflow provides free utilities to convert data between dozens of popular computer vision formats. Check out [Roboflow Formats](https://roboflow.com/formats) to find tutorials on how to convert data between formats in a few clicks.
# 
# 

# In[ ]:




