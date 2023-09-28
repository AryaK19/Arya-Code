# creating an empty set and adding new things to it

b = set()
print(type(b))

b.add(2)
b.add(34)
b.add(1)
b.add(3)
b.add(4)
print(b)

# b.add([1,2,3,3])# list cant be added

b.add((1,2,3)) # but tuple can
print(b)

# b.add({1:3})# dic. can't be added
print(b)
# things that are not  changeble can be added
# can't can items in sets ,but can add

print(len(b)) # prints lenth
b.remove(2) # removes 
# b.remove(500) # error as not there 
print(b.pop()) # removes random value
print(b)
