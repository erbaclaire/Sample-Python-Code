'''
Homework 3 - Problem 1:
Write a function called vectorize(func) that takes a function as its only positional argument and 
returns a new function that calls func multiple times. The new function should accept any number 
of positional arguments. If N arguments are passed to the new function, func is called N times 
with each of the values as a single argument. The new function should return a list of return values
from each invocation of func.
'''

# Cite: Matt Pozsgai and I checked our output from our individual codes against eachother's as a check on our own codes

def vectorize(func):
    def new(*args):
        print(list(map(func, args)))        
    return new

'''
# tests
from math import sqrt
multisqrt = vectorize(sqrt)
multisqrt(4.0, 25.0, 1.0, 10.0)

lamb = vectorize(lambda x: x ** 4)
lamb(8, -2, 4,2, 9, 7)

mult = vectorize(lambda x: x*4)
mult(*[8, -2, 4,2, 9, 7])
mult([8, -2, 4,2, 9, 7]) # only one positional argument

# general case for when function takes more than 1 arg:
def vectorize2(func):
    def new(*args):
        l = []
        for arg in args:
            try:
                l.append(func(*arg)) # will unpack again
            except:
                l.append(func(arg))
        print(l)
    return new

multisqrt2 = vectorize2(sqrt)
multisqrt2(4.0, 25.0, 1.0, 10.0)

pow = vectorize2(pow)
pow((4,2), (3,6), (2, 1))
'''
