import os


oldname="D:\python arya\chapter 9\problem set\9\9.txt"
newname="D:\python arya\chapter 9\problem set\9\\renamed_by_python.txt"

with open(oldname) as f :
    a = f.read()
with open(newname,'w') as f:
    f.write(a)

os.remove(oldname)

