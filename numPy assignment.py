#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.Create a null vector of size 10 but the fifth value which is 1.
import numpy as np
a=np.zeros(10)
a[4]=1
print(a)


# In[5]:


#2Create a vector with values ranging from 10 to 49.
b=np.arange(10,50)
print(b)


# In[6]:


#3. Create a 3x3 matrix with values ranging from 0 to 8
c=np.arange(0,9).reshape(3,3)
print(c)


# In[7]:


#4. Find indices of non-zero elements from [1,2,0,0,4,0]
d=np.array([1,2,0,0,4,0])
non_zero_indences=np.nonzero(d)
print(non_zero_indences)


# In[17]:


#5. Create a 10x10 array with random values and find the minimum and maximum values.
e=np.random.randint(low=0,high=100,size=(10,10))
min_value=np.min(e)
max_value=np.max(e)
print(e)
print("min value is",min_value)
print("max value is ",max_value)


# In[18]:


#6.Create a random vector of size 30 and find the mean value.
f=np.random.randint(low=0,high=50,size=(30))
mean_value=np.mean(f)
print(f)
print("mean value is", mean_value)


# In[ ]:




