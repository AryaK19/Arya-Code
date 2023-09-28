a = int(input("Enter a no. :"))

b = [i*a for i in range(1,11)]

with open("chapter 12\problem set\\5\\5.txt","a") as f:
    f.write(str(b))
    f.write("\n")