import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:/Users/nares/OneDrive/Desktop/college placement/college_placement_data.csv"
df = pd.read_csv(file_path)

df['Branch'] = df['Branch'].str.upper()
df['Placement %'] = (df['Placed'] / df['Total Students']) * 100

# Bar Chart
df.groupby('Branch')['Placement %'].mean().plot(kind='bar')
plt.title("Branch-wise Placement Percentage")
plt.ylabel("Placement %")
plt.show()

# Line Chart
df.groupby('Year')['Avg Package (LPA)'].mean().plot(kind='line', marker='o')
plt.title("Year-wise Average Package Trend")
plt.ylabel("Average Package (LPA)")
plt.show()

# Pie Chart
df.groupby('Gender')['Placed'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.title("Gender-wise Placement Distribution")
plt.ylabel("")
plt.show()
