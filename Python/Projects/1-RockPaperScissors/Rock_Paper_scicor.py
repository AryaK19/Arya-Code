import random

b = print('comp Turn : Rock(r), Paper(p) , Sciscor(s)?') 
a = input('Your Turn : Rock(r), Paper(p) , Sciscor(s)? :') 

c = random.randint(1,3)
if c == 1 :
    comp = 'r'
elif c == 2 :
    comp = 'p'    
elif c == 3 :
    comp= 's'

print("Comp:",comp)
print("You:",a)

if comp == a : 
    print ("It's a Tie!!")
elif comp == 'r'and a == 'p':
    print('You Win!! ')
elif comp == 'p'and a == 's': 
    print('You Win!! ')
elif comp == 's'and a == 'r': 
    print('You Win!! ')
else :
    print('You Lose :(')
