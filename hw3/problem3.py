'''
Homework 3 - Problem 3:
Write own version of lru_cache function

See HW3 PDF for specific specifications
'''

# Cite: Matt Pozsgai and I checked our output from our individual codes againt eachother's as as check on our own codes

import collections
import urllib.request

def lru_cache(func, maxsize = 128):
    cache = collections.OrderedDict() # cite: https://stackoverflow.com/questions/10058140/accessing-items-in-a-ordereddict; popitem for regular dictionary wasn't doing LIFO so switched to this. 
    CacheInfo = collections.namedtuple('CacheInfo', ['hits', 'misses', 'maxsize', 'currsize']) # cite: https://docs.python.org/3/library/collections.html#collections.namedtuple
    hit_counts = CacheInfo(0, 0, maxsize, 0)
    def inner(*args, **kwargs):
        nonlocal hit_counts
        arg = str(args) + str(kwargs)
        if arg not in cache: # if arg is not in the cache add it - if cache is full then pop out first and add the arg
            if len(cache) == maxsize:
                cache.pop(list(cache.items())[0][0]) # pops out the first entry of the ordered dict
                cache[arg] = func(*args, **kwargs)
            else:
                cache[arg] = func(*args, **kwargs)
            hit_counts = hit_counts._replace(misses = hit_counts.misses + 1, currsize = len(cache))
            return cache[arg] # arg is now added to cache so can just get from cache instead of calling function again - saves computing time
        else: # if arg is in the cache its a hit and rearrange cache so hit is now at end
            cache[arg] = cache.pop(arg)
            hit_counts = hit_counts._replace(hits = hit_counts.hits + 1, currsize = len(cache))
            return cache[arg]
    def cache_info():
        print(hit_counts)    
    inner.cache_info = cache_info
    return inner

'''
# test1
def get_pep(num):
    "Retrieve text of a Python Enhancement Proposal"
    resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except urllib.error.HTTPError:
        return 'Not Found'

get_pep = lru_cache(get_pep, maxsize=6)
for n in 8, 290, 308, 320,8, 218,320, 279, 289, 320, 9991:
    pep = get_pep(n)
    print(n, len(pep))
    
get_pep.cache_info()
get_pep(11)
get_pep.cache_info()
get_pep(320)
get_pep.cache_info()

# test2
get_pow = lru_cache(pow, maxsize=10)
for n in (3, 8), (10,1), (10, 1), (12, 1), (2, 1):
    pow = get_pow(*n)
    print(pow)
    
get_pow.cache_info()

# test3
get_n = lru_cache(lambda x: x*1, maxsize=5)
for n in 8, 9, 10, 11, 12, 8, 9, 10, 11, 72:
    _n = get_n(n)
    print(_n)
    
get_n.cache_info()

# test4
from math import sqrt
test = lru_cache(sqrt, maxsize = 5)
for n in 22, 16, 256, 33, 21, 144, 16, 22:
    t = test(n)
    print(t)
    
test.cache_info()
'''
