import random

with open('Python Arya\Projects\Projest_1 copy\score.txt') as f:
    u = f.read()
    s = u.split()
    if s[3] == "0" and s[7] == "0":
        o = int(input('Score limit :'))
    else :
        o=int(s[-1]) 


u = u.replace(str(s[-1]),str(o))
with open('Python Arya\Projects\Projest_1 copy\score.txt','w') as f:
    f.write(u)

b = print('comp Turn : Rock(r), Paper(p) , Sciscor(s)?') 
a = input('Your Turn : Rock(r), Paper(p) , Sciscor(s)? :') 


c = random.randint(1,3)

if c == 1 :
    comp = 'r'
elif c == 2 :
    comp = 'p'    
elif c == 3 :
    comp= 's'

if a == 'reset':
    pass
else:
    print("Comp:",comp)
    print("You:",a)

if a == 'reset':
    pass
else:
    if comp == a :
        print ("It's a Tie!!")
    elif comp == 'r'and a == 'p':
        k = True
        print('You Win!! ')
    elif comp == 'p'and a == 's':
        k = True 
        print('You Win!! ')
    elif comp == 's'and a == 'r':
        k = True 
        print('You Win!! ')
    else :
        k = False
        print('You Lose :(')

with open('Python Arya\Projects\Projest_1 copy\score.txt') as f:
    n = f.read()
    n = n.split()
        

ms = mns = 0
cs = cns = 0
ms = int(n[3])
cs = int(n[7])

if a == 'reset':
    print('Done!')
elif comp == a :
    cns = cs
    mns = ms
elif k :
    cns = cs
    mns = ms + 1 
else :
    mns = ms
    cns = cs + 1


q =f'YOUR SCORE : {ms}'
w =f'YOUR SCORE : {mns}'
z =f'COMP SCORE : {cs}'
x =f'COMP SCORE : {cns}'
jj=f'LIMIT      : {n[-1]}'
kk=f'LIMIT      : 1'

with open('Python Arya\Projects\Projest_1 copy\score.txt') as f:
    s = f.read()

with open('Python Arya\Projects\Projest_1 copy\score.txt','w') as f:
    if a == "reset":
        s = s.replace(q,'YOUR SCORE : 0')
        s = s.replace(z,'COMP SCORE : 0')
        s = s.replace(jj,kk)
        f.write(s)

s = s.replace(q,w)
s = s.replace(z,x)

with open('Python Arya\Projects\Projest_1 copy\score.txt','w') as f:
    f.write(s)

with open('Python Arya\Projects\Projest_1 copy\score.txt') as f:
    read = f.readline()
    print(read,end='')
    read = f.readline()
    print(read,end='')

with open('Python Arya\Projects\Projest_1 copy\score.txt') as f:
    n=f.read()
    n=n.split()
    t = n[-1]
    if int(mns)== int(t):
        print("Congratulations You Won !!!") 
    elif int(cns)== int(t):
        print("Better Luck Next Time.....")
    else :
        pass

