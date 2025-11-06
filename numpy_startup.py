# numpy stands for numerical python
# its a python library used for numerical computing
# wildly used in fields like data science, engineering, AI/ML
# under the hood, numpy is written in c

# EXAMPLE
# np.array([1, 2, 3]) * 2 = [2, 4, 6] - uses numpy
# [1, 2, 3] * 2 = [1, 2, 3, 1, 2, 3] - uses regular python

import numpy as np

# prints current version of numpy
# print(np.__version__)

# my_list = [1, 2, 3, 4]

# my_list = my_list * 2 # duplicates our list rather than multiplying each value by 2

# print(my_list)

array = np.array([1, 2, 3, 4])
array = array * 2 # will double the elements in the numpy array
print(array)
print(type(array)) # prints the type of object the array is (numpy.ndarray)