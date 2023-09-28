
list = ['donkey','partha','mad','pagal','guu']
with open('D:\python arya\chapter 9\problem set\\5\\5.txt') as f:
    content = f.read()

for a in list : # you have to use this kind of syntx for list
    if a in content :
        content = content.replace(a,'$#$%##')
    with open('D:\python arya\chapter 9\problem set\\5\\5.txt','w') as f:
        f.write(content)