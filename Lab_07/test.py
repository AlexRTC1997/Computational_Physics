# importing the modules
import numpy as np
from numpy import random

# limits of integration
a = 0
b = np.pi  # gets the value of pi
N = 1000000
theorycal_value = 2.0

# array of zeros of length N
ar = np.zeros(N)

# iterating over each Value of ar and filling
# it with a random value between the limits a
# and b
for i in range(len(ar)):
    ar[i] = random.uniform(a, b)

# variable to store sum of the functions of
# different values of x
integral = 0.0


# iterates and sums up values of different functions of x
# TODO: Change the integral to calc
for i in ar:
    integral += np.sin(i)

# we get the answer by the formula derived adobe
ans = (b-a)/float(N)*integral
error = (ans - theorycal_value) / theorycal_value * 100

# prints the solution
print(f'The theorycal value is {theorycal_value}')
print(f'The value calculated by monte carlo integration is {ans}')
print(f'The error is {error}%')
