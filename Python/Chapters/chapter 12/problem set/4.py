try:
    a = int(input("Enter a no.: "))
    b = int(input("Enter a no.: "))
    c = a/b
    print(f"{a}/{b} = {c}")
except ZeroDivisionError:
    print("Infinite")
except ValueError:
    print("Enter a Valid Number")
else :
    pass
