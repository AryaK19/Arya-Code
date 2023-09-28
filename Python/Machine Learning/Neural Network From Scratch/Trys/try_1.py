import numpy as np
from data import get_mnist
import random as rn


X,Y = get_mnist()



class Layer_Dense:
    def __init__(self,n_inputs, n_neurons):
        self.weights = 0.10*np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1,n_neurons))
        
            
    def forward(self,inputs):
        self.output = np.dot(inputs,self.weights) + self.biases

        return self.output

class Activation_ReLU:
    def forward(self,inputs):
        self.output = np.maximum(0,inputs)
 

class Activation_SoftMAx:
    def forward(self,inputs):
        exp_values = np.exp(inputs - np.max(inputs,1,keepdims=True))
        self.output = exp_values/np.sum(exp_values,1,keepdims=True)
        return self.output
    
class Activation_Sigmoid:
    def forward(self,inputs):
        exp_values = np.exp(inputs)
        self.output = 1.0 / (1.0+ exp_values)
        return self.output

class Loss:
    def calculate(self,output,y):
        sample_losses = self.forward(output,y)
        data_loss = np.mean(sample_losses)
        return data_loss
    
class Loss_CategoricalCrossentropy(Loss):
    def forward(self,output,y):
        samples = len(y)
        y_pred_clipped = np.clip(y,1e-7,1-1e-7)

        sample_output = np.sum(output*y,axis=1)
        
        negative_log_probability = -np.log(sample_output) # Formula for this type of loss
        return negative_log_probability


class Loss_MeanSquaredError(Loss):
    def forward(self,output,y):
        error = (1 / len(output)) * np.sum((output - y) ** 2, axis=0)   #Formula for RMSE
        
        return error
    
class Loss_SquaredError(Loss):
    def forward(self,output,y):
        error = np.sum((y - output) ** 2, axis=0)   #Formula for RMSE
        
        return error
        

dense1 = Layer_Dense(784,18)
activation1 = Activation_Sigmoid()

dense2 = Layer_Dense(18,10)
activation2 = Activation_Sigmoid()

activation3 = Activation_SoftMAx()

loss_function = Loss_SquaredError()
loss_pre = 100
acc=0

range_ = 100
while loss_pre>0.04 and acc<90:
    count = 0

    dense1.forward(X[:range_])
    activation1.forward(dense1.output)

    dense2.forward(activation1.output)
    activation2.forward(dense2.output)



    output = activation3.forward(activation2.output)


    loss_new = loss_function.calculate(output,Y[:range_])

    if loss_new<loss_pre:
        print("LOSS :",loss_new)
        loss_pre = loss_new
        weigths_1 = dense1.weights
        biases_1 = dense1.biases
        weigths_2 = dense2.weights
        biases_2 = dense2.biases
        for i in range(range_):   
            if (np.argmax(output[i]) == np.argmax(Y[i])):
                count+=1

        acc = (count/range_)*100
        print("ACCURACY :",acc)

    else:
        dense1.weights = np.random.randn(784,1)
        dense1.biases = 20*rn.random()*np.random.randn(1,18)

        dense2.weights =np.random.randn(18,10)
        dense2.biases = 20*rn.random()*np.random.randn(1,10)


