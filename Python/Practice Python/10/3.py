matrix = [[5,4,3,9],
          [2,0,7,6],
          [1,3,4,0],
          [9,8,3,4]]
zero = []
for i in range(0,4):
    for j in range(0,4):
        if matrix[i][j] == 0:
            zero.append([i,j])
            
for k in range(0,4):
    for i,j in zero:
        matrix[i][k] = 0
        matrix[k][j] = 0          

print(matrix)
