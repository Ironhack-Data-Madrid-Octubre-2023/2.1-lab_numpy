#!/usr/bin/env python
# coding: utf-8

# #1. Import the NUMPY package under the name np.

# In[1]:


import numpy as np


# In[2]:


#2. Print the NUMPY version and the configuration.
print(np.__version__)


# In[3]:


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
#a = np.random.random(30)
#a = np.random.random((2,3,5))
a = np.random.random((2,3,5))
a


# In[4]:


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.random.random((5,2,3))
b


# In[5]:


#7. Do a and b have the same size? How do you prove that in Python code?
#print(a.size)
#print(b.size)


# In[6]:


#8. Are you able to add a and b? Why or why not?
#a+b(sumarlo como tal no ya que el numero de filas no coincide con el numero de columnas)


# In[7]:


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array).
#Assign the transposed array to varialbe "c".
c= b.reshape((2,3,5))


# In[8]:


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
d=a+c # Ahora funciona por que coincide la cantidad de filas y columnas



# In[9]:


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
#print(a)
#print("---------------------------------------------------------")
#print(d)


# In[10]:


#12. Multiply a and c. Assign the result to e.
e = a*c


# In[11]:


#13. Does e equal to a? Why or why not?
# no se si lo estare haciendo mal por que no veo ninguna igualdad entre A y E


# In[53]:


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_mean=np.mean(d)
d_max = np.max(d)
d_min = np.min(d)


# In[51]:


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f = np.empty((2,3,5))
f


# #16 Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
# If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
# If a value equals to d_mean, assign 50 to the corresponding value in f.
# Assign 0 to the corresponding value(s) in f for d_min in d.
# Assign 100 to the corresponding value(s) in f for d_max in d.
# In the end, f should have only the following values: 0, 25, 50, 75, and 100.
# Note: you don't have to use Numpy in this question.""

# In[55]:


#un compañero me explico esta manera de hacerlo.
f[(d > d_min) & (d < d_mean)] = 25
f[(d > d_mean) & (d < d_max)] = 75
f[(d == d_mean)] = 50
f[(d == d_min)] = 0
f[(d == d_max)] = 100
print(f)
print(d)


# In[84]:


f = np.where((d > d_min) & (d < d_mean), 25, f)
f = np.where(d == d_mean, 50, f)
f = np.where((d > d_mean) & (d < d_max), 75, f)
f = np.where(d == d_min, 0, f)
f = np.where(d == d_max, 100, f)
f


# #18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
# ("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
# array([[[ 'D',  'D',  'D',  'B',  'D'],
#         [ 'D',  'D',  'B',  'B',  'B'],
#         [ 'D',  'B',  'D',  'D',  'D']],
# 
#        [[ 'B',  'B',  'B',  'B',  'E'],
#         [ 'D',  'D',  'D',  'D',  'D'],
#         [ 'B',  'D',   'A',  'D', 'D']]])
# Again, you don't need Numpy in this question.

# In[87]:


f = np.where((d > d_min) & (d < d_mean), "A", f)
f = np.where(d == d_mean, "B", f)
f = np.where((d > d_mean) & (d < d_max), "C", f)
f = np.where(d == d_min, "D", f)
f = np.where(d == d_max, "F", f)
f


# In[ ]:




