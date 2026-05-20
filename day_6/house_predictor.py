import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle

os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("===== HOUSE PRICE PREDICTOR =====")

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

print("Model loaded successfully!")

test_houses = pd.DataFrame({
    "Area":     [1000, 2000, 3000],
    "Bedrooms": [2,    3,    5],
    "Age":      [5,    2,    1]
})

predictions = model.predict(test_houses)

print("\n--- Sample Predictions ---")
for i in range(len(test_houses)):
    area  = test_houses["Area"][i]
    beds  = test_houses["Bedrooms"][i]
    age   = test_houses["Age"][i]
    price = predictions[i]
    print(f"Area: {area} sqft | {beds} BHK | {age} yrs  =>  Price: Rs {price:,.0f}")

print("\n--- Enter Your House Details ---")
area  = float(input("Enter Area (sqft) : "))
beds  = float(input("Enter Bedrooms    : "))
age   = float(input("Enter Age (years) : "))

user_input = pd.DataFrame([[area, beds, age]], columns=["Area", "Bedrooms", "Age"])
price = model.predict(user_input)[0]
print(f"\nPredicted House Price: Rs {price:,.0f}")

data = pd.read_csv("house_data.csv")

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.scatter(data["Area"], data["Price"], color="orange", edgecolors="darkorange", s=80, label="Data Points")
m, b = np.polyfit(data["Area"], data["Price"], 1)
x_line = np.linspace(data["Area"].min(), data["Area"].max(), 100)
plt.plot(x_line, m * x_line + b, "r-", linewidth=2, label="Trend Line")
plt.xlabel("Area (sqft)"); plt.ylabel("Price (Rs)"); plt.title("Area vs Price")
plt.legend(); plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.scatter(data["Area"], data["Price"], color="steelblue", s=80, label="Dataset")
plt.scatter([area], [price], color="red", s=200, zorder=5, label=f"Your House: Rs {price:,.0f}")
plt.xlabel("Area (sqft)"); plt.ylabel("Price (Rs)"); plt.title("Your Prediction on Chart")
plt.legend(); plt.grid(True, alpha=0.3)

plt.suptitle("Day 6 - House Price Predictor", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig("day6_output.png", dpi=150)
plt.show()

print("\nChart saved as day6_output.png")
print("===== Day 6 Complete! =====")