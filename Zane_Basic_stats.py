#!/usr/bin/env python
# coding: utf-8

# ## Script to calculate Basic Statistics

# ### Equation for the mean:   $\mu_x = \sum_{i=1}^{N}\frac{x_i}{N}$
# 
# ### Equation for the standard deviation:  $\sigma_x = \sqrt{\sum_{i=1}^{N}\left(x_i - \mu \right)^2}\frac{1}{N-1}$
# 
# 
# **Instructions:**
# 
# **(1) Before you write code, write an algorithm that describes the sequence of steps you will take to compute the mean and standard deviation for your samples.  The algorithm can be written in pseudocode or as an itemized list.***
# 
# **(2) Use 'for' loops to help yourself compute the average and standard deviation.**
# 
# **(3) Use for loops and conditional operators to count the number of samples within $1\sigma$ of the mean.**
# 
# **Note:** It is not acceptable to use the pre-programmed routines for mean and st. dev., e.g. numpy.mean()

# ### Edit this box to write an algorithm for computing the mean and std. deviation.
# 
# ~~~
# 
# #### Mean
# 
# count number of inputs 
#     if number is less than 10, simply just remember the number 
#     if number is more than 10, write this number down 
# add inputs together
# divide by total number of inputs 
#    
# 
# #### Standard Deviation
# 
# count number of inputs 
#     if number is less than 10, simply just remember the number
#     if number is more than 10, write this number down
# add inputs together 
# divide by total number of inputs 
# save the mean as a variable x 
# for each input, subtract input minus mean 
# square these values 
# add squared values together 
# take square root of the total 
# divide by the total number of inputs + 1 
# 
# 
# 
# 
# 
# 
# ~~~

# ### Write your code using instructions in the cells below.

# In[2]:


# Lauren Zane 9/17/21 V. 1


# In[3]:





# In[73]:


# Import the matplotlib module here.  No other modules should be used.
import matplotlib as plt


# In[63]:


# Create a list variable that contains at least 25 elements.  You can create this list any number of ways.  
# This will be your sample.
hw_list = [6,7,8,9,10,11,1,2,3,4,5,60,70,80,90,100,110,109,108,107,106,1,1,1,1,1]


# In[11]:


# Pretend you do not know how long x is; compute it's length, N, without using functions or modules.
get_ipython().run_line_magic('pinfo', 'list')
#length = 26


# In[26]:


# Compute the mean of the elements in list x.
#need sum and division 

hw_list = [6,7,8,9,10,11,1,2,3,4,5,60,70,80,90,100,110,109,108,107,106,1,1,1,1,1]
list_sum = 0

for number in hw_list:
    list_sum = int(number) + list_sum
    
mu = list_sum / len(hw_list)

print(mu)
    
    
    





# In[29]:


# Compute the std deviation, using the mean and the elements in list x.

for number in hw_list:
    sigma = sum([((int(number) - mu)**2/len(hw_list))**0.5])
    

print(sigma)



    


# In[30]:


# Use the 'print' command to report the values of average (mu) and std. dev. (sigma).

print(mu)
print(sigma)


# In[36]:


# Count the number of values that are within +/- 1 std. deviation of the mean.  
# A normal distribution will have approx. 68% of the values within this range.  
# Based on this criteria is the list normally distributed?


mu + sigma


#46.31439973504274

mu - sigma 

#31.45483103418803

#0 values are +/- one std. dev. from the mean, list is not normally distributed




# In[59]:


# Use print() and if statements to report a message about whether the data is normally distributed.

for number in hw_list:
    if int(number) > 46:
        print(int(number))
        
list_of_values_greater_than = [60,70,80,90,100,110,109,108,107,106]

get_ipython().run_line_magic('pinfo', 'list_of_values_greater_than')

#length = 10

for number in hw_list:
    if int(number) < 31:
        print(int(number))
        
list_of_values_less_than = [1,1,1,1,1,5,4,3,2,1,11,10,9,8,7,6]
get_ipython().run_line_magic('pinfo', 'list_of_values_less_than')

#length = 16

26 -(10 +16)
# 0 

0/26

#not normally distributed 



# In[ ]:





# In[98]:


### Use Matplotlb.pyplot to make a histogram of x.

from matplotlib import pyplot as plt
import numpy as np



data_array = np.array([6,7,8,9,10,11,1,2,3,4,5,60,70,80,90,100,110,109,108,107,106,1,1,1,1,1])

plot = plt.hist(data_array)


# ### OCG 593 students, look up an equation for Skewness and write code to compute the skewness. 
# #### Compute the skewness and report whether the sample is normally distributed.

# In[ ]:




