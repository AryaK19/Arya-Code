
import numpy as np
layer_outputs = [[4.8,1.21,2.385],
                 [8.9,-1.01,0.2],
                 [1.41,1.051,0.026]]

# we sutract max value for other to get rid of the overflow bc of exponential
out_max = np.max(layer_outputs,1,keepdims=True)

sub_values = layer_outputs - out_max

exp_values = np.exp(sub_values)

print(sub_values)

# Normaliseing the values 
norm_values = []
norm_values = exp_values/np.sum(exp_values,1,keepdims=True)


## the actual valuees are the same

print(norm_values)
