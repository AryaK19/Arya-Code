# recursion

# n = 0
# a=1
# for i in range(n):
#     a = a * (i+1) 
# print(a)

def factorial_of(n):
    a=1    
    for i in range(n):
       a = a * (i+1) 
    return a 

# recursion calls itself just like loop.....
''' if u put the value of def in def you will loop it and
hence form a recursion and no need to use loop( it is calling  itself )
'''

def fac_recursive(n):
    if n ==1 or n==0 :
        return 1 
    else :
       return n * fac_recursive(n-1)

print(factorial_of(5))

f = fac_recursive(7)
print(f)

# be carefull not to make it repeat infinite....... 
# cant be stoped as loop can be ..... :0