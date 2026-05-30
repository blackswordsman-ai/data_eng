import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["John", "Alice", "Bob"],
    "Age": [25, np.nan, 30]
})
df.dropna(axis=1) # Remove columns with missing values

print(df)