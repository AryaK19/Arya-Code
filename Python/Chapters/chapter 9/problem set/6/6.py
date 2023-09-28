with open("D:\python arya\chapter 9\problem set\\6\\6.txt") as f :
    a = f.read()

if 'python' in a.lower() :
    print('There is Python in the log file')
else:
    print('There is no Python in the log file')