# Real data is not always numbers. It often has text categories:
# City:  ["Mumbai", "Delhi", "Chennai"]
# Color: ["Red", "Blue", "Green"]
# Grade: ["A", "B", "C", "D"]
# ML models only understand numbers. So we need to convert text → numbers smartly.

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# ----------------------------------
# STEP 1: Dataset with text column
# ----------------------------------
data = {
    'city':       ['Mumbai','Delhi','Chennai','Mumbai','Chennai',
                   'Delhi','Mumbai','Delhi','Chennai','Mumbai'],
    'size_sqft':  [1000, 1500, 2000, 1200, 1800,
                   2500, 900, 1600, 2200, 3000],
    'price_lakhs':[60,   70,  55,   72,   60,
                   120,  54,  75,   58,   165]
}
df = pd.DataFrame(data)
print("Original Data:")
print(df.head())

# ----------------------------------
# STEP 2: One Hot Encoding
# ----------------------------------
# pd.get_dummies automatically creates 0/1 columns
df_encoded = pd.get_dummies(df, columns=['city'])
print("\nAfter One Hot Encoding:")
print(df_encoded.head())

# ----------------------------------
# STEP 3: Drop ONE dummy column to avoid
# "Dummy Variable Trap"
# ----------------------------------
# If Mumbai=0 and Delhi=0, it MUST be Chennai
# So one column is always redundant — drop it!
df_encoded = pd.get_dummies(df, columns=['city'], drop_first=True)
print("\nAfter dropping first (avoiding dummy variable trap):")
print(df_encoded.head())

# ----------------------------------
# STEP 4: Train model with encoded data
# ----------------------------------
X = df_encoded.drop('price_lakhs', axis=1)
y = df_encoded['price_lakhs']

model = LinearRegression()
model.fit(X, y)
print(f"\nModel R² Score: {model.score(X, y):.4f}")