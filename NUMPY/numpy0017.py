# Write a NumPy program to evaluate Einstein’s summation convention of two given multidimensional arrays.
import numpy as np

# Define two 2D arrays (matrices)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Perform matrix multiplication using Einstein summation
# 'ij,jk->ik' means: sum over 'j', multiply A's columns with B's rows
result = np.einsum('ij,jk->ik', A, B)

# Print the arrays and the result
print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nResult of A * B (Matrix multiplication):")
print(result)
