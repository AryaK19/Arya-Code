
try:   
    with open("chapter 12\problem set\\1\\1.txt") as f :
        f=f.read
    with open("chapter 12\problem set\\1\\2.txt") as a :
        a=a.read
    with open("chapter 12\problem set\\1\\3.txt") as d :
        d=d.read
except FileNotFoundError :
    print("file not found")

print(f)
print(a)
print(d)
