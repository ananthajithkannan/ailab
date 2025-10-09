import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

data = load_iris()
x = data.data
y = data.target

df = pd.DataFrame(x, columns=data.feature_names)
df['target'] = y
print(df.head(10))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=43)

model = SVC()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print("Predicted labels:", y_pred)

confusion = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(confusion)

accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy:.2f}")

classification = classification_report(y_test, y_pred)
print("\nClassification Report:")
print(classification)