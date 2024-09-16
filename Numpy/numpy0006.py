# Write a NumPy program to test elements-wise for positive or negative infinity. 

import numpy as np

arr= np.array([3,np.inf,-np.inf,1,-8,-5])

positive = np.isposinf(arr)
negative = np.isneginf(arr)

print("Positive", positive)
print("Negative", negative)