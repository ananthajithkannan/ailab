from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = load_iris()
X = data.data
y = data.target
target_names = data.target_names

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print("Correct Predictions:")
for i in range(len(y_test)):
    if y_pred[i] == y_test[i]:
        print(f"Sample {i}: Predicted = {target_names[y_pred[i]]}, Actual = {target_names[y_test[i]]}")

print("\nWrong Predictions:")
for i in range(len(y_test)):
    if y_pred[i] != y_test[i]:
        print(f"Sample {i}: Predicted = {target_names[y_pred[i]]}, Actual = {target_names[y_test[i]]}")

print(f"\nAccuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")