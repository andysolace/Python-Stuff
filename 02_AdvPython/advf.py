#!/usr/local/bin/python3
# advf.py Python 3

import sys
import inspect
import functools

# TODO: insert your decorator here
def logger(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        line_no = inspect.getouterframes(inspect.currentframe())[1][2]
        print(f'Function was called from line {line_no}.')
        return func
    return wrapper

@logger
def myfunc1(): pass

@logger
def myfunc2(): pass

@logger
def myfunc3(p = 0):
    """ Multiply arg by 2 """
    print(p * 2)

myfunc1()
myfunc2()
myfunc3(42)
myfunc1()

print(myfunc1.__name__)
help(myfunc3)
     