
def square(a):
    return (a*a)

l = [1,2,4]

# Method 1
l3=[]
for i in range(0,3):
    l3.append(square(l[i]))
print(l3)    

# Method 2 
l2=[]
for item in l:
    l2.append(square(item))
print(l2)

# method 3 

print(list(map(square,l)))


    

