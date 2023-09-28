from sklearn import datasets
from sklearn import linear_model, metrics
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
X = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
y = raw_df.values[1::2, 2]

# boston = datasets.load_boston()

# #features / labels

# X = boston.data
# y = boston.target
# print(X)
# print(y)
# print(X.shape)

#spliting for test and train 

X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=0.008)

# create a model 
model = linear_model.LinearRegression()
model.fit(X_train,y_train)
prediction = model.predict(X_test)

prediction = np.round(prediction,1)

accuracy = model.score(X_test,y_test)*100

# accuracy = metrics.accuracy_score(y_test,prediction)

print(prediction)
print(y_test)
print(accuracy)