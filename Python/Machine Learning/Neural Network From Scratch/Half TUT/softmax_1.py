
import numpy as np
layer_outputs = [[4.8,1.21,2.385],
                 [8.9,-1.01,0.2],
                 [1.41,1.051,0.026]]


exp_values = np.exp(layer_outputs)

# Normaliseing the values 
norm_values = []
norm_values = exp_values/np.sum(exp_values,1,keepdims=True)

print(norm_values)
