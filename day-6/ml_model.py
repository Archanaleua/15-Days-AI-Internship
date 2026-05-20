# Import libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load CSV dataset
data = pd.read_csv("house_data.csv")

# Input and Output
X = data[["Area"]]
y = data["Price"]

# Create Linear Regression model
model = LinearRegression()

# Train model
model.fit(X, y)

# Save trained model
with open("house_price_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained successfully!")