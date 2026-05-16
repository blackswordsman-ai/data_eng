# import time

# marks = list(range(10000000))    # 10 million

# start = time.time()

# new_marks2 = [i + 5 for i in marks]

# end = time.time()

# print("List Comprehension Time:", end - start)


# import numpy as np
# import time

# marks = np.arange(1000000)

# start = time.perf_counter()

# new_marks = marks + 5


# end = time.perf_counter()


# find_speed =end - start

# print("NumPy Time:", find_speed)

# import numpy as np
# import time

# marks =np.array([45, 78, 92, 56, 89])


# start = time.perf_counter()

# new_marks = marks + 5
# end = time.perf_counter()
# find_speed =end - start
# print("NumPy Time:", find_speed)


# Import modules
import time          # Used to measure execution time
import sys           # Used to measure memory size
import numpy as np   # NumPy library


# -----------------------------------
# CREATE A NORMAL PYTHON LIST
# -----------------------------------

# Create numbers from 0 to 999999
python_list = list(range(1000000))

# Check memory size of list object
# (does not include all internal integer objects fully)
print("Python List Memory:", sys.getsizeof(python_list), "bytes")


# -----------------------------------
# START TIMER FOR PYTHON LOOP
# -----------------------------------

# Save current high precision time
start = time.perf_counter()


# Create empty list
new_list = []


# Loop through every number one by one
for i in python_list:

    # Add 5 to each number
    result = i + 5

    # Store result into new list
    new_list.append(result)


# Save ending time
end = time.perf_counter()


# Total execution time
print("Python Loop Time:", end - start)


# -----------------------------------
# NUMPY ARRAY
# -----------------------------------

# Create NumPy array
numpy_array = np.arange(1000000)

# NumPy memory used by actual data
print("NumPy Memory:", numpy_array.nbytes, "bytes")


# -----------------------------------
# START TIMER FOR NUMPY
# -----------------------------------

start = time.perf_counter()


# Vectorized operation
# NumPy internally handles looping in C
new_numpy = numpy_array + 5


# End timer
end = time.perf_counter()


# Total NumPy execution time
print("NumPy Time:", end - start)