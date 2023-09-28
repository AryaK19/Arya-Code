#Something depend upon condition so yes or no

# 1.if-elif-else ladder( only the first true statement is taken )

a = 45 
if a>3 :
    print(a ,"is greater than 3")
elif a>7 :
    print(a ,'is greater than 7')
elif a>13 :
    print(a ,'is greater than 13')
elif a>17 :
    print(a ,'is greater than 17')
else :
    print(" The value is not greater than 3 or 7")

# 2. multiple if statements ( all the statements are taken)

a = 45 
if a>3 :                              #independent if statement 
    print(a ,"is greater than 3")
if a>7 :                              #independent if statement 
    print(a ,'is greater than 7')
if a>13 :                             #independent if statement 
    print(a ,'is greater than 13')

if a>17 :                             # this two are one ladder 
    print(a ,'is greater than 17')
else :
    print(" The value is not greater than 3 or 7")