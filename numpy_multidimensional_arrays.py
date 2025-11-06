# working with numpy multidimensional arrays

import numpy as np

array0 = np.array('A') # zero dimensional array
print(array0.ndim) # prints number of dimensions
print(array0.shape) # prints tuple of integers (depth, rows, columns)

array1 = np.array(['A', 'B', 'C']) # one dimensional array
print(array1.ndim) # prints number of dimensions
print(array1.shape) # prints tuple of integers (depth, rows, columns)

array2 = np.array([['A', 'B', 'C'], 
                   ['D', 'E', 'F'],
                   ['G', 'H', 'I']]) # two dimensional array
print(array2.ndim) # prints number of dimensions
print(array2.shape) # prints tuple of integers (depth, rows, columns)

array3 = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                   [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                   [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]]) # three dimensional array
print(array3.ndim) # prints number of dimensions
print(array3.shape) # prints tuple of integers (depth, rows, columns)
print(array3[0][0][1]) # multidimensional indexing (layer, row, element)
print(array3[0][0][2]) # multidimensional indexing (layer, row, element)
print(array3[0][1][0]) # multidimensional indexing (layer, row, element)
print(array3[0][2][0]) # multidimensional indexing (layer, row, element)
print(array3[1][1][1]) # multidimensional indexing (layer, row, element)
print(array3[0][0][0]) # multidimensional indexing (layer, row, element)