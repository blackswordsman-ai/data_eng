import numpy as np

# Create a 1D array
# arr_1d = np.array([[1,2,3],[12,32,33]])
# reshaped = arr_1d.reshape(3,2)
# print("1D Array:\n", arr_1d)
# print("Shape of 1D Array:", arr_1d.shape)
# print("Reshaped Array:\n", reshaped)
# print("Shape of Reshaped Array:", reshaped.shape)

# # Create a 2D array
# arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
# print("2D Array:\n", arr_2d)

# # Create a 3D array
# arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print("3D Array:\n", arr_3d)

# Understanding the datatype of an array
# import numpy as np

arr = np.array([1,2,3,])

change_to =arr.astype(float)

print(arr)
print(arr.dtype)
print(change_to)
print(change_to.dtype)
# import numpy as np

# arr = np.array([32,767], dtype=np.int16)

# print(arr)

# arr = arr + 1
# print(arr)

# import numpy as np

# arr =np.array(["apple","banana"])

# print(arr.dtype)