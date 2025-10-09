import pandas as pd 
data = pd.read_csv("/home/vml23ad091/Downloads/grades.csv") 
print("Original Data:\n") 
data.head() 
SORT 
sort = data.sort_values("Roll.no", axis=0, ascending=1, inplace=False) 
print("Sorted DATA:\n") 
sort.head()