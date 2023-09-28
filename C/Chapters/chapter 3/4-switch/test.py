a = int(input("Enter Your Marks (1-100) "))

if a in range(90,101):
    print("Grade : A")
elif a in range(80,90):
    print("Grade : B")
elif a in range(70,80):
    print("Grade : C")
elif a in range(60,70):
    print("Grade : D")
elif a in range(1,70):
    print("Grade : F")
else:
    print("Invalid Input!")