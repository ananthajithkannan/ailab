import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

data = [21, 15, 14, 17, 15, 18, 11, 14, 16, 19, 14, 19, 14, 11]
data_np = np.array(data)

print("Mean:", np.mean(data_np))
print("Median:", np.median(data_np))

mode_result = stats.mode(data_np, keepdims=True)
print("Mode:", mode_result.mode[0])

print("Standard Deviation:", np.std(data_np))

sns.histplot(data_np, kde=True)
plt.title("Data Distribution")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()