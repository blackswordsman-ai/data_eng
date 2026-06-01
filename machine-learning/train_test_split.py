import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Sample dataset
np.random.seed(42)
X = pd.DataFrame({'size': np.random.randint(500, 3000, 100)})
y = X['size'] * 50 + np.random.randint(-5000, 5000, 100)

# ----------------------------------
# Split: 80% train, 20% test
# ----------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 20% for testing
    random_state=42     # fixes the random split (reproducible)
)

print(f"Training samples : {len(X_train)}")
print(f"Testing samples  : {len(X_test)}")

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# ----------------------------------
# ALL Evaluation Metrics Explained
# ----------------------------------
r2   = r2_score(y_test, y_pred)
mae  = mean_absolute_error(y_test, y_pred)
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"\n📊 Evaluation Metrics:")
print(f"R² Score : {r2:.4f}  → {r2*100:.1f}% of data pattern explained")
print(f"MAE      : {mae:.2f}  → avg error is ₹{mae:.0f}")
print(f"MSE      : {mse:.2f}  → penalizes large errors more")
print(f"RMSE     : {rmse:.2f}  → same unit as target (most useful)")




# Metric Cheat Sheet
# R²   → How well model fits (0 to 1, higher = better)
# MAE  → Average of all errors (easy to understand)
# MSE  → Squares the errors (punishes big mistakes heavily)
# RMSE → Square root of MSE (same unit as your output)

# For house prices in Lakhs:
# RMSE = 5 means → on average, predictions are off by ₹5 Lakhs