'''
Homework 7 - Problem 1
'''

import random
import numpy as np
import timeit

def mc_vanilla(n):
    n_in = 0
    for i in range(n):
        r_x = random.uniform(-1,1)
        r_y = random.uniform(-1,1)
        if r_x**2 + r_y**2 < 1:
            n_in += 1
    return 4*n_in/n

def mc_numpy(n):
    r_xs, r_ys = np.random.uniform(-1,1,size=n), np.random.uniform(-1,1,size=n)
    return 4*(np.sum((r_xs**2 + r_ys**2) < 1))/n

if __name__ == '__main__':
    print("mc_vanilla result = {}".format(mc_vanilla(10000000)))
    print("mc_vanilla time: {}".format(min(timeit.repeat(stmt='mc_vanilla(10000000)', number=1, repeat=3, globals=globals()))))
    print("mc_numpy result = {}".format(mc_numpy(10000000)))
    print("mc_numpy time: {}".format(min(timeit.repeat(stmt='mc_numpy(10000000)', number=1, repeat=3, globals=globals()))))


    
    
        
        
