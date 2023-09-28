letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']

i = 0
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]
I=[]
J=[]
K=[]
L=[]
M=[]
N=[]
O=[]
P=[]

while i <1000:
    for div in letters:
        i+=1
        eval(div).append(i+22210000)

# for div in letters:
#     print(div,eval(div))
#     print(len(eval(div)))

im = int(input("Enter Pin : "))

for div in letters:
    try:
        roll = eval(div).index(im)
        divi = div
    except ValueError:
        continue
    
if letters.index(divi)>0:
    inde = letters.index(divi)
    inde-=1
else:
    inde = 0
print(letters[inde],roll+1)