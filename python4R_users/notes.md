# Functions, Methods, and Libraries

Calling functions
- R and Python functions work the same
- python: functions & methods

Methods vs Functions
- python is objected oriented
 	- attributes
	- methods
- methods are functions that an **object can call** on itself
- functions are **called on an object**
- you pass objects into functions

Ex: l = [0, 1, 2, 3, 4]
len(1) #call a function
l.len() #not a method

Recall you passed "L", a list, to the function len(), rather than calling the method len() on "L.

Periods have a special meaning in Python!
append to list

l = [1, "2", True]
l.append("appended value")


Note the syntax, you call the append() method on the list "L" using the dot notation

### Update a dictionary

For dictionaries, you can call the update() method, note the dot notation to call the method

d = {"int_value": 3, "bool_value": False, "str_value": "hello"}

d.update({"str_value": "new value", "new_key": "new_value"})
print(d)

### Libraries

Libraries provide more functionality
- arrays and dfs are not built into Python
- arrays and matrices come from *numpy*
- dfs come from *pandas*

When loadings a library in R, you can use any functions from the library directly....
not so much the case in python

import bumpy
arr = numpy.loadtxt("my_file.csv", delimiter = ",")

import numpy as np #this is common practice
arr = np.loadtxt("my_file.csv", delimiter = ",")

Pandas works the same!