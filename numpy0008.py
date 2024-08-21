# Write a NumPy program to test element-wise for complex numbers, real numbers in a given array. Also test if a given number is of a scalar type or not.

import numpy as np

arr = np.array([1, 1.5, 1+2j, np.inf, -np.inf, np.nan, 3.5, 0, -1])

is_complex = np.iscomplex(arr)

is_real = np.isreal(arr)

scalar_tests = [np.isscalar(element) for element in arr]

print("Array:", arr)
print("Is Complex:", is_complex)
print("Is Real:", is_real)
print("Is Scalar (for each element):", scalar_tests)
