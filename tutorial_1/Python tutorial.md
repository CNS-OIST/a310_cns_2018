
# Lightning Introduction to Python

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

    <ipython-input-11-7420b469ce9e> in <module>()
          1 del(a, b)
    ----> 2 print(a, b)
    

    NameError: name 'a' is not defined


## Code blocks (Indents)

In Python, code blocks are defined by fixed indents followed by `:`.
