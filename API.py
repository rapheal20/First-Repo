#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests as rq


# In[2]:


url2 ="https://data.cityofchicago.org/resource/ydr8-5enu.json"


# In[11]:


data = rq.get(url2)
json_data = data.json()
data_frame = pd.DataFrame(json_data)
data_frame.columns
data_frame.dropna(axis = 1)
data2 = data_frame['permit_type'].unique()
for i in data2:
    _data = data_frame[data_frame == i]
    _data.to_excel(i.split('/')[0]+'.xlsx')


# In[ ]:




