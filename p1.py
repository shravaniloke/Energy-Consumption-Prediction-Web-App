import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from pickle import dump 

#Load dataset
train_data = pd.read_csv("train_energy_data.csv")
test_data = pd.read_csv("test_energy_data.csv")

# Separate features and target
x_train = train_data.drop("Energy Consumption", axis=1)
y_train = train_data["Energy Consumption"]

x_test = test_data.drop("Energy Consumption", axis=1)
y_test = test_data["Energy Consumption"]

# One-hot encode categorical columns (IMPORTANT)
x_train = pd.get_dummies(
    x_train,
    columns=["Building Type", "Day of Week"],
    drop_first=True
)

x_test = pd.get_dummies(
    x_test,
    columns=["Building Type", "Day of Week"],
    drop_first=True
)

# Align columns (VERY IMPORTANT STEP)
x_test = x_test.reindex(columns=x_train.columns, fill_value=0)

# Train Random Forest
model = RandomForestRegressor(n_estimators=200,random_state=42)
model.fit(x_train, y_train)

# Predict on test data
y_pred = model.predict(x_test)

# R² score
r2 = r2_score(y_test, y_pred)

print("R² Score :", r2)

#generate a pickle file (load)
f = open("sp.pkl", "wb")
dump(model, f)
f.close()
print("model saved")
