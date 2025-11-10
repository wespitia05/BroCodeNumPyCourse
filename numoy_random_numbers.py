import numpy as np

# sets the random number generator
rng = np.random.default_rng()

# prints the random numbers
# parameters: starting, end (exclusive), size
print(rng.integers(low=1, high=101, size=(3, 2)))

# uniform = uniform distribution (floating point number)
print(np.random.uniform(low=-1, high=1, size=(3,3)))

# shuffling an array
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)