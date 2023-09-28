# Loading iris dataset
from sklearn import datasets
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()

features = iris.data
labels = iris.target

lenth = int(len(features)*0.80)

train_x = features[:lenth]
train_y = labels[:lenth]
test_x  = features[lenth:]
test_y = labels[lenth:]
# print(iris.DESCR)

# print(features[0],labels[0])
 
#  Training The classifier

clf = KNeighborsClassifier()

clf.fit(features,labels)
preds = clf.predict(test_x)
print(1-np.square(preds-test_y).mean())