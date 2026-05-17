import pandas as pd

data = {
    "name": ["John", "Alice", "Mike"],
    "salary": [50000, 60000, 70000],
    "department": ["IT", "HR", "IT"]
}

df = pd.DataFrame(data)

print(df)