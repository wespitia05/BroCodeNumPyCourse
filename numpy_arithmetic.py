import numpy as np

# ***** SCALAR ARITHMETIC ***** #
array = np.array([1, 2, 3])

print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5)

# ***** VECTORIZED MATH FUNCTIONS ***** #
array1 = np.array([1.01, 2.5, 3.99])

print(np.sqrt(array1))
print(np.round(array1))
print(np.floor(array1)) # always round down
print(np.ceil(array1)) # always round up
print(np.pi)

# ***** EXERCISE ***** #
radii = np.array([1, 2, 3])

print(np.pi * radii ** 2) # area of circle

# ***** ELEMENT-WISE ARITHMETIC ***** #
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])

print(a1 + a2)
print(a1 - a2)
print(a1 * a2)
print(a1 / a2)
print(a1 ** a2)