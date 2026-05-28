# # conda install scikit-learn #anaconda users
# # Pip3 install scikit-learn

# from sklearn.linear_model import LinearRegression
# import numpy as np

# # Input data
# X = np.array([[1], [2], [3], [4]])

# # Output labels
# y = np.array([11, 22, 33, 42])

# # Create model
# model = LinearRegression()

# # Train model
# model.fit(X, y)
# score = model.score(X, y)
# print("Model Score:", score)

# # Predict
# prediction = model.predict([[5]])

# print(prediction)


# Install scikit-learn
# pip install scikit-learn

# Import the most common libraries
# import numpy as np          # Math operations
# import pandas as pd         # Data handling
# import matplotlib.pyplot as plt  # Plotting graphs
# from sklearn import datasets     # Sample datasets

# # Quick test - load a sample dataset
# from sklearn.datasets import load_iris
# data = load_iris()
# print(data)
# print("Features:", data.feature_names)
# print("Classes:", data.target_names)
# print("Data shape:", data.data.shape)  # 150 rows, 4 columns


import pickle
from pyexpat import model

# Save the trained model
with open('income_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Model saved!")

# Load and use later (no retraining needed!)
with open('income_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

result = loaded_model.predict([[2025]])
print(f"Income in 2025: ${result[0]:.2f}")