#!/usr/bin/env python
# coding: utf-8

# In[4]:


N = int(input("Enter N"))

print("Enter the N numbers you want to insert (one by one):")
nums = []
for i in range(1, N + 1):
    x = int(input(f"Enter number #{i}: "))
    nums.append(x)

X = int(input("Enter X to search: "))

try:
    index = nums.index(X) + 1
except ValueError:
    index = -1

print(index)


# In[ ]:




