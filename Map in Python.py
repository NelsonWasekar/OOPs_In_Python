#!/usr/bin/env python
# coding: utf-8

# ### Map in Python is a function that works as an iterator to return a result after applying a function to every item of an iterable (tuple, lists, etc.). 
# 
# ### It is used when you want to apply a single transformation function to all the iterable elements. The iterable and function are passed as arguments to the map in Python

# In[1]:


## The syntax of the Python map() function is:


# ### map(function, iterables)

# In[2]:


# In the above syntax:


# function: It is the transformation function through which all the items of the iterable will be passed.

# iterables: It is the iterable (sequence, collection like list or tuple) that you want to map


# In[ ]:


#  https://www.simplilearn.com/tutorials/python-tutorial/map-in-python#:~:text=Map%20in%20Python%20is%20a,to%20the%20map%20in%20Python.


# In[3]:


def mul(i):
    return i * i


# Using the map function
x = map(mul, (3, 5, 7, 11, 13))


print(x)
print(list(x))


# In[12]:


li1 = (1,2,3,4)

y = map(max, li1)    # max is an bult in function

# h = list(y)
print(y)


# In[10]:


list(map(min, [1,2,3,4], [0,10,0,10]))

#[0,2,0,4]


# In[13]:


list(map(max, [1,2,3,4], [10,100,765,5262]))


# In[ ]:




