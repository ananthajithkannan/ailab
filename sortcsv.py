import pandas as pd

data = pd.read_csv("/home/vml23ad091/Downloads/grades.csv")

print("Original Data:\n")
print(data.head())

sorted_data = data.sort_values(by="Roll.no", ascending=True)

print("\nSorted Data:\n")
print(sorted_data.head())