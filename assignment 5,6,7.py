#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


ground_cricket_data = {"Chirps/second": [20.0, 16.0, 19.8, 18.4, 17.1, 15.5, 14.7,
                                         15.7, 15.4, 16.3, 15.0, 17.2, 16.0, 17.0,
                                         14.4],
                       "Ground Temperature": [88.6, 71.6, 93.3, 84.3, 80.6, 75.2, 69.7,
                                              71.6, 69.4, 83.3, 79.6, 82.6, 80.6, 83.5,
                                              76.3]}
df = pd.DataFrame(ground_cricket_data)
df.head()


# In[3]:


np.reshape(1,-1)


# In[4]:


x = df['Ground Temperature']
x = x.to_frame()
y = df['Chirps/second']


# In[5]:


linreg = linear_model.LinearRegression()
linreg.fit(x, y)
print('intercept:', linreg.intercept_)
print('coefficient:', linreg.coef_)


# In[6]:


plt.scatter(x, y, color='blue')
plt.plot(x, linreg.predict(x), color='limegreen')


# In[7]:


print('r-squared: ', linreg.score(x, y))


# In[10]:


#Interploate
(18 - linreg.intercept_) / linreg.coef_


# In[11]:


df = pd.read_fwf("brain_body.txt")
df.head()


# In[12]:


x = df['Brain']
x = x.to_frame()
y = df['Body']


# In[13]:


linreg = linear_model.LinearRegression()
linreg.fit(x, y)


# In[14]:


print('intercept:', linreg.intercept_)
print('coefficient:', linreg.coef_)


# In[15]:


plt.scatter(x, y, color='green')
plt.plot(x, linreg.predict(x), color='lightblue', linewidth=2)


# In[16]:


print('r-squared: ', linreg.score(x, y))


# In[17]:


df = pd.read_fwf("salary.txt", header=None, 
                 names=['Sex', 'Rank', 'Year', 'Degree', 'YSdeg', 'Salary'])
feature = ['Sex', 'Rank', 'Year', 'Degree', 'YSdeg']


# In[18]:


df = pd.read_fwf("salary.txt", header=None, 
                 names=['Sex', 'Rank', 'Year', 'Degree', 'YSdeg', 'Salary'])


# In[19]:


feature = ['Sex', 'Rank', 'Year', 'Degree', 'YSdeg']
x = df[feature]
y = df.Salary


# In[20]:


linreg = linear_model.LinearRegression()
linreg.fit(x, y)


# In[21]:


print('Features & Coefficients')
print(list(zip(feature, linreg.coef_)))


# In[22]:


print('Features & Coefficients')
print(list(zip(feature, linreg.coef_)))


# In[23]:


x = df[feature]
y = df.Salary


# In[24]:


linreg = linear_model.LinearRegression()
linreg.fit(x, y)


# In[26]:


print('Features & Coefficients')
print(list(zip(feature, linreg.coef_)))


# In[ ]:


[('Sex', 1241.7924996014231), ('Rank', 5586.1814495214376), ('Year', 482.85976782882136), ('Degree', -1331.6440634059163), ('YSdeg', -128.79057354486233)]
 


# In[ ]:




