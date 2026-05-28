# import pandas as pd

# df = pd.read_csv("/Users/bestway/Python-Project/python-workspace/pandas/employees.csv")
# print(df.head())# Shows the first 5 rows
# print(df.info()) # Shows column types and non-null counts.
# print(df.describe())
# print(df.columns)
# print(df.shape) # Shows the number of rows and columns.

# Employees in department 50
# dept_50 = df[df["DEPARTMENT_ID"] == 50]
# print(dept_50)

# Employees in department 50 with salary > 5000
# high_salary = df[(df["DEPARTMENT_ID"] == 50) & (df["SALARY"] > 5000)]
# print(high_salary)

# Select specific columns
# print(df[["FIRST_NAME", "SALARY"]])

# Sort by salary descending
# print(df.sort_values(by="SALARY", ascending=False))


# Series operations
# import pandas as pd

# salary = pd.Series([50000, 60000, 70000])

# # print(salary)
# print(salary[0])

# Custom Index
# import pandas as pd

# salary = pd.Series(
#     [50000, 60000, 70000],
#     index=["John", "Alice", "Mike"]
# )

# print(salary)


# Series From Dictionary
# import pandas as pd

# data = {
#     "John": 50000,
#     "Alice": 60000,
#     "Mike": 70000
# }

# salary = pd.Series(data)

# print(salary)
# --------------------------------
# ndim - Number of dimensions
# import pandas as pd

# df = pd.Series([10,20,30,40])

# print(df.ndim) # Number of dimensions

import pandas as pd

data = {
    "name": ["John", "Alice"],
    "salary": [50000, 60000]
}

df = pd.DataFrame(data)

print(df.ndim)
print(df)