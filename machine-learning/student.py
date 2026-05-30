from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

# X = input data (features)
X = [[1], [2], [3], [4], [5], [6],[7]]

# y = output data (target)
y = [10, 20, 30, 40, 50, 60,70]

# Split data into training and testing
train_X, val_X, train_y, val_y = train_test_split(
    X,
    y,
    random_state=0
)
print("Training X:", train_X)
print("Validation X:", val_X)

# Create model
model = DecisionTreeRegressor()

# Train model
model.fit(train_X, train_y)

# Predict
predictions = model.predict(val_X)

print("Predictions:", predictions) 

# Calculate error
mae = mean_absolute_error(val_y, predictions)

print("MAE:", mae)

