m1 = int(input('English (/100):'))
m2 = int(input('Science (/100):'))
m3 = int(input('Physics (/100):'))

if (m1 + m2 + m3 )>=((40/100)*300) :
    f = 1
else :
    f = 0


if (m1>=33):
    f1=1
else:
    f1=0
if (m2>=33):
    f2=1
else :
    f2 = 0
if (m3>=33):
    f3=1
else :
    f3=0

if f1+f2+f3 == 3 :
    a = 1 
else :
    a =0
if f + a == 2 :
    print('You passed!!')
else :
    print('You failed :(')
