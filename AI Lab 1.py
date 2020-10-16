#!/usr/bin/env python
# coding: utf-8

# # Loops

# **While**

# In[3]:


x = 10
i = 0

while i<x:
    print("Inside", i)
    i+=1
    
print("Outside", i)


# In[6]:


x = input("Enter Value ")
x


# In[7]:


print("Name "+ x)


# In[9]:


print("Name "+ str(i))


# In[15]:


x = 10
i = 0

while i<x:
    print(i, end=' ')
    print("Even ") if i%2 == 0 else print("Odd")
    i+=1
    
print("Outside", i)


# In[16]:


for i in range(1, 10):
    print(i)


# In[18]:


s = "Ali Ahmad"
for i in s:
    print(i)


# In[21]:


l = list(s)
l


# In[23]:


for i in l:
    print(i)


# In[24]:


l = [10, 8, 'Ali']
for i in l:
    print(i)


# In[25]:


dic = {'Name': 'Ali', 'Age': 30, 'Course': 'AI'}
dic


# In[28]:


for key, value in dic.items():
    print(key, '\t', value)


# In[29]:


for i in dic.keys():
    print(i)


# In[31]:


for i in dic.keys():
    print(dic[i])


# In[32]:


for i in dic.values():
    print(i)


# In[35]:


for i in dic:
    print(i)


# In[41]:


for i in dic.items():
    print(i)


# In[ ]:




