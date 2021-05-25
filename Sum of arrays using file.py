#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Sum of array

lst = []
num = int(input("Enter the size of array: "))
print("Enter array elements:")
for i in range(num):
    numbers = int(input())
    lst.append(numbers)
print("Sum:",sum(lst))


# In[2]:


#Sum of array in files
#Sum of Array using Files

lst = []
f = open('file.txt')
text = f.read()
lst = list(map(int,text.split(' ')))
print("Sum:",sum(lst))


# In[ ]:




