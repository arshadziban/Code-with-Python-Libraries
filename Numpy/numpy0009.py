# Write a NumPy program to test whether two arrays are element-wise equal within a tolerance.
import numpy as np

array1 = np.array([1.0, 2.0, 3.0, 4.0])
array2 = np.array([1.0, 2.0000001, 2.9999999, 4.0])

# Test if the two arrays are element-wise equal within a tolerance
are_equal = np.allclose(array1, array2, atol=1e-7)

# Print the result
print("Are the two arrays element-wise equal within a tolerance?:", are_equal)
