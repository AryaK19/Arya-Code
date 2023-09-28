try:
    a = int(input("Enter a number"))
    c = 1/a
    a=int(a)
except ValueError as e :
    print("Exception1 occured.")
    print(e)
        
except ZeroDivisionError as e :
    print("Exception2 occured (0).")
    print(e)
    # and thus more types of more error ......
print("Thanks")