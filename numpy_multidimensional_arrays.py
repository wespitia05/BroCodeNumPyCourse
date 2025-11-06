# working with numpy multidimensional arrays

import numpy as np

array0 = np.array('A') # zero dimensional array
print(array0.ndim) # prints number of dimensions

array1 = np.array(['A', 'B', 'C']) # one dimensional array
print(array1.ndim) # prints number of dimensions

array2 = np.array([['A', 'B', 'C'], 
                   ['D', 'E', 'F'],
                   ['G', 'H', 'I']]) # two dimensional array
print(array2.ndim) # prints number of dimensions

array3 = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                   [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                   [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]]) # three dimensional array
print(array3.ndim) # prints number of dimensions