# Write a NumPy program to test if any of the elements of a given array are non-zero. 
import numpy as np
arr= np.array([2,3,1,0,7])
 
result = np.any(arr)

if result:
    print("no zero")
else:
    print("zero")
    
# Explanation:
# np.any(arr) returns True if any element in arr is non-zero.
# If the result is True, it means there is at least one non-zero element in the array.
# If the result is False, it means all elements are zero.