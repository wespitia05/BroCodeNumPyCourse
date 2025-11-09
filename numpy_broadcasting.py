# broadcasting allows numpy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape

# the dimensions have the same size
# OR
# one of the dimensions has a size of 1

import numpy as np

array1 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)

# ***** EXERCISE ***** #
a1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
a2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(a1.shape)
print(a2.shape)

print(a1 * a2)