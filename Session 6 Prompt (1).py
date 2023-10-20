#!/usr/bin/env python
# coding: utf-8

# **Have to import math first**

# In[1]:


# Function to calculate sin(x)
import math


# Next step is to create functions that return **sin(x)** and **cos(x)**

# *sin(x) function:*

# In[2]:


def calculate_sin(x):
    return math.sin(x)


# *cos(x) function:*

# In[3]:


# Function to calculate cos(x)
def calculate_cos(x):
    return math.cos(x)


# Now we need to create a cell that tabulates **sin(x)** and **cos(x)** to our specifed range of **x** values. Can't forget to import numpy first. 

# In[4]:


import numpy as np

# Create an array of x values
x_values = np.linspace(0, 2*np.pi, 1000)

# Calculate sin(x) and cos(x) for each x
sin_values = [calculate_sin(x) for x in x_values]
cos_values = [calculate_cos(x) for x in x_values]


# Finally, print the first 10 results of the function above, and make it look a little nicer by not having as many decimals. I do this by using the **:.3f** format function. I also print a little header for aesthetics.  

# In[5]:


print("  x     | sin(x)| cos(x)")
print("--------+-------+--------")
for i in range(10):
    print(f"{x_values[i]:.3f} \t| {sin_values[i]:.3f} | {cos_values[i]:.3f}")
    

