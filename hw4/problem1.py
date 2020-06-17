'''
Homework 4 - Problem 1:
In JavaScript, the Array datatype (somewhat equivalent to Python's list) has a
number of methods which list in Python does not have. For this problem, you are to
write an implementation of MutableSequence that provides some of these methods.
Specifications
The class should be named ESArray

It should inherit from the MutableSequence abstract base class in the
collections.abc module.

The join method should accept a string, s as its only argument (other than self)
and return a string that results from joining each item in the list by the string s.

The every method tests whether all items in the list pass a test implemented by a
provided function.

The for_each method executes a provided function function once for each item
in the list.

The flatten method returns a new ESArray with all list-like items in the original
list flattened. That is, calling flatten() on a nested list returns a single list with
all items appearing the their original order but with no nesting.
'''

# Checked homework with Matt Pozsgai
from collections.abc import MutableSequence
from functools import reduce

class ESArray(MutableSequence):

    def __init__(self, l):
        self.l = l

    # MutableSequence abstract methods - allows us to use mixed methods, as well
    def __len__(self):
       return len(self.l)

    def __getitem__(self, position):
        return self.l[position]

    def __setitem__(self, position, value):
        self.l[position] = value

    def __delitem__(self, position):
        del self.l[position]

    def insert(self, position, value):
        self.l.insert(position, value)

    # New functions
    def join(self, s):
        return reduce(lambda x,y: str(x) + s + str(y), self.l)

    def every(self, func):
        return True if len(list(filter(func, self.l)))==len(self.l) else False

    def for_each(self, func):
        for x in self.l:
            func(x)

    def flatten(self): # recursions ftw!
        result = ESArray([])
        for x in self.l:
            if isinstance(x, list): # I do list here and not Iterable because I don't believe we want to flatten dictionaries, strings, or other iterables except lists
                for i in ESArray(x).flatten():
                    result.append(i) # can use this on ESArray because of mixed methods
            else:
                result.append(x)
        return result
                
    def __repr__(self):
        return "{}".format(self.l)

'''
if __name__ == '__main__':

    x = ESArray([1, -3, 10, 5])
    print(x.join('**'))
    print(type(x.join('**')))
    print(x.every(lambda v: v > 0))
    print(x.every(lambda v: isinstance(v, int)))
    x.for_each(print)
    print(x.flatten())

    y = ESArray([[3, 4], [5], 6, [7, [8, [9, 10]]]])
    print(y.join('**'))
    #print(y.every(lambda v: v > 0))
    print(y.every(lambda v: isinstance(v, int)))
    y.for_each(print)
    print(y.flatten())
    print(type(y.flatten()))
    print(y.flatten().for_each(lambda v: v**2))
    print(len(y.flatten()))
    print(type(y))
    print(y[1])
    y[1] = 17
    print(y)
    del y[1]
    print(y)
    y.insert(1, 17)
    print(y)
    
    z = ESArray([[[['a',(1,3)], 66] , dict(h='Tyler'), 'hello'], ['m', 'n', 67, [14, 'cat']]])
    print(z.join('    '))
    print(z.every(lambda v: isinstance(v, (list))))
    print(z.every(lambda v: isinstance(v, (dict))))
    print(z.for_each(lambda v: v[1]))
    print(z.flatten())
'''

    
