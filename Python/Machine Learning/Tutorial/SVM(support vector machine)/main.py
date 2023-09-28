from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score 

iris  = datasets.load_iris()
#split it in features and labels

X = iris.data
y = iris.target

classes = ["Iris Setosa", "Iris Versicolour","Iris Virginica"]

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2)
 
model = svm.SVC()
model.fit(X_train,y_train)


prediction = model.predict(X_test)

acc = accuracy_score(y_test,prediction)*100
print('actual value :',y_test)
print("Preditions   :",prediction)
print("Accuracy :",str(acc)+"%")