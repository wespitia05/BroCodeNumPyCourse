import numpy as np

# sets the random number generator
rng = np.random.default_rng()

# prints the random numbers
# parameters: starting, end (exclusive), size
print(rng.integers(low=1, high=101, size=(3, 2)))