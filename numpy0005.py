# Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a number).

import numpy as np


arr = np.array([1, 0, np.nan, np.inf, -np.inf, 3.5])


finiteness = np.isfinite(arr)

print("Array:", arr)
print("Finiteness (True means finite):", finiteness)
