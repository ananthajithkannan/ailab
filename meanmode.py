import numpy as np 
import pandas as pd 
from scipy import stats 
data = [21, 15, 14, 17, 15, 18, 11, 14, 16, 19, 14, 19, 14, 11] 
data_np = np.array(data) 
print("Mean:", np.mean(data_np)) 
print("Median:", np.median(data_np)) 
print("Mode:", stats.mode(data_np, keepdims=True)[0][0]) 
print("Standard Deviation:", np.std(data_np)) 
import matplotlib.pyplot as plt 
import seaborn as sns 
sns.histplot(data_np, kde=True) 
plt.title("Data Distribution") 
plt.xlabel("Values") 
plt.ylabel("Frequency") 
plt.show()