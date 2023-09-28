e = 2.71828182845904

def Factorial(i):
    b = 1   
    for j in range(1,(i+1)):
        b = b * j
    return b

print("Value of e^x ")
x = int(input("Enter x :"))
ran = int(input("Enter range : "))

val = 1
for i  in range(1,ran):
    val = val + (x**i)/Factorial(i)
print(f"Value of e = {e}")
print(f"Your value = {val}")

