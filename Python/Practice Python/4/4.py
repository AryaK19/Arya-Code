# 20 random cards are placed in a row all faced down.A move consists of turning a face down card ,face up and then turning the card  immediatly to the right face up.Show that no matter what the choise of card to turn ,this sequence of  moves should terminate to all face up.

# face up = u
# face down = d 

import random as rn

list= []
for i in range(1,21):
    list.append('d')
print(list)

rno=0 
while (rno==0):
    a =rn.randint(0,18)
    try:
        rnno=1
        list.index('d')
    except ValueError:
        rnno = 0
    if rnno== 0:
        break
    else :
        if list[a]=='d':
            list[a] = "u"
        elif list[a+1]=='d':
            list[a+1] = "u"
        else :
            list[a+1] = "d"
        continue

print(list)