with open('D:\python arya\chapter 9\problem set\8\8.txt') as f :
    a = f.read()
b='copy'
with open(f'D:\python arya\chapter 9\problem set\8\\{b}.txt','w') as f :
    f.write(a)