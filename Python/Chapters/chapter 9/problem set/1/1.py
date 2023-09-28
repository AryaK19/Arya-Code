f = open ('D:\python arya\chapter 9\problem set\\1\poems.txt')
t = f.read()
if 'twinkle' in t :
    print("twinkle is present")
else :
    print("twinkle is not present")
f.close()