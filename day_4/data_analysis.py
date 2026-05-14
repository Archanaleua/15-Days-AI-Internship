# data_analysis.py
import pandas as pd
import matplotlib.pyplot as plt

# Create sample dataset
data = {'Name': ['Alice','Bob','Charlie','Diana'],
        'Math': [92,78,85,90],
        'Science': [88,82,79,95]}

df = pd.DataFrame(data)
print(df.describe())

# Chart
df.set_index('Name').plot(kind='bar', title='Student Marks')
plt.tight_layout()
plt.savefig('marks_chart.png')
print("Chart saved!")