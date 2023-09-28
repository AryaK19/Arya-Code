#Create a code so that you can enter values as much as u want and when you press enter,you get the sum of all the no.s typed 

a =str((input("Enter The Price [in the format 1 2 3 ....]: ")))

with open("1.txt",'w') as f:
    f.write(a)

with open("1.txt") as f :
    p = f.read()
    p = p.split()
a=0
try:
    for i in range(0,len(p)) :
        a=a+int(p[i])
    print(a)
except Exception as e:
    print(e)