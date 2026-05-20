import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Page configuration
st.set_page_config( 
    page_title="AI House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# Title
st.title("🏠 AI House Price Predictor")

st.markdown("---")

st.write(
    "This Machine Learning model predicts house prices based on area."
)

# Dataset
data = pd.DataFrame({
    "Area": [1000, 1200, 1500, 1800, 2000, 2500],
    "Price": [20, 25, 30, 35, 40, 50]
})

# Features and target
X = data[["Area"]]
y = data["Price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Sidebar
st.sidebar.header("User Input")

# Slider input
area = st.sidebar.slider(
    "Select House Area",
    500,
    5000,
    1500
)

# Prediction
prediction = model.predict([[area]])

# Output section
st.subheader("Prediction Result")

st.success(
    f"Estimated House Price = {prediction[0]:.2f} Lakhs"
)

# Show dataset
st.subheader("Training Dataset")

st.dataframe(data)

# Visualization
st.subheader("Data Visualization")

fig, ax = plt.subplots()

ax.scatter(data["Area"], data["Price"])

ax.plot(data["Area"], model.predict(X))

ax.set_xlabel("Area")
ax.set_ylabel("Price")

st.pyplot(fig)
