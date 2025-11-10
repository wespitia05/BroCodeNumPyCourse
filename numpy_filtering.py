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