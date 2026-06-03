import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# ----------------------------------
# STEP 1: Create dataset
# Predict if patient has diabetes
# based on age and blood sugar level
# ----------------------------------
np.random.seed(42)
n = 200

age         = np.random.randint(20, 70, n)
blood_sugar = np.random.randint(70, 200, n)

# Rule: high age + high sugar = likely diabetic
diabetes = ((age > 45) & (blood_sugar > 140)).astype(int)
# Add some noise
noise_idx = np.random.choice(n, 20, replace=False)
diabetes[noise_idx] = 1 - diabetes[noise_idx]

df = pd.DataFrame({
    'age': age,
    'blood_sugar': blood_sugar,
    'diabetes': diabetes
})

print("Sample Data:")
print(df.head(10))
print(f"\nDiabetic: {diabetes.sum()}  |  Non-diabetic: {(diabetes==0).sum()}")

# ----------------------------------
# STEP 2: Prepare features and target
# ----------------------------------
X = df[['age', 'blood_sugar']]
y = df['diabetes']

# ----------------------------------
# STEP 3: Train / Test Split
# ----------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------------------
# STEP 4: Train the model
# ----------------------------------
model = LogisticRegression()
model.fit(X_train, y_train)

# ----------------------------------
# STEP 5: Predict
# ----------------------------------
y_pred      = model.predict(X_test)         # Class: 0 or 1
y_prob      = model.predict_proba(X_test)   # Probability: [P(0), P(1)]

print("\n🔮 Sample Predictions:")
print(f"{'Age':>5} {'Sugar':>7} | {'Actual':>8} {'Predicted':>10} {'Probability':>14}")
print("-" * 55)
for i in range(8):
    age_val   = X_test.iloc[i]['age']
    sugar_val = X_test.iloc[i]['blood_sugar']
    actual    = y_test.iloc[i]
    pred      = y_pred[i]
    prob      = y_prob[i][1]   # probability of being diabetic
    print(f"{age_val:>5} {sugar_val:>7} | {actual:>8} {pred:>10} {prob:>13.1%}")

# ----------------------------------
# STEP 6: Evaluate accuracy
# ----------------------------------
accuracy = accuracy_score(y_test, y_pred)
print(f"\n✅ Accuracy: {accuracy:.2%}")

# ----------------------------------
# STEP 7: Predict for a new patient
# ----------------------------------
new_patient = pd.DataFrame({'age': [55], 'blood_sugar': [160]})
prediction  = model.predict(new_patient)
probability = model.predict_proba(new_patient)[0][1]

print(f"\n🏥 New Patient (Age:55, Sugar:160)")
print(f"   Prediction  : {'Diabetic 🔴' if prediction[0]==1 else 'Healthy 🟢'}")
print(f"   Probability : {probability:.1%} chance of diabetes")