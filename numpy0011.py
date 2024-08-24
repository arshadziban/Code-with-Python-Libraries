# Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.
import numpy as np

array1 = np.array([1.0, 2.1, 3.2, 4.3, 5.4])
array2 = np.array([1.0, 2.10000001, 3.2, 4.3001, 5.5])

exact_equality = np.equal(array1, array2)
print("Element-wise comparison (exact equality):\n", exact_equality)

tolerance = 1e-5
equal_within_tolerance = np.isclose(array1, array2, atol=tolerance)
print("Element-wise comparison (within tolerance):\n", equal_within_tolerance)
