n = [3,7,1,2,8,4,5]
n.sort()
for i in range(0,len(n)):
    if i != n[i] - 1:
        print(i+1)
        break