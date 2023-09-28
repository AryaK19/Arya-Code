out_max = np.max(layer_outputs,1,keepdims=True)

sub_values = layer_outputs - out_max

exp_values = np.exp(sub_values)

print(sub_values)

# Normaliseing the values 
norm_values = []
norm_values = exp_values/np.sum(exp_values,1,keepdims=True)
