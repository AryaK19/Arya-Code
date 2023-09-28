import tensorflow as tf
from tensorflow import keras 
import numpy as np
import matplotlib.pyplot as plt

data = keras.datasets.fashion_mnist

(train_images,train_labels),(test_images , test_labels) = data.load_data() ## here keras makes it easy to split the data

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat','Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images/255.0
test_images = test_images/255.0


# print(train_images[7])
# print(train_labels[60])
# plt.imshow(train_images[60],cmap=plt.cm.binary)
# plt.show()


model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28,28)),
        keras.layers.Dense(128,activation='relu'),
        keras.layers.Dense(10,activation='softmax'),
        ])
model.compile(optimizer='adam',loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=["accuracy"])

model.fit(train_images,train_labels,epochs=4) #epoch tells how many times the same image is seen/used
predictions = model.predict(test_images)

for i in range(100,105):
    plt.grid(False)
    plt.imshow(test_images[i],cmap=plt.cm.binary)
    plt.title(f"Actual = {class_names[test_labels[i]]}")
    plt.xlabel(f"Prediction : {class_names[np.argmax(predictions[i])]}")
    plt.show()


