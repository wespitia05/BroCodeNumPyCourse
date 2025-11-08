import numpy as np

array = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8], 
                  [9, 10, 11, 12], 
                  [13, 14, 15, 16]])

# array[start:end:step]

# accessing array at index 0
print(array[0])
# accessing array at index 1
print(array[1])
# accessing array at index 2
print(array[2])
# accessing array at index 3
print(array[3])

# ***** ROW SELECTION ***** #
# access 1-12
print(array[0:3])
# access 5-16
print(array[1:4])
# access 1-16
print(array[0:])
# access 1-4, 9-12
print(array[0:4:2]) # end point is exclusive
# access 5-8, 13-16
print(array[1:5:2]) # end point is exclusive
# access 1-16 in reverse
print(array[::-1])
# access 5-8, 13-16 in reverse
print(array[::-2])

# ***** COLUMN SELECTION ***** #
# selecting all rows and accessing column 0
print(array[:, 0])
# selecting all rows and accessing column 1
print(array[:, 1])
# selecting all rows and accessing column 2
print(array[:, 2])
# selecting all rows and accessing column 3
print(array[:, 3])
# selecting all rows and accessing column 1, 2, 3
print(array[:, 0:3]) # end point is exclusive
# selecting all rows and accessing column 2, 3, 4
print(array[:, 1:4]) # end point is exclusive