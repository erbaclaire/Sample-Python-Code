'''
Homework 5 - Problem 1:
Rewrite lru_cache (from Homework 3, Problem 2) to be a parameterized decorator that takes max_size as an argument.
'''

# Checked with Matt Pozsgai

from collections import OrderedDict, namedtuple

def lru_cache(maxsize=128):
    def outer(func):
        # OrderedDict is a LIFO of key,value pairs
        cache = OrderedDict()
        hits = 0
        misses = 0
        
        def inner(*args):
            nonlocal cache, hits, misses
            if args in cache:
                hits += 1
                result = cache[args]
                cache.move_to_end(args)
            else:
                misses += 1
                result = func(*args)
                if len(cache) >= maxsize:
                    cache.popitem(last=False)
                cache[args] = result
            return result
            
        def get_cache_info():
            #nonlocal cache, hits, misses
            CacheInfo = namedtuple('CacheInfo', ['hits', 'misses', 'maxsize', 'currsize'])
            return CacheInfo(hits=hits, misses=misses, currsize=len(cache), maxsize=maxsize)
        inner.cache_info = get_cache_info
        return inner
    return outer

if __name__ == '__main__':
    import urllib.request, urllib.error

    @lru_cache(maxsize=32)
    def get_pep(num):
        resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
        try:
            with urllib.request.urlopen(resource) as s:
                return s.read()
        except urllib.error.HTTPError:
            return 'Not Found'

    for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
        pep = get_pep(n)
        print(n, len(pep))

    print(get_pep.cache_info())
