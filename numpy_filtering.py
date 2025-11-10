# filtering = refers to the process of selecting elements from
#             an array that match a given condition

import numpy as np

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65], 
                 [39, 22, 15, 99, 18, 19, 20, 21]])

# create new array with teenagers
teenagers = ages[ages < 18]
print(teenagers)

# create new array with adults
adults = ages[(ages >= 18) & (ages < 65)]
print(adults)

# create new array with seniors
seniors = ages[ages >= 65]
print(seniors)

# create new array with even ages
evens = ages[ages % 2 == 0]
print(evens)

# create new array with odd ages
odds = ages[ages % 2 != 0]
print(odds)

# using where function to preserve original shape
# 3 arguments: (condition, array, fill in value)
adults = np.where(ages >= 18, ages, 0)
print(adults)