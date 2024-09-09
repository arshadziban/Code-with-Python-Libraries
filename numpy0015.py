# Write a NumPy program to compute the cross product of two given vectors.
import numpy as np

p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]

result1= np.cross(p,q)
result2= np.cross(q,p)

print("Result1:", result1)
print("Result2:", result2)