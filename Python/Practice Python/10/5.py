l1 = [1,2,4]
l2 = [3,5,6]
l = []
for items in l1:
    l.append(items)
for items in l2:
    l.append(items)
    

l.sort()
print(l)