import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
import pickle

os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("===== ML MODEL TRAINING =====")

data = pd.read_csv("house_data.csv")
print("Data loaded! Total rows:", len(data))
print(data)

X = data[["Area", "Bedrooms", "Age"]]
y = data["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("\nTraining rows:", len(X_train))
print("Testing rows :", len(X_test))

model = LinearRegression()
model.fit(X_train, y_train)
print("\nModel Training DONE!")

y_pred = model.predict(X_test)
print("R2 Score :", round(r2_score(y_test, y_pred) * 100, 2), "%")
print("MAE      :", round(mean_absolute_error(y_test, y_pred), 2))

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("\nModel saved as model.pkl")
print("Now run house_predictor.py !")