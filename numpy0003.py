# Write a NumPy program to test whether none of the elements of a given array are zero.
import numpy as np
arr= np.array([1,2,3,5])
result = np.all(arr)

if result:
    print("No zero")
else:
    print("zero")

# Explanation:
# np.all(arr) will return True if all elements of arr are non-zero.
# If the result is True, it means there are no zero elements in the array.
# If the result is False, it means there is at least one zero in the array.