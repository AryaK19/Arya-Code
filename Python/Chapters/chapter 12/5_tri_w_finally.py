#it will show print even if it exits 
# it woks inspite of stopting (it finnaly will to its job....!)

try:
    a = int(input("Enter a Number :"))
    c=1/a
except Exception as e :
    print(e)
    exit()
finally:
    print("we were successful")