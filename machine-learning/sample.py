# conda install scikit-learn #anaconda users
# Pip3 install scikit-learn

from sklearn.linear_model import LinearRegression
import numpy as np

# Input data
X = np.array([[1], [2], [3], [4]])

# Output labels
y = np.array([11, 22, 33, 42])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict
prediction = model.predict([[5]])

print(prediction)