# . ARRAY CREATION What is Array Creation?
# Creating a NumPy array to store numbers efficiently.
# ------------------------------------
# import numpy as np

# # Creating a NumPy array
# marks = np.array([45, 67, 89, 23, 90])

# print(marks)


# Indexing 
# ------------------------------------
# import numpy as np

# marks = np.array([45, 67, 89, 23, 90])

# # First element
# print(marks[0])

# # Third element
# print(marks[2])

# # Last element
# print(marks[-1])


# 2D Indexing
# ------------------------------------
# import numpy as np

# matrix = np.array([
#     [1,2,3],
#     [4,5,6]
# ])

# print(matrix[1,2])

# Slicing array[start:end]
# ------------------------------------
# import numpy as np

# marks = np.array([45, 67, 89, 23, 90])

# print(marks[1:4])

# Step Slicing
# print(marks[::2])

# SHAPE
# ------------------------------------
# import numpy as np

# arr = np.array([1,2,3,4])

# print(arr.shape)
# 2D Shape
# ------------------------------------
# import numpy as np
# matrix = np.array([
#     [1,2,3],
#     [4,5,6]
# ])

# print(matrix.shape)


# import numpy as np

# arr = np.array([1,2,3])

# print(arr + 5)


import numpy as np

# ARRAY CREATION
marks = np.array([45, 67, 89, 23, 90])

print("Original Array:")
print(marks)

# INDEXING
print("\nFirst Mark:")
print(marks[0])

print("\nLast Mark:")
print(marks[-1])

# SLICING
print("\nSlice:")
print(marks[1:4])

# SHAPE
print("\nShape:")
print(marks.shape)

# BASIC OPERATIONS
print("\nAdd 5:")
print(marks + 5)

print("\nMultiply by 2:")
print(marks * 2)

print("\nAverage:")
print(marks.mean())

print("\nTotal:")
print(marks.sum())



