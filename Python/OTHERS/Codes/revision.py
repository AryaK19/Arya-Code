print("Hello World")

print("\nTuple \n")
tuple1 = (1,2,3)
print(tuple1)

tuple2 = (2, "Hello", 4.4)
print(tuple2)

tuple3 = (1, [2,3,4], (5,6,7), "ThisPC")
print(tuple3)

tuple4 = ("1ElementOnly",)
print(tuple4)

print("\nindexing : \n")
thistuple = ("t", "h", "i", "s", "t", "u", "p", "l", "e")
print(thistuple[0])
print(thistuple[-2])
print(thistuple[0:4])
print(thistuple[:-4])

thistuple.count("t")

language = ("Python", "C", "Java", "HTML")
print("Python" in language)
print("C++" in language)

print("\nTaking an input and converting it into a list :\n")

abc = input('Enter some numbers here to make a list : ')
list1 = abc.split(" ")
print(list1)
list2=[]
for x in list1:
    list2.append(int(x))
print("Final list : ", list2)

