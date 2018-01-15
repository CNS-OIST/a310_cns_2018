
# Lightning Introduction to Python - part 1

## Language basics 
### Variables

Python is a dynamic language, and variables can be created and assigned without declaration.


```python
a = 2    # define a
print(a)
```

    2



```python
b = a
a *= b   # a==???
print(a, b)
```

    4 2



```python
del(a, b)
print(a, b)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-7420b469ce9e> in <module>()
          1 del(a, b)
    ----> 2 print(a, b)
    

    NameError: name 'a' is not defined


### Code blocks (Indents)

In Python, code blocks are defined by fixed indents followed by `:`. There is no rule about how many spaces/tabs should be used, but indenting should be consistent within a block.

For example, indenting is required in conditionals, 


```python
if True:
    print("True.")
    print("To be precise, that was True.")
else:
    print("False.")

```

    True.
    To be precise, that was True.


in loops,


```python
for x in range(6):
    print(x)
```

    0
    1
    2
    3
    4
    5


and when you define functions,


```python
def f(x):
    y = x + 1
    return y

print(f(2))
```

    3


### Flow control

#### Conditionals


```python
simulator = "NEURON"
language = "Python"

if simulator=="NEURON" and language=="Python":
    print("This is a NEURON simulation written in Python.")

if simulator!="NEURON":
    print("Not a NEURON simulation.")

if not language=="Python":
    print("Not written in Python.")

```

    This is a NEURON simulation written in Python.


#### Loops


```python
j = 0
for i in range(10):
    j += i
    print(i, j)
```

    0 0
    1 1
    2 3
    3 6
    4 10
    5 15
    6 21
    7 28
    8 36
    9 45



```python
i, j = 0, 0
while i<10:
    i, j = i+1, i+j+1
    print(i, j)
```

    1 1
    2 3
    3 6
    4 10
    5 15
    6 21
    7 28
    8 36
    9 45
    10 55



```python
j = 0
for x in ["a", "b", "c", "d"]:
    print("For condition", x, ", variable = ", j)
    j += 1

```

    For condition a , variable =  0
    For condition b , variable =  1
    For condition c , variable =  2
    For condition d , variable =  3



```python
for j, x in enumerate(["a", "b", "c", "d"]):
    print("For condition", x, ", variable = ", j)

```

    For condition a , variable =  0
    For condition b , variable =  1
    For condition c , variable =  2
    For condition d , variable =  3


### Defining functions and how to call them


```python
def f(x, y):
    return x**y
```


```python
print(f(2,3))
```

    8


Default values for inputs can be specified:


```python
def f(x, y=2):
    return x**y

print(f(3))
```

    9


It is recommended to make a note about how to use the function


```python
def f(x, y=2):
    """ computes the y-th power of x."""
    return x**y
```


```python
help(f)
```

    Help on function f in module __main__:
    
    f(x, y=2)
        computes the y-th power of x.
    


## Modules and namespaces

Every module in Python comes with its own namespace, and functions in a module need to be called with the namespace.


```python
import numpy

a = numpy.sqrt([1, 2, 3, 4])
print(a)
```

    [ 1.          1.41421356  1.73205081  2.        ]


In fact, every file is considered as a module with its own namespace. For example, let's say you have mymodule.py as


```python
"""
Here you write a module help. Try help(mymodule) after importing.
"""

def func1():
    """ Help for func1. """
    print("You called func1!")
```


```python
import mymodule
mymodule.func1()
```

    You called func1!


However, if the namespace gets too long, you can use two alternatives: First, you can use an alias,


```python
import numpy.random as r
print(r.rand(10))
```

    [ 0.40809877  0.73432772  0.57399723  0.3957452   0.39514387  0.15250764
      0.82284366  0.59357915  0.27205398  0.01087061]


Second, you can directly import functions,


```python
from numpy.random import rand
print(rand(10))
```

    [ 0.93330894  0.81071528  0.15239019  0.88832229  0.47910904  0.40924464
      0.80845977  0.64283412  0.31242843  0.34156272]


You can import **all** symbols as the following, but use this method **only when you know what you are doing!**


```python
from mymodule import *
func1()
```

    You called func1!

