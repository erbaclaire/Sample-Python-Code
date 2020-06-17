'''
Homework 7 - Problem 2
'''

import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(step_size=0.01, max_iterations=1000):

        ''' The list of lists for complex numbers in the pseudocode can be viewed as an array with the imaginary numbers as a (,1) vector and the real numbers as a (1,) vector added together to produce all combinations of real and imaginary numbers from the given ranges.
        Two zero matrices of the size of the complex numbers are created.
        There is no easy way to vectorize max_iterations - the code is run until all iterations are complete in this for loop.
        While the loop runs, two items are tracked:    
        1. z keeps track of the value in the array squared plus the original value in that position from the complex number array.
        2. iteration_counters keeps track of how many iterations the loop goes through before the abs(z) >= 4. 
        '''

        real_range = np.arange(-2, 1+step_size, step_size)
        imag_range = np.arange(-1, 1+step_size, step_size)
        complex_numbers = real_range + (imag_range*1.0j).reshape(-1,1)

        iteration_counts = np.zeros(complex_numbers.shape)
        z = np.zeros(complex_numbers.shape, dtype='complex64')
        for i in range(max_iterations):
            z = z**2 + complex_numbers
            iteration_counts = iteration_counts + (abs(z) < 4)
        
        return iteration_counts

if __name__ == '__main__':
    print(mandelbrot())
    plt.imshow(mandelbrot())
    plt.gray()
    plt.show()
