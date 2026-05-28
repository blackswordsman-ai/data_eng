# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints)
# plt.show()
import pandas as pd
from streamlit import dataframe


create_data_frame= pd.DataFrame({
    "name": ["John", "Alice", "Mike"],
    "salary": [50000, 60000, 70000],
    "department": ["IT", "HR", "IT"]
})

name = dataframe.loc[0] = ["John", 55000, "IT"]
print(name)