a = [3,4,2,4,5,2,4,24,67,346]
# b=[]
# for item in a :
#     if item%2==0:
#         b.append(item)
# print(b)

#Shortcut to the write the same code (mage dar tarika) 
#if i write it inside the list itself it will work still
# same can be done woth set ,dictionary

b = [i for i in a if i%2==0]
s = {i for  i in a}
print(b)
print(s)