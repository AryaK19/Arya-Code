with open('D:\python arya\chapter 9\problem set\\4\\4.txt') as f:
    content = f.read()
if 'donkey'in content :
    content = content.replace('donkey','$#$%##')
with open('D:\python arya\chapter 9\problem set\\4\\4.txt','w') as f:
    f.write(content)
        
        