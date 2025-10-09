import pandas as pd 
from sklearn.datasets import load_iris 
data=load_iris() 
x=data.data 
y=data.target 
df=pd.DataFrame(x,y) 
df.head(10) 
from sklearn.model_selection import train_test_split 
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=43) 
from sklearn.svm import SVC 
model=SVC() 
model.fit(x_train,y_train) 
y=model.predict(x_test) 
print(y) 
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score 
confusion=confusion_matrix(y_test,y) 
print(confusion) 
accuracy=accuracy_score(y_test,y) 
print("accuracy ",accuracy) 
classification=classification_report(y_test,y) 
print("The classification of the dataset is ") 
print(classification)