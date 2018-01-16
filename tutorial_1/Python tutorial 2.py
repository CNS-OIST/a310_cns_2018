
# coding: utf-8

# # Lightning Introduction to Python - part 2

# ## Data types
# ### List
# 
# List is a mutable data type that can contain elements with different data types.

# In[16]:


a = [0, 1, 2, 3, 4, 5]
print(a)
a = list(range(6))
print(a)


# In[17]:


a.append(6)     # You can append elements...
print(a)

a.append('J')   # of different types...
print(a)

a.remove(3)     # and remove them, too.
print(a)


# In[19]:


print(3 in a) # Test if it has a particular element.

for x in a: 
    print(x**2)   # Loop around elements in the list.


# In[8]:


print(a[3])
print(a[1:5])    # Access a range of elements.
print(a[-1])     # You can also index from the end.


# ### Tuple
# 
# Tuple is similar to List, but is immutable.

# In[24]:


a = (1, 2)
print(3 in a)       # Test if it has the particular element.

a = 1, 2     # a == ???
print(a)
a, b = 1, 2  # a == ??? We have seen this before.
print(a, b)
      
def f():
    return 1, 2

print(f())     # x==???
x, y = f()  # x==???
print(x, y)


# ### Dictionary
# 
# The dictionary is an incredibly convenient data structure that provides key/value access.

# In[26]:


p = {'type': 'pyr', 'rate': 1.0, 'number': 1000}
print(p)
print(p['type'])
print('type' in p)    # Check if the dict has a particular **key**


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

