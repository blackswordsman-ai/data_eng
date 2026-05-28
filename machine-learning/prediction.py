#  WHERE it is used

# Predicting Canada's per capita income (your PDF's exercise!)
# Predicting house prices based on size
# Predicting crop yield based on rainfall

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# ----------------------------------
# STEP 1: Create sample data
# (Canada per capita income example from your PDF)
# ----------------------------------
data = {
    'year': [1970,1971,1972,1973,1974,1975,1976,1977,1978,
             1979,1980,1981,1982,1983,1984,1985,1986,1987,
             1988,1989,1990,1991,1992,1993,1994,1995,1996],
    'income': [3399,3768,4042,4457,4966,5456,5911,6420,6837,
               7400,8031,8736,9077,9240,9814,10212,10697,11156,
               11749,12336,13021,13481,13816,14181,14696,15547,16244]
}
df = pd.DataFrame(data)


# ----------------------------------
# STEP 2: Prepare X (input) and y (output)
# ----------------------------------
X = df[['year']]   # Input: year (2D array needed)
y = df['income']   # Output: income

# ----------------------------------
# STEP 3: Split data → train & test
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
# STEP 5: Check model parameters
# ----------------------------------
print(f"Slope (m): {model.coef_[0]:.2f}")
print(f"Intercept (c): {model.intercept_:.2f}")
# This means: income = m × year + c

# ----------------------------------
# STEP 6: Predict for year 2020
# ----------------------------------
prediction_2020 = model.predict([[2020]])
print(f"\nPredicted income for 2020: ${prediction_2020[0]:.2f}")

# ----------------------------------
# STEP 7: Check accuracy (R² score)
# ----------------------------------
score = model.score(X_test, y_test)
print(f"Model Accuracy (R²): {score:.4f}")
# R² close to 1.0 = very accurate

# ----------------------------------
# STEP 8: Visualize
# ----------------------------------
plt.scatter(df['year'], df['income'], color='blue', label='Actual Data')
plt.plot(df['year'], model.predict(X), color='red', label='Best Fit Line')
plt.xlabel('Year')
plt.ylabel('Per Capita Income ($)')
plt.title('Canada Per Capita Income - Linear Regression')
plt.legend()
plt.show()