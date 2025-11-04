import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


iris = load_iris()



data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
print(data.head())



x = iris.data
y = iris.target


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=1)


model = GaussianNB()
model.fit(x_train, y_train)


y_pred = model.predict(x_test)



print("Predicted labels:", y_pred)
print("The accuracy of the model is:", accuracy_score(y_test, y_pred) * 100, "%")
print("Confusion matrix of the model is:\n", confusion_matrix(y_test, y_pred))
print("Classification report of the model is:\n", classification_report(y_test, y_pred))