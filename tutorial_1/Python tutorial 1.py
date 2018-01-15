
# coding: utf-8

# # Lightning Introduction to Python - part 1

# ## Language basics 
# ### Variables
# 
# Python is a dynamic language, and variables can be created and assigned without declaration.

# In[1]:


a = 2    # define a
print(a)


# In[2]:


b = a
a *= b   # a==???
print(a, b)


# In[3]:


del(a, b)
print(a, b)


# ### Code blocks (Indents)
# 
# In Python, code blocks are defined by fixed indents followed by `:`. There is no rule about how many spaces/tabs should be used, but indenting should be consistent within a block.
# 
# For example, indenting is required in conditionals, 

# In[4]:


if True:
    print("True.")
    print("To be precise, that was True.")
else:
    print("False.")


# in loops,

# In[5]:


for x in range(6):
    print(x)


# and when you define functions,

# In[6]:


def f(x):
    y = x + 1
    return y

print(f(2))


# ### Flow control
# 
# #### Conditionals

# In[7]:


simulator = "NEURON"
language = "Python"

if simulator=="NEURON" and language=="Python":
    print("This is a NEURON simulation written in Python.")

if simulator!="NEURON":
    print("Not a NEURON simulation.")

if not language=="Python":
    print("Not written in Python.")


# #### Loops

# In[8]:


j = 0
for i in range(10):
    j += i
    print(i, j)


# In[9]:


i, j = 0, 0
while i<10:
    i, j = i+1, i+j+1
    print(i, j)


# In[10]:


j = 0
for x in ["a", "b", "c", "d"]:
    print("For condition", x, ", variable = ", j)
    j += 1


# In[11]:


for j, x in enumerate(["a", "b", "c", "d"]):
    print("For condition", x, ", variable = ", j)


# ### Defining functions and how to call them

# In[12]:


def f(x, y):
    return x**y


# In[13]:


print(f(2,3))


# Default values for inputs can be specified:

# In[14]:


def f(x, y=2):
    return x**y

print(f(3))


# It is recommended to make a note about how to use the function

# In[15]:


def f(x, y=2):
    """ computes the y-th power of x."""
    return x**y


# In[16]:


help(f)


# ## Modules and namespaces
# 
# Every module in Python comes with its own namespace, and functions in a module need to be called with the namespace.

# In[3]:


import numpy

a = numpy.sqrt([1, 2, 3, 4])
print(a)


# In fact, every file is considered as a module with its own namespace. For example, let's say you have mymodule.py as

# In[5]:


"""
Here you write a module help. Try help(mymodule) after importing.
"""

def func1():
    """ Help for func1. """
    print("You called func1!")


# In[6]:


import mymodule
mymodule.func1()


# However, if the namespace gets too long, you can use two alternatives: First, you can use an alias,

# In[7]:


import numpy.random as r
print(r.rand(10))


# Second, you can directly import functions,

# In[10]:


from numpy.random import rand
print(rand(10))


# You can import **all** symbols as the following, but use this method **only when you know what you are doing!**

# In[11]:


from mymodule import *
func1()

