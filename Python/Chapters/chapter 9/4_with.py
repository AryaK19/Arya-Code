# the best way to open and do anything to the file is with "with"


with open ('D:\python arya\chapter 9\\arya.txt','a') as f:
    a = f.write('hi\n')
print(a)

with open ('D:\python arya\chapter 9\\arya.txt','r') as f:
    a = f.read()
    print(a)
