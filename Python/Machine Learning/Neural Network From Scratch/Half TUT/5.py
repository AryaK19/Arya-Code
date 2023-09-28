import numpy as np
np.random.seed(0)

X =[[1,2,3,2.5],
    [2.5,5,1,2.0],
    [1.5,2.7,0.3,0.8]]


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

class Loss:
    def calculate(self,output,y):
        sample_losses = self.forward(output,y)
        data_loss = np.mean(sample_losses)
        return data_loss
    
class Loss_CategoricalCrossentropy(Loss):
    def forward(self,output,y):
        samples = len(y)
        y_pred_clipped = np.clip(y,1e-7,1-1e-7)

        if len(output.shape)==1:
            sample_output = output[range(len(output)),y]
        elif len(output.shape)==2:
            sample_output = np.sum(output*y,axis=1)
        
        negative_log_probability = -np.log(sample_output)
        return negative_log_probability



dense1 = Layer_Dense(4,5)
activation1 = Activation_ReLU()

dense2 = Layer_Dense(5,3)
activation2 = Activation_SoftMAx()

dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)

y = [[0,1,0],[0,0,1],[1,0,0]]
print(activation2.output)

loss_function = Loss_CategoricalCrossentropy()
loss = loss_function.calculate(activation2.output,y)

print("Loss :",loss)


