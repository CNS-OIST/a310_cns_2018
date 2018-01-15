
# coding: utf-8

# # Lightning Introduction to Python

# ## Language basics 
# ### Variables
# 
# Python is a dynamic language, and variables can be created and assigned without declaration.

# In[8]:


a = 2    # define a
print(a)


# In[10]:


b = a
a *= b   # a==???
print(a, b)


# In[11]:


del(a, b)
print(a, b)


# ## Code blocks (Indents)
# 
# In Python, code blocks are defined by fixed indents followed by `:`.
