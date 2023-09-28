import math
# Cathagorical cross entrophy
soft_max = [0.7,0.1,0.2]
target_output = [1,0,0]
loss=0
for i in range(len(soft_max)):
    loss +=  math.log(soft_max[i])*target_output[i]

print(-loss)