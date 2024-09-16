# Write a NumPy program to compute the inner product of vectors for 1-D arrays (without complex conjugation) and in higher dimension.
import numpy as np

# Create two 1-D arrays 'a' and 'b'
a = np.array([1, 2, 5])
b = np.array([2, 1, 0])

# Display the original 1-D arrays 'a' and 'b'
print("Original 1-d arrays:")
print(a)
print(b)

# Calculate the inner product of arrays 'a' and 'b' using np.inner()
result = np.inner(a, b)

# Display the inner product of the said vectors
print("Inner product of the said vectors:")
print(result)

# Create two 3x3 arrays 'x' and 'y'
x = np.arange(9).reshape(3, 3)
y = np.arange(3, 12).reshape(3, 3)

# Display the original higher-dimensional arrays 'x' and 'y'
print("Higher dimension arrays:")
print(x)
print(y)

# Calculate the inner product of arrays 'x' and 'y' using np.inner()
result = np.inner(x, y)

# Display the inner product of the said vectors
print("Inner product of the said vectors:")
print(result) 
