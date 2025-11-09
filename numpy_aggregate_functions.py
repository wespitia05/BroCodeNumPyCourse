# aggregate functions = summarize data and typically return a single value

import numpy as np

array = np.array([[1, 2, 3, 4, 5], 
                  [6, 7, 8, 9, 10]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array)) # standard deviation
print(np.var(array)) # variance (square of std)
print(np.min(array))
print(np.max(array))
print(np.argmin(array)) # returns index number of min
print(np.argmax(array)) # returns index number of max