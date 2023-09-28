a = input('Write a string\n')
b = a.find("  ")
if b == -1 :
    print("There is no double space in the string")
else :
    print("There is/are double space/s in the string")
    print("The corrected version is :",a.replace("  "," "))   