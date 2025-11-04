import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("/home/Desktop/neha/sheet.csv")
print("Columns:", df.columns)

x = df[['Hours']]
y = df['Scores']

model = LinearRegression()
model.fit(x, y)

print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_)

plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, model.predict(x), color='red', label='Regression Line')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression")
plt.legend()
plt.show()