import numpy as np

softmax_outputs = np.array([[0.7,0.1,0.2],
                           [0.1,0.5,0.4],
                           [0.02,0.9,0.08]])

class_targets = [0,1,1] # say the y =[dog,cat,human]so here for the 3 batch the output must me dog , cat  , cat 

# print(softmax_outputs[[0,1,2],class_targets])
# print(softmax_outputs[range(len(softmax_outputs)),class_targets
# ])
loss = -np.log(softmax_outputs[range(len(softmax_outputs)),class_targets])
print(loss)


average = np.mean(loss)

print(average)  