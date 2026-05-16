# ------------------------------------------------
# # WITHOUT NumPy:

# # define a list to store the marks of students
# marks =[45, 78, 92, 56, 89]

# # create an empty list to store the new marks after adding 5 to each mark
# new_mark =[]

# # iterate through the marks list and add 5 to each mark and append it to the new_mark list
# for i in marks:
#     new_mark.append(i + 5)

# # print the new marks
# print(new_mark)


# ---------------------------------------------------

# WITH NumPy:

# import numpy as np

# marks =np.array([45, 78, 92, 56, 89])

# print(marks + 5)

# ---------------------------------------------------
# finding mean with numpy

# import numpy as np

# arr = np.array([10,20,30,40])

# print(arr.mean())

# ---------------------------------------------------
# finding mean without numpy

# number =[12, 15, 18, 20, 25]

# find_mean =sum(number) / len(number)

# print(find_mean)

