# Simple:   y = m×x + c
# Multiple: y = m1×x1 + m2×x2 + m3×x3 + ... + c

# Example (House Price):
# Price = m1×(size) + m2×(rooms) + m3×(location_score) + c

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# ----------------------------------
# STEP 1: Create dataset
# Predict house price based on
# size, bedrooms, age, location score
# ----------------------------------
data = {
    'size_sqft':      [1000,1500,2000,2500,1200,1800,3000,2200,900,1600],
    'bedrooms':       [2,   3,   4,   4,   2,   3,   5,   4,  1,   3  ],
    'age_years':      [10,  5,   8,   2,   15,  3,   1,   6,  20,  4  ],
    'location_score': [7,   8,   6,   9,   5,   9,   10,  7,  4,   8  ],
    'price_lakhs':    [45,  75,  90,  130, 40,  100, 180, 110, 30, 85 ]
}
df = pd.DataFrame(data)
print(df)

# ----------------------------------
# STEP 2: Separate features and target
# ----------------------------------
X = df[['size_sqft', 'bedrooms', 'age_years', 'location_score']]
y = df['price_lakhs']

# ----------------------------------
# STEP 3: Train/Test Split
# ----------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------------------
# STEP 4: Train the model
# ----------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# ----------------------------------
# STEP 5: See what the model learned
# ----------------------------------
print("\n📊 What the model learned:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"  {feature:20s} → coefficient: {coef:.4f}")
print(f"  {'intercept':20s} → {model.intercept_:.4f}")

# ----------------------------------
# STEP 6: Predict on test data
# ----------------------------------
y_pred = model.predict(X_test)

print("\n🔮 Predictions vs Actual:")
for actual, predicted in zip(y_test, y_pred):
    print(f"  Actual: {actual} Lakhs  |  Predicted: {predicted:.1f} Lakhs")

# ----------------------------------
# STEP 7: Evaluate the model
# ----------------------------------
r2  = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"\n✅ R² Score  : {r2:.4f}  (closer to 1 = better)")
print(f"✅ MSE       : {mse:.2f}")
print(f"✅ RMSE      : {rmse:.2f} Lakhs average error")

# ----------------------------------
# STEP 8: Predict a NEW house
# ----------------------------------
new_house = pd.DataFrame({
    'size_sqft':      [2000],
    'bedrooms':       [3],
    'age_years':      [5],
    'location_score': [8]
})
predicted_price = model.predict(new_house)
print(f"\n🏠 New house prediction: ₹{predicted_price[0]:.1f} Lakhs")