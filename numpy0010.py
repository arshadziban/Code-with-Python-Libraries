# Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.
import numpy as np

a = np.array([3,6])
b = np. array ([4,9])
print("Greater:", np.greater(a,b))
print ("Greater_ Equal:", np.greater_equal(a,b))
print("Less:", np.less(a, b))
print("Less or Equal:", np.less_equal(a, b))
