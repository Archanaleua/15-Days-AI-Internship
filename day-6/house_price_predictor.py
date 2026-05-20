# house_price_predictor.py
from sklearn.linear_model import LinearRegression
import numpy as np

# Size (sqft) vs Price (lakhs)
X = np.array([[500],[750],[1000],[1200],[1500],[2000]])
y = np.array([25, 38, 50, 60, 75, 100])

model = LinearRegression()
model.fit(X, y)

size = 1100
predicted = model.predict([[size]])
print(f"Predicted price for {size} sqft: ₹{predicted[0]:.1f} Lakhs")
print(f"Model accuracy (R²): {model.score(X, y):.2%}")