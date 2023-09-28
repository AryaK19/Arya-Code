import numpy as np
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd

data = pd.read_csv("Tutorial\Files\KNN\car.data")


X = data[['buying','maint','safety']].values

y = data[['class']]


#converting the data 
Le = LabelEncoder()
for i in range(len(X[0])):
    X[:,i] = Le.fit_transform(X[:,i])



#converting the y

label_maping = {"unacc":0,'acc':1,'good':2,"vgood":3}

y["class"] = y['class'].map(label_maping)
y = np.array(y)


knn = neighbors.KNeighborsClassifier(n_neighbors=25, weights="uniform")

X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

knn.fit(X_train,y_train)

prediction = knn.predict(X_test)

accuracy = metrics.mean_squared_error(y_test,prediction)

print("Preditions :",prediction)
print("Accuracy :",accuracy)
a = 584
print('actual value : ',y[a][0])
print('predicted value : ',knn.predict(X)[a])

