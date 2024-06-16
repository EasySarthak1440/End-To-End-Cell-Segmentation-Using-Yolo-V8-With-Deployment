#!/usr/bin/env python
# coding: utf-8

# In[1]:


import gdown


# In[2]:


import os


# In[3]:


os.chdir("../")


# In[4]:


get_ipython().run_line_magic('pwd', '')


# In[5]:


url = "https://drive.google.com/file/d/1tfuDGpeuB0GBbSuJ_J_OqjKIaKmnrAd3/view?usp=sharing"


# In[6]:


file_id = url.split("/")[-2]
file_id


# In[10]:


# prefix = 'https://drive.google.com/uc?/export=download&id='
# gdown.download(prefix+file_id, "data/cell_data.zip")


# In[9]:


import os
import requests

url = f'https://drive.google.com/uc?export=download&id={file_id}'

# Specify the desired output folder and file name
output_folder = 'data'
output_file = 'cell_data.zip'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Combine the output folder and file name to get the full path
output_path = os.path.join(output_folder, output_file)

# Download the file and save it to the specified location
response = requests.get(url)
with open(output_path, 'wb') as f:
    f.write(response.content)

print(f"File downloaded and saved to: {output_path}")


# In[ ]:




