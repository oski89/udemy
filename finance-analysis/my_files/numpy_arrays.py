import numpy as np

# Create a numpy array
my_list = [1, 2, 3, 4, 5]
x = np.array(my_list)
print(type(x))
print()

# Matrix
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = np.array(my_matrix)
print(y)
print()

# Range
print(list(range(5)))
print(np.arange(5))
print()

# Zeros
print(np.zeros((2, 2)))
print()

# Ones
print(np.ones((3, 3)))
print()

# Linear space -> (from, to, #)
print(np.linspace(0, 5, 11))
print(np.linspace(7, 76, 7))
print()

# Identity matrix
print(np.eye(4))
print()

# Numpy's random library
# Uniform distribution
print(np.random.rand(5, 4))
print()

# Normal distribution
print(np.random.randn(5, 4))
print()

# Integers -> (from, to, #)
print(np.random.randint(1, 10, 13))
print()

# Reshaping
arr = np.arange(16)
print(arr)
print(arr.shape)
print()
print(arr.reshape(4, 4))
print(arr.reshape(4, 4).shape)
print()
print(arr.reshape(16, 1))
print(arr.reshape(16, 1).shape)
print()

# Data type
print(arr.dtype)
print()

# Argmax
ranarr = np.random.randint(0, 50, 10)
print("Max number in ranarr:", ranarr.max())
print("Index of max number in ranarr:", ranarr.argmax())
