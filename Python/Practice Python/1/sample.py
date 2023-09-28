i = input("Enter No.s : ")
i = list(i)

a = 0
for j in range(0,len(i)-1,2):
    a = int(i[j]) + a

print(a)