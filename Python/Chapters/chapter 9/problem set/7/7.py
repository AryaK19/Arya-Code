a = True
i=1

with open("D:\python arya\chapter 9\problem set\\6\\6.txt") as f :
    while a :
        a = f.readline()
        i+=1

        if 'python' in a.lower() :
            print(a)
            print('There is Python in the log file')
            print(i)
