import pandas as pd
import matplotlib.pyplot as plt

print("===== CHART PROGRAM =====")

data = pd.read_csv("day_4/student_data.csv")

plt.bar(data["Name"], data["Marks"])

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.show()