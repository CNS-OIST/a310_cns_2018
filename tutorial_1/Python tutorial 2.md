
# Lightning Introduction to Python - part 2

## Data types
### List

List is a mutable data type that can contain elements with different data types.


```python
a = [0, 1, 2, 3, 4, 5]
print(a)
a = list(range(6))
print(a)
```

    [0, 1, 2, 3, 4, 5]
    [0, 1, 2, 3, 4, 5]



```python
a.append(6)     # You can append elements...
print(a)

a.append('J')   # of different types...
print(a)

a.remove(3)     # and remove them, too.
print(a)
```

    [0, 1, 2, 3, 4, 5, 6]
    [0, 1, 2, 3, 4, 5, 6, 'J']
    [0, 1, 2, 4, 5, 6, 'J']



```python
print(3 in a) # Test if it has a particular element.

for x in a: 
    print(x**2)   # Loop around elements in the list.
```

    False
    0
    1
    4
    16
    25
    36



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-19-870b50332837> in <module>()
          2 
          3 for x in a:
    ----> 4     print(x**2)   # Loop around elements in the list.
    

    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'



```python
print(a[3])
print(a[1:5])    # Access a range of elements.
print(a[-1])     # You can also index from the end.
```

    4
    [1, 2, 4, 5]
    J


### Tuple

Tuple is similar to List, but is immutable.


```python
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
```

    False
    (1, 2)
    1 2
    (1, 2)
    1 2


### Dictionary

The dictionary is an incredibly convenient data structure that provides key/value access.


```python
p = {'type': 'pyr', 'rate': 1.0, 'number': 1000}
print(p)
print(p['type'])
print('type' in p)    # Check if the dict has a particular **key**
```

    {'type': 'pyr', 'rate': 1.0, 'number': 1000}
    pyr
    True


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

