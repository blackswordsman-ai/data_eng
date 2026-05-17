# First list
a = [1, 2, 3]

# Second list
b = [4, 5, 6]

# Empty list to store results
c = []

# Loop through indexes
for i in range(len(a)):

    # Multiply matching positions
    c.append(a[i] * b[i])

# Print final result
print(c)