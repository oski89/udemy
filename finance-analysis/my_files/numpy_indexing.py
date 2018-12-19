import numpy as np

arr = np.arange(11)
print(arr)
print()

# Brackets for indexing
print(arr[8])
print(arr[1:5])
print(arr[:5])
print(arr[3:])
print()

# Broadcasting OBS! Numpy uses broadcasting instead of copying.
print(arr)
slice_arr = arr[:5]
print(slice_arr)
slice_arr[:] = 99
print(slice_arr)
print(arr)
print()

# Copy an array
arr_copy = arr.copy()
print(arr_copy)
arr_copy[:] = range(11)
print(arr_copy)
print(arr)
print()

# Matrix -> mat[row,col] or mat[row][col]
mat = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(mat[0])
print(mat[1][1])  # or
print(mat[1, 1])
print(mat[0, 2])
print(mat[:2, 1:])
print(mat[1:, :2])
print()

# Conditional selection
arr = np.arange(11)
print(arr)
bool_arr = arr > 4
print(arr[bool_arr])  # or
print(arr[arr > 4])
