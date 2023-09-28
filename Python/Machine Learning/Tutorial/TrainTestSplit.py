from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np

iris  = datasets.load_iris()
#split it in features and labels

X = iris.data
y = iris.target



print(X.shape)
print(y.shape)


X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2)# This 0.2 means the 20percent of the data remember the arrangement....lol how did i remember sahil now and what i once told about engineering lol 

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
